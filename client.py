import socket
import ssl

HOST = "192.168.68.107"
PORT = 5000

def start_client():

    try:
        # Create SSL context
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

        # Trust the server certificate
        context.load_verify_locations("cert.pem")
        context.check_hostname = False
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        secure_client = context.wrap_socket(client, server_hostname=HOST)

        # Attempt connection
        secure_client.connect((HOST, PORT))

        print("Secure connection established")

        while True:

            message = input("Enter command (BOOK <seat> / VIEW / EXIT): ")

            secure_client.send(message.encode())

            response = secure_client.recv(1024).decode()
            print("Server:", response)

            if message.upper() == "EXIT":
                break

        secure_client.close()

    # Certificate verification failure
    except ssl.SSLCertVerificationError:
        print("SSL Error: Certificate verification failed. Connection aborted safely.")

    # General SSL errors
    except ssl.SSLError as e:
        print("SSL handshake failed:", e)

    # Network connection errors
    except ConnectionRefusedError:
        print("Could not connect to server.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    start_client()