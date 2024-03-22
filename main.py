#Jehad Hamayel 1200348
#Lama Naser 1200190
from socket import *
serverPort = 7788
# create TCP socket for client
serverSocket = socket(AF_INET, SOCK_STREAM)
# bind socket to local port 7788
serverSocket.bind(('', serverPort))
# server begin listening for incoming TCP requests
serverSocket.listen(1)
print("The server is ready to receive")
flag = 1
while True:
    # server waits an accept for incoming request
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    # taking the IP and port for client
    ip = addr[0]
    port = addr[1]
    # sometimes the client send an empty request i do this code to solve this problem
    if(len(sentence) == 0):
        continue
    print(sentence)
    # spliting the request and take the first line
    x = sentence.split("\n")
    # spliting the first line to take the kind of the request
    y = x[0].split("/")
    # to take the name of the file that the request want
    t = y[1].split(" ")
    # to take the extention of the name of the file in the request
    r = t[0].split(".")
    i=0
    # if statement for insure of the right extention
    if len(r) < 2:
        i = 0
    else:
        i = 1
    # cases for the different file requests
    if t[0].__eq__("main_en.html") or t[0].__eq__("") or t[0].__eq__("index.html") or t[0].__eq__("en"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f1 = open("main_en.html", "r")
        print("in en")
        connectionSocket.send(str(f1.read()).encode())
    elif t[0].__eq__("main_en.css"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/css \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("main_en.css", "r")
        print("in main_en.css")
        connectionSocket.send(str(f2.read()).encode())
    elif t[0].__eq__("main_ar.css"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/css \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("main_ar.css", "r")
        print("in main_ar.css")
        connectionSocket.send(str(f2.read()).encode())
    elif t[0].__eq__("form.html"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("form.html", "r")
        print("in form.html")
        connectionSocket.send(str(f2.read()).encode())
    elif t[0].__eq__("pic2.png") :
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: image/png \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("pic2.PNG", "rb")
        print("in pic2.png")
        connectionSocket.send(f2.read())
    elif t[0].__eq__("pic1.jpg"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: image/jpg \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("pic1.JPG", 'rb')
        print("in pic1.jpg")
        connectionSocket.send(f2.read())
    elif r[i].__eq__("ar") and (len(r) == 1):
            connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
            connectionSocket.send(str("Content-Type: text/html;charset=utf-8 \r\n").encode())
            connectionSocket.send(str("\r\n").encode())
            f2 = open("main_ar.html","rb")
            print("in ar")
            connectionSocket.send(f2.read())
    elif r[i].__eq__("html")and (len(r) >= 2) and (not (t[0].__eq__("main_en.html") or t[0].__eq__("") or t[0].__eq__("index.html") or t[0].__eq__("en"))):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("any.html", "r")
        print("in any.html")
        connectionSocket.send(str(f2.read()).encode())
    elif t[0].__eq__("error.css"):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/css \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("error.css", "r")
        print("in error.css")
        connectionSocket.send(str(f2.read()).encode())
    elif r[i].__eq__("css") and (len(r) >= 2) and (not (t[0].__eq__("main_en.html") or t[0].__eq__("") or t[0].__eq__("index.html") or t[0].__eq__("en"))):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: text/css \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("any.css", "r")
        print("in any.css")
        connectionSocket.send(str(f2.read()).encode())
    elif r[i].__eq__("png") and (len(r) >= 2) and (not (t[0].__eq__("main_en.html") or t[0].__eq__("") or t[0].__eq__("index.html") or t[0].__eq__("en"))):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: image/png \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("any.PNG", "rb")
        print("in any.PNG")
        connectionSocket.send(f2.read())
    elif r[i].__eq__("jpg") and (len(r) >= 2) and (not (t[0].__eq__("main_en.html") or t[0].__eq__("") or t[0].__eq__("index.html") or t[0].__eq__("en"))):
        connectionSocket.send(str("HTTP/1.1 200 OK \r\n").encode())
        connectionSocket.send(str("Content-Type: image/jpg \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("any.JPG", 'rb')
        print("in any.jpg")
        connectionSocket.send(f2.read())
    elif r[i].__eq__("go") and (len(r) == 1):
        connectionSocket.send(str("HTTP/1.1 307 Temporary Redirect \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("Location: https://www.google.com \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
    elif r[i].__eq__("so") and (len(r) == 1):
        connectionSocket.send(str("HTTP/1.1 307 Temporary Redirect \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("Location: https://stackoverflow.com/ \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
    elif r[i].__eq__("bzu") and (len(r) == 1):
        connectionSocket.send(str("HTTP/1.1 307 Temporary Redirect \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("Location: https://ritaj.birzeit.edu/ \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
    else:
        connectionSocket.send(str("HTTP/1.1 404  Not Found \r\n").encode())
        connectionSocket.send(str("Content-Type: text/html \r\n").encode())
        connectionSocket.send(str("\r\n").encode())
        f2 = open("error.html", 'r')
        print("in error.html")
        connectionSocket.send(str(f2.read()+"Ip:"+ str(ip) + " Port:" + str(port)).encode())

    connectionSocket.close()
