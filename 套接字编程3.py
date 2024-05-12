from socket import *


""" if len(sys.argv) <= 1:
    print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2) """

# 为代理服务器 创建一个TCP套接字、绑定端口号、设置服务器最大连接客户机数量
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
IP = ''
serverPort = 12000
tcpSerSock.bind((IP,serverPort))
tcpSerSock.listen(8)
print(f'服务端启动成功，在{serverPort}端口等待客户端连接...')
# Fill in end.


while 1:
    # 准备从客户机接收响应消息
    print("---------------------------------------------")
    print('准备从客户机接收响应消息...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('接收到一个连接，来自：', addr)

    # 获取客户机发送过来的消息
    # Fill in start.   
    message = tcpCliSock.recv(4096)
    message_str = message.decode()
    # Fill in end.
    print('客户机发送过来的消息：', message_str)
    if(message == ''):
        continue

    # 从消息从提取出文件名
    filename = message_str.split()[1].partition("//")[2].replace('/', '_')
    #http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html
    print('文件名：', filename)#gaia.cs.umass.edu_wireshark-labs_INTRO-wireshark-file1.html
    fileExist = "false"

    try:
        # 检查要访问的文件是否在此Web代理服务器中
        print('开始检查代理服务器中是否存在文件：', filename)
        f = open(filename, "r")
        outputdata = f.read()
        fileExist = "true"
        print('文件存在在代理服务器中')
        # 文件存在在代理服务器中，返回响应消息(请求的web网页)给客户机
        #tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        #tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        tcpCliSock.send(outputdata.encode())
        print("文件从代理服务器中读取成功")
        # Fill in end.


    # 文件不在代理服务器当中，代理服务器就会向远端服务器请求消息，保存好了再返回给客户机
    except IOError:
        if fileExist == "false":
            print('文件不在代理服务器当中，开始向远端服务器请求网页')
            # 在代理服务器中创建一个TCP套接字 
            # Fill in start.  
            c = socket(AF_INET, SOCK_STREAM) 
            # Fill in end.

            hostn = message_str.split()[1].partition("//")[2].partition("/")[0]
            print('Host Name: ', hostn)
            try:
                # TCP套接字c 连接到远端服务器80端口
                # Fill in start.  
                c.connect((hostn,80))
                print("connect succ")
                c.send(message)
                # Fill in end.

                # 在套接字上创建一个临时的文件，而且要向80端口(远端服务器)请求信息
                # for the file requested by the client
                # fileobj = c.makefile('r', 0)
                # fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
                
                # 代理服务器 读取 从远端服务器从响应的消息
                # Fill in start.
                # resp_msg = fileobj.readlines()
                resp_msg = c.recv(4096)
                print(resp_msg.decode())
                # Fill in end.
                #400 Bad Request Your browser sent a request that this server could not understand

                # 在代理服务器中 创建一个新的文件 用于存放请求过来的消息
                # 将代理服务器中的响应 发送到客户端套接字，并将相应的文件发送到缓存中
                
                # Fill in start.                
                tmpFile = open("./" + filename, "wb")
                tmpFile.write(resp_msg)
                tcpCliSock.send(resp_msg)
                print("文件从远程服务器中读取成功")
                # Fill in end.


            except:
                print("代理服务器向远端服务器请求网页失败")
        else:
            # 如果客户机请求的消息在远端服务器也找不到，就说明请求不到了
            print('文件存在，但是还是出现了 IOError异常')

    # 关闭客户机 和 代理服务器的TCP套接字
    # Fill in start.
    print('关闭套接字：tcpCliSock & c')
    tcpCliSock.close()
    c.close()
    # Fill in end.
    

# 关闭代理服务器 和 服务器的TCP套接字
print('关闭套接字：tcpSerSock')
tcpSerSock.close()
