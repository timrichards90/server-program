# import sys
# import socket
# import _thread
#
#
# def parse_http(request):
#     hsep = '\r\n'
#     headers = request.decode().split(hsep)
#
#     request_line = headers.pop(0)
#     payload = headers.pop()
#     cmd, path, prot = request_line.split()
#
#     return cmd, path, headers, payload
#
# # request handler
# def do_request(connectionSocket):
#     request = connectionSocket.recv(1024)
#     cmd = parse_http(request)
#     # print(request)
#     # print('cmd ', cmd, 'path ', path)
#     response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, world!'
#     connectionSocket.send(response.encode())
#
#     # Close the connection
#     connectionSocket.close()
#
#
# def main(serverPort):
#     # Create the server socket object
#     mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # Bind the server socket to the port
#     mySocket.bind(('', serverPort))
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
#     # serverPort = int(sys.argv[1])
#     serverPort = 8080
#     main(serverPort)
