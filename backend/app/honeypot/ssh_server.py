import socket
import threading

import paramiko

from app.core.config import settings
from app.honeypot.auth_handler import SSHAuthHandler
from app.honeypot.command_logger import log_connection, log_event
from app.honeypot.fake_terminal import run_fake_shell


def _build_server_socket(host: str, port: int) -> socket.socket:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(50)
    server.settimeout(1)
    return server


def _handle_client(client: socket.socket, address, host_key: paramiko.RSAKey) -> None:
    ip, client_port = address
    log_connection(ip, client_port)

    transport = None

    try:
        transport = paramiko.Transport(client)
        transport.local_version = "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3"
        transport.add_server_key(host_key)

        auth_handler = SSHAuthHandler(ip, client_port)
        transport.start_server(server=auth_handler)

        channel = transport.accept(20)
        if channel is None:
            log_event("channel_timeout", ip=ip, port=client_port)
            return

        run_fake_shell(channel, ip, client_port, auth_handler.username)
    except Exception as exc:
        log_event("client_error", ip=ip, port=client_port, error=str(exc))
    finally:
        if transport is not None:
            transport.close()
        client.close()


def start_ssh_honeypot(stop_event: threading.Event | None = None) -> None:
    stop_event = stop_event or threading.Event()
    host_key = paramiko.RSAKey.generate(2048)

    try:
        server = _build_server_socket(settings.honeypot_host, settings.honeypot_port)
    except OSError as exc:
        log_event(
            "server_start_error",
            host=settings.honeypot_host,
            port=settings.honeypot_port,
            error=str(exc),
        )
        return

    log_event("server_started", host=settings.honeypot_host, port=settings.honeypot_port)

    with server:
        while not stop_event.is_set():
            try:
                client, address = server.accept()
            except TimeoutError:
                continue
            except OSError as exc:
                log_event("server_error", error=str(exc))
                break

            thread = threading.Thread(
                target=_handle_client,
                args=(client, address, host_key),
                daemon=True,
            )
            thread.start()

    log_event("server_stopped", host=settings.honeypot_host, port=settings.honeypot_port)
