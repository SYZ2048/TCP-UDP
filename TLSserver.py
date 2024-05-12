from socket import *
import time
import random
import rsa
from pyDes import *
import binascii


class Server(object):
	_serverSocket = None
	_serverName = None
	_serverPort = None
	_server_random_num = None
	_connectionSocket = None
	_addr = None
	
	#def __init__(self):
		
	
	def connect(self):
		_serverPort = 12000
		_serverSocket = socket(AF_INET, SOCK_STREAM) # 建立TCP套接字，使用IPv4协议
		_serverSocket.bind(('',_serverPort)) # 将TCP欢迎套接字绑定到指定端口
		_serverSocket.listen(1) # 最大连接数为1
		
	def server_handshake(self):
		connectionSocket, _addr = _serverSocket.accept() # 接收到客户连接请求后，建立新的TCP连接套接字
		print('Accept new connection from %s:%s...' % _addr)
		
		msg_recv = None
		while msg_recv == None:		
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))
			if msg['name'] = "client_hello":#收到了client_hello
				algorithm = msg['support algorithm']	
				#回复server_hello
				server_hello()
				time.sleep(2)
				#发送certificate
				certificate()
				time.sleep(2)
				# 若单向验证，不需要此步
				#certificate_request()
				server_hello_done()
				time.sleep(2)
		
		msg_recv = None
		while msg_recv == None:
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))
			if msg_recv['name'] = "client_key_exchange": #收到了client_key_exchange
				#解析client密钥
				##############################
				##############################
				server_handshake_done()
				
		print("handshake done")
		print("start to send and receive data......")
		
	
	
##################### function #######################		
		
	def server_hello(self):
		random.seed(time.time())
		_server_random_num = random.randint(1, 999)
		connectionSocket.send(json.dumps({
        "name": "server_hello",
        "version": "TLSv1.2",
        "support algorithm": "RSA",
        "data": "DES",
        "hash": "SHA-256",
        "random": _server_random_num
		}).encode('utf-8'))	
		
	def certificate(self):
		with open("key/server.crt","r") as f:
			msg = str(f.read())
		connectionSocket.send(json.dumps({
        "name": "server_certificate",
        "public key": msg,
		}).encode('utf-8'))	
		
	def server_key_exchange(self):
		#if algorithm is "RSA", no action needed 
	
	def certificate_request(self):
		connectionSocket.send(json.dumps({
        "name": "certificate_request",
		}).encode('utf-8'))	
	
	def server_hello_done(self):
		connectionSocket.send(json.dumps({
        "name": "server_hello_done",
		}).encode('utf-8'))			
		
		
	def server_handshake_done(self):
		connectionSocket.send(json.dumps({
        "name": "server_handshake_done"
		}).encode('utf-8'))	
		
	def communicate(self):
		print("handshake done!!start to communicate...")
		while True:
			
	

	
		

print("The server in ready to receive")

if __name__ == "__main__":
	serverSocket = Server()
	####	socket连接	####
	serverSocket.connect() # 向服务器发起连接
	
	####	进行TLS握手协议	####
	serverSocket.server_handshake()
	
	####	TLS加密发送		####
	serverSocket.send()
	
	####	socket连接断开	####
	serverSocket.close()