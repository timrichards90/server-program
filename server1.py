# import sys
# import socket
# import _thread
#
# # request handler
# def do_request(connectionSocket):
#
#     request = connectionSocket.recv(1024)
#     print(request)
#     response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, world!'
#     connectionSocket.send(response.encode())
#
#     # Close the connection
#     connectionSocket.close()
#
# def main(serverPort):
#
#     # Create the server socket object
#     mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # Bind the server socket to the port
#     mySocket.bind(('',serverPort))
#
#     # Start listening for new connections
#     mySocket.listen()
#     print('The server is ready to receive messages on port:', serverPort)
#
#     while True:
#         # Accept a connection from a client
#         connectionSocket, addr = mySocket.accept()
#
#         # Handle each connection in a separate thread
#         _thread.start_new_thread(do_request, (connectionSocket,))
#
#
# if __name__ == '__main__':
#
#     # serverPort = int(sys.argv[1])
#     serverPort = 8080
#     main(serverPort)
#
#
