# py-daemon
# Author: Brendan Gasparin
# Last Modified: Monday 7th July 2025
# A simple daemon that listens and responds on a port.

import socket

HOST = '0.0.0.0'    # Listen on all interfaces
PORT = 6669          # TODO: Change this with a command line argument or a config file

def main():
    # Create a TCP socket
    daemon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    daemon_socket.bind((HOST, PORT))

    # Listen
    daemon_socket.listen(1)
    print("Py-Daemon is listening on port {PORT}...")

    # Loop forever (TODO: accept multiple clients at once with a threaded version)
    while True:
        # Accept a connection
        client_socket, client_address = daemon_socket.accept()
        print("Connected by {client_address}")

        # Send a message
        client_socket.sendall(b"Hello, world.\n")
        client_socket.sendall(b"I am Brendan's daemon.\n")
        client_socket.sendall(b"I have come to learn about you.\n")

        # TODO: Ask for a message and receive it

        # Close the Connection
        client_socket.close()


main()
