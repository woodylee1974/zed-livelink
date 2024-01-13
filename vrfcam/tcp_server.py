import socket
import threading


def handle_client_connection(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                continue
            print(f"Received: {data.decode()}")
            break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()


def start_tcp_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = '127.0.0.1'
    server_port = 6699

    # Bind the socket to the server address and port
    server_socket.bind((server_address, server_port))

    # Enable the server to accept connections
    server_socket.listen(5)
    print(f"Listening on {server_address}:{server_port}")

    try:
        while True:
            # Accept a connection
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            # Handle client connection in a new thread
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()


# Start the server
start_tcp_server()
