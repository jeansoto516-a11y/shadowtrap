import socket
from datetime import datetime


def start_ssh_honeypot():

    # Cria socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reutilização da porta
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Host e porta
    host = "0.0.0.0"
    port = 2222

    # Bind
    server.bind((host, port))

    # Escuta conexões
    server.listen(5)

    print(f"[SHADOWTRAP] Honeypot ativo na porta {port}")

    # Loop principal
    while True:

        # Aceita conexão
        client, address = server.accept()

        # Captura IP e porta
        ip = address[0]
        client_port = address[1]

        # Captura horário atual
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Exibe alerta formatado
        print("\n==============================")
        print("[ALERTA] Nova conexão detectada")
        print(f"[IP] {ip}")
        print(f"[PORTA] {client_port}")
        print(f"[HORARIO] {timestamp}")
        print("==============================")

        # Fecha conexão
        client.close()