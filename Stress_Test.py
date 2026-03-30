import socket
import ssl
import threading
import time

HOST = "192.168.68.109"
PORT = 5000

NUM_CLIENTS = 10   # change to 20, 50, etc for heavy load


def client_task(client_id):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_client = context.wrap_socket(sock, server_hostname=HOST)

        start_time = time.time()

        secure_client.connect((HOST, PORT))

        # each client tries booking different seat
        seat_number = client_id + 1
        message = f"BOOK {seat_number}"

        secure_client.send(message.encode())

        response = secure_client.recv(1024).decode()

        end_time = time.time()

        print(f"[Client {client_id}] {response} | Time: {end_time - start_time:.4f}s")

        secure_client.close()

    except Exception as e:
        print(f"[Client {client_id}] Error:", e)


threads = []

start = time.time()

for i in range(NUM_CLIENTS):
    t = threading.Thread(target=client_task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

print("\n=== Stress Test Complete ===")
print(f"Total Clients: {NUM_CLIENTS}")
print(f"Total Time: {end - start:.2f}s")
