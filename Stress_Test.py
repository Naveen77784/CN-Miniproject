import socket
import ssl
import threading
import time

HOST = "10.30.201.69"
PORT = 5000

def client_task():

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = context.wrap_socket(s, server_hostname=HOST)

    s.connect((HOST, PORT))

    start = time.time()

    s.send("BOOK 10".encode())
    response = s.recv(1024)

    end = time.time()

    print("Response:", response.decode(), "Time:", end-start)

    s.close()


threads = []

for i in range(10):
    t = threading.Thread(target=client_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()