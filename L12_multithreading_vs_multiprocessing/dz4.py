import socket
import threading

HOST = "127.0.0.1"
PORT = 8080


def handle_client(client_socket, client_address: tuple) -> None:
    """Handle a single client's HTTP request
     """
    print(f"Client connected: {client_address}")

    request = client_socket.recv(1024).decode()
    print(request)

    response_body = "Hello! This is a multithreaded web server."
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )

    client_socket.sendall(response.encode())
    client_socket.close()

    print(f"Client disconnected: {client_address}")


def start_server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()

        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()


start_server()
