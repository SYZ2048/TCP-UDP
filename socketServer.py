#import socket module
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # 创建TCP欢迎套接字，使用IPv4协议
#Prepare a sever socket 
#Fill in start 
serverSocket.bind(('',serverPort)) # 将TCP欢迎套接字绑定到指定端口
serverSocket.listen(1) # 最大连接数为1
#Fill in end 

while True:     
#Establish the connection      
    print('Ready to serve...')
    connectionSocket, addr =   serverSocket.accept()
    print('接受一个客户端连接:', addr)
#Fill in start  #Fill in end
    try:         
        message = connectionSocket.recv(1024) #Fill in start  #Fill in end
        filename = message.split()[1]                          
        f = open(filename[1:])
        outputdata = f.read() #Fill in start  #Fill in end
        #Send one HTTP header line into socket         
        #Fill in start
        header =  'HTTP/1.1 200 OK'  
        connectionSocket.send(header.encode())
        #print(header)     
        #Fill in end    

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        #print(header)
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end  
           
serverSocket.close()
