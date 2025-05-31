import socket
import threading

def handle_send(conn):
    while True:
        msg = input()
        conn.send(msg.encode())
        if msg.lower() == 'exit':
            break

def handle_receive(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg.lower() == 'exit':
                print("Chat ended.")
                break
            print("Friend:", msg)
        except:
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    threading.Thread(target=handle_send, args=(conn,)).start()
    threading.Thread(target=handle_receive, args=(conn,)).start()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to the server.")

    threading.Thread(target=handle_send, args=(client_socket,)).start()
    threading.Thread(target=handle_receive, args=(client_socket,)).start()

if __name__ == '__main__':
    mode = input("Enter mode (server/client): ").strip().lower()
    if mode == 'server':
        start_server()
    elif mode == 'client':
        start_client()
    else:
        print("Invalid mode! Please enter 'server' or 'client'.")
