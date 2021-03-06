import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    # GET URI HTTP/1.1
    #  /hello.html   - DOCROOT
    print(request.decode('utf8'))

    # Sending the headers
    # then send the body of the response
    # if the URI starts with /cgi-bin  Then dynamic page
    http_response = """\
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello, World!</h1>
"""
    client_connection.sendall(http_response.encode('utf8'))
    client_connection.close()
