## File: solution.py
## Name: Luis Grados

# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("192.168.1.20", port))

  #Creates socket to listen
  serverSocket.listen(5)


  while True:
    #Establish the connection
    #print('Ready to serve...')
    
    #Accept incoming requests
    connectionSocket, addr = serverSocket.accept()
 
    try:

      try:
        #Define bits of data to receive
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])

        #Display file contents
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        #Close client socket
        connectionSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)