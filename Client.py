import socket

def start_client(host='127.0.0.1', port=65432):
    """Starts a simple TCP client that connects to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello world!, this is what the client see"
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024)
        print(f"Server response: {data.decode()}")

if __name__ == "__main__":
    start_client()
