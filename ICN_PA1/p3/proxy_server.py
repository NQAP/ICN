import socket

# Set the server IP address and port
# TODO Start
HOST, PORT = '127.0.0.1', 9999
# TODO end

# Create a server socket, bind it to the specified IP and port, and start listening
# TODO Start
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
# TODO end

while True:
    print('Ready to serve...')
    # Accept an incoming connection and get the client's address
    # TODO Start
    client_socket, client_address = serverSocket.accept()
    # TODO end

    print('Received a connection from:', client_address)

    try:
        # Receive and parse the client's request
        # TODO Start
        request = client_socket.recv(1024).decode('utf-8')
        # TODO end
        print(request)       

        # Extract the requested filename from the HTTP request
        if request == "":
            request = "/ /"
        filename = request.split()[1].partition("/")[2]
        print(filename)
        file_path = "/" + filename
        print(file_path)

        # Check if the requested file is available in the cache
        file_exist = "false"
        try:
            with open(file_path[1:], "rb") as cache_file:
                output_data = cache_file.read()
            file_exist = "true"
            
            # ProxyServer finds a cache hit and generates a response message
            # Send the file data to the client
            # TODO Start
            response = b'HTTP/1.1 200 OK\r\n\r\n'
            content = output_data
            client_socket.sendall(response + content)
            # TODO End
            print('Read from cache')

        # If the file is not found in the cache, forward the request to the web server
        except FileNotFoundError:
            if file_exist == "false":
                # # Establish a connection to the web server
                # TODO Start
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s_HOST, s_PORT = '127.0.0.1', 2077
                # TODO End

                try:
                    print("Trying to connect to the web server")
                    # Connect the socket to the web server port
                    # TODO Start
                    s.connect((s_HOST, s_PORT))
                    # TODO End
                    print("Connected successfully")

                    # Send HTTP GET request to the web server
                    # TODO Start
                    s.send(request.encode('utf-8'))
                    # TODO End
                    print("Sent the request to the web server successfully")


                    # Receive response from the web server    
                    # If the response indicates a 404 error, return an error to the client without caching
                    # TODO Start
                    response = s.recv(1024).decode('utf-8')
                    temp = response.split('\r\n\r\n', 1)
                    http_msg = temp[0]
                    content = temp[1]
                    client_socket.sendall(response.encode('utf-8'))
                    if '404' not in http_msg:
                        with open(file_path[1:], "w") as f:
                            f.write(content)
                    # TODO End                    

                    # If not, cache only valid files and send the valid response to the client socket
                    # TODO Start
                    # TODO End

                except:
                    # Handle errors related to connection issues or invalid requests
                    print("Illegal request")

                finally:
                    # Ensure the connection to the web server is closed properly
                    # TODO Start
                    s.close()
                    # TODO End
    finally:
        # Close the client socket
        client_socket.close()