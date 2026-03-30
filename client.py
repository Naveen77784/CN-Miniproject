import socket
import ssl
import threading
import time
import sys

HOST = "192.168.68.109"
PORT = 5000

TIMEOUT = 3  

last_activity = time.time()
running = True


def timeout_checker(sock):
    global last_activity, running

    while running:
        if time.time() - last_activity > TIMEOUT:
            print("\nSession timed out due to inactivity.")

            running = False  

            break  

        time.sleep(1)


def start_client():
    global last_activity, running

    try:
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations("cert.pem")
        context.check_hostname = False

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_client = context.wrap_socket(client, server_hostname=HOST)

        secure_client.connect((HOST, PORT))

        print("Secure connection established")

        # Start timeout thread
        threading.Thread(target=timeout_checker, args=(secure_client,), daemon=True).start()

        while running:
            try:
                message = input("Enter command (BOOK <seat> / VIEW / EXIT): ")
            except:
                break

            if not running:
                break

            last_activity = time.time()

            try:
                secure_client.send(message.encode())
                response = secure_client.recv(1024).decode()
                print("Server:", response)
            except:
                break

            if message.upper() == "EXIT":
                running = False
                break

        secure_client.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    start_client()
