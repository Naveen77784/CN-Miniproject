import socket
import ssl
import threading
from booking import process_request
from storage import load_data

HOST = "0.0.0.0"
PORT = 5000

seats = load_data()

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode().strip()
            print(f"[REQUEST] {addr}: {message}")

            response = process_request(message, seats)

            conn.send(response.encode())

            if message.upper() == "EXIT":
                break

    except Exception as e:
        print(f"[ERROR] {addr} -> {e}")

    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def start_server():

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    secure_server = context.wrap_socket(server, server_side=True)

    print("[SERVER STARTED]")
    print(f"Listening on {HOST}:{PORT}")

    while True:
        conn, addr = secure_server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()