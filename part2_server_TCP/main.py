from socket import *
serverPort = 5566
# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# server begine listening for incoming TCP requests
serverSocket.listen(1)
print("The server is ready to receive")
count = 0
while True:
    # server waits an accept for incoming request
    connectionSocket, addr = serverSocket.accept()
    # increase the counter for each accept and print the counter
    count = count+1
    print(count)
    # closing the TCP socket Connection
    connectionSocket.close()
