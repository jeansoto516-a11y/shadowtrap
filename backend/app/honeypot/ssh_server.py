import socket


def start_ssh_honeypot():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reutilizar a porta
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = "0.0.0.0"
    port = 2222

    server.bind((host, port))

    server.listen(5)

    print(f"[SHADOWTRAP] Honeypot ativo na porta {port}")

    while True:

        client, address = server.accept()

        print(f"[ALERTA] Nova conexão detectada: {address}")

        client.close()