import socket
import ssl

HOST = "10.30.201.69"   # change to server IP
PORT = 5000

def start_client():

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_client = context.wrap_socket(client, server_hostname=HOST)

    secure_client.connect((HOST, PORT))

    print("Connected to secure server")

    while True:

        msg = input("Enter command (BOOK <seat> / VIEW / EXIT): ")
        secure_client.send(msg.encode())

        response = secure_client.recv(1024).decode()
        print("Server:", response)

        if msg.upper() == "EXIT":
            break

    secure_client.close()


if __name__ == "__main__":
    start_client()