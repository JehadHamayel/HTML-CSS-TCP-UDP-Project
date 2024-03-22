#Jehad Hamayel 1200348
#Lama Naser 1200190
from socket import *
serverName = "localhost"
serverPort = 5566
# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)
for x in range(0, 1000000):
    # attach server name and server port to message, send into socket
    clientSocket.sendto(str(x).encode(),(serverName,serverPort))
#closing the socket
clientSocket.close()