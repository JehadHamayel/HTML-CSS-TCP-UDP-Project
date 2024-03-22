from socket import *
serverPort = 5566
# create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# bind socket to local port 5566
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
count = 0
while True:
    # read from UDP socket into message, getting client's address
    message, clientAddress = serverSocket.recvfrom(2048)
    # increase the counter for each receive and print the counter
    count = count+1
    print(count)
