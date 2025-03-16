import socket                  #required for network connections

def start_server(host='127.0.0.1', port=65432):         #listens on local host with port number
    """Starts a simple TCP server that listens for client requests."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))          #binds the server/socket to the host and port
        server_socket.listen()                    #listens for incoming connections
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()          #accepts the connection
            with conn:
                print(f"Connected by {addr}")              #prints the address of the client
                data = conn.recv(1024)
                if not data:                        #if no data is received,
                    break
                print(f"Received: {data.decode()}")
                response = "Hello from server, this is what the client sees.!"      #response from server
                conn.sendall(response.encode())          #sends the response to the client

if __name__ == "__main__":
    start_server()
