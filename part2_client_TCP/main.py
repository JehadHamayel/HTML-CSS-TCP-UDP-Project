#Jehad Hamayel 1200348
#Lama Naser 1200190
from socket import *
#sending numbers from zero to one mellion
for y in range(0, 1000000):
    serverName = "localhost"
    serverPort = 5566
    # create TCP socket for server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #create connection between server and client
    clientSocket.connect((serverName, serverPort))
    #sending the message
    clientSocket.send(str(y).encode())
    #closing the socket after each request
    clientSocket.close()
