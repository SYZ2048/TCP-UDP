from socket import *
import base64
msg = "I love computer networks!"  #要发送的消息内容
endmsg = "\r\n.\r\n"
# Choose a mail server 
mailserver = 'smtp.qq.com' #Fill in start   #Fill in end  #根据发送方邮箱确定邮箱服务器（qq邮箱的服务器为smtp.qq.com;163邮箱为smtp.163.com）

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM) # 建立TCP套接字，使用IPv4协议
clientSocket.connect((mailserver,serverPort)) # 向服务器发起连接
# 建立TCP套接字，使用IPv4协议
# 向服务器发起连接
#Fill in end

#第一步 建立连接返回代码220
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':     
    print('220 TCP reply not received from server.')

# Send HELO command and print server response.开始与服务器的交互，服务器将返回状态码250
heloCommand = 'HELO qq.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 HELO reply not received from server.')

# send AUTH LOGIN command  发送"AUTH LOGIN"命令，开始验证身份，服务器将返回状态码235
# Fill in start
# 账户密码可以telnet认证
LoginCommand = 'AUTH LOGIN\r\n'
clientSocket.send(LoginCommand.encode())
username = '136014634@qq.com'   #MTM2MDE0NjM0QHFxLmNvbQ==
usernamebyte = base64.b64encode(username.encode('utf-8'))+b'\r\n'
password = 'chbkedagcypvbjbj'   #Y2hia2VkYWdjeXB2Ympiag==
passwordbyte = base64.b64encode(password.encode('utf-8'))+b'\r\n'
while True:
    recvlogin_command = clientSocket.recv(1024).decode()
    if recvlogin_command[:3] == '334':
        break        
clientSocket.send(usernamebyte)
while True:
    recvUsername = clientSocket.recv(1024).decode()
    if recvUsername[:3] == '334':
        break       
clientSocket.send(passwordbyte)
while True:
    recvPss = clientSocket.recv(1024).decode()
    if recvPss[:3] == '235':
        break

# print(recv2)
# if recv2[:3] != '235':
#     print('235 LOGIN reply not received from server.')
#base64.b64encode(***)  # base64编码函数
# Fill in end

# Send MAIL FROM command and print server response.发送"MAIL FROM"命令，并包含发件人邮箱地址，服务器将返回状态码250
# Fill in start
mailCommand = 'MAIL FROM: <136014634@qq.com>\r\n'
clientSocket.send(mailCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 FROM reply not received from server.')
#mailCommand = 'MAIL FROM: <' + send_mail_addr + '>\r\n'
#接下来clientSocket.send并接受返回的消息
# Fill in end

# Send RCPT TO command and print server response.发送"RCPT TO"命令，并包含收件人邮箱地址，服务器将返回状态码250
# Fill in start
RCPTCommand = 'RCPT TO:<19307130359@fudan.edu.cn>\r\n'
clientSocket.send(RCPTCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 TO reply not received from server.')
# Fill in end

# Send DATA command and print server response.发送"DATA"命令，表示即将发送邮件内容，服务器将返回状态码354
# Fill in start
DATACommand = 'DATA\r\n'
clientSocket.send(DATACommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '354':
    print('354 DATA reply not received from server.')
# Fill in end

# Send message data.发送邮件内容
# Fill in start
mailmsg = 'FROM: <136014634@qq.com>\r\n' + 'TO:<19307130359@fudan.edu.cn>\r\n' + 'Subject:network\r\n' + '\r\n' +msg
clientSocket.send(mailmsg.encode())
#mailmsg = '' + msg #邮件头部+正文要发送的消息内容
#clientSocket.send()
# Fill in end 

# Message ends with a single period.  服务器将返回状态码250
# Fill in start
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 MSG reply not received from server.')
#发送邮件结尾信息 clientSocket.send(endmsg.encode())
#接收返回的消息，判断是否为250，输出
# Fill in end

# Send QUIT command and get server response.发送"QUIT"命令，断开与邮件服务器的连接。
# Fill in start
QuitCommand = 'QUIT\r\n'
clientSocket.send(QuitCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '221':
    print('221 QUIT reply not received from server.')
# Fill in end

# close
clientSocket.close()
