# import socket
#
# def main(host, port):
#     clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     clientSocket.connect((host, port))
#
#     # Send request for headers only without the payload
#     # request = '\r\n'.join(['HEAD / HTTP/1.1', 'Host:www.google.com', '\r\n'])
#     request = 'hello from my client'
#     clientSocket.send(request.encode())
#
#     response = clientSocket.recv(1024)
#     print(response, len(response))
#
# if __name__ == '__main__':
#
#     # host = 'www.google.co.nz'
#     # port = 80
#
#     host = 'localhost'
#     port = 8080
#     main(host, port)
