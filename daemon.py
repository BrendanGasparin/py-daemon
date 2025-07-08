# py-daemon
# Author: Brendan Gasparin
# Last Modified: Monday 7th July 2025
# A simple daemon that listens and responds on a port.

import socket
import threading

HOST = '0.0.0.0'    # Listen on all interfaces
PORT = 6669          # TODO: Change this with a command line argument or a config file

def main():
    # Create a TCP socket
    daemon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    daemon_socket.bind((HOST, PORT))

    # Listen
    daemon_socket.listen(1)

    # Loop forever (TODO: accept multiple clients at once with a threaded version)
    try:
        while True:
            # Accept connections
            conn, address = daemon_socket.accept()

            # Start handle_client as a thread with each user so we can handle multiple connections
            client_thread = threading.Thread(target=handle_client, args =(conn, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server closed by user.")
    # Close the Connection
    finally:
        daemon_socket.close()


def handle_client(conn, addr):
    print(f"[+] New connection from {addr}")
    try:
        # Send a message (TODO: Get a response)
        conn.sendall(b"Hello, world.\n")
        conn.sendall(b"I am Brendan's daemon.\n")
        conn.sendall(b"I have come to learn about you.\n")
    finally:
        conn.close()



if __name__ == "__main__":
    main()
