from socket import *

serverName = 'hostname' #IP address or hostname of server
serverPort = 1200

clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input lowercase sentence: ')

clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)


print(modifiedMessage)

clientSocket.close()


