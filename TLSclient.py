from socket import *
import time
import random
import json
import rsa
from pyDes import *
import binascii


class Client(object):
	_clientSocket = None
	serverName = '10.222.71.179'
	serverPort = 12000
	_client_random_num = None
	_server_random_num = None
	_server_public_key = None
	
	
	#def __init__(self):

		
	def connect(self):
        #serverName =  # 指定服务器IP地址
		#serverPort = 12000
        _clientSocket = socket(AF_INET, SOCK_STREAM) # 建立TCP套接字，使用IPv4协议
		print("try to connect with server...")
		_clientSocket.connect((serverName,serverPort))
	
	def client_handshake(self):
		print("start to handshake on client...")
		client_hello()
				
		msg_recv = None
		while msg_recv == None:
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))				
			if msg_recv["name"] == "server_hello":
				print("recieve hello from server")
				_server_random_num = msg_recv['random']
				print("server random number: ", _server_random_num)
				
		msg_recv = None
		while msg_recv == None:
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))
			if msg_recv['name'] == "server_certificate":
				server_cert = msg_recv['public key']
				if CertificateVerify(server_cert) == True:#验证通过，提取公
					_server_public_key = rsa.PublicKey.load_pkcs1(base64.b64decode(server_cert["publicKey"].encode()))
				else:
					print("fail to verify, exit")
					return		
					
		msg_recv = None
		while msg_recv == None:
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))
			if msg_recv['name'] == "server_hello_done":
				client_key_exchange()
				
		msg_recv = None
		while msg_recv == None:
			msg_recv = json.loads(_connectionSocket.recv(4096).decode('utf-8'))
			if msg_recv['name'] == "server_handshake_done":
				client_handshake_done()
		
		print("handshake done")
		print("start to send and receive data......")

			
				
##################### function #######################		
		
	def client_hello(self):#done
		random.seed(time.time())
		_client_random_num = random.randint(1, 999)
		_clientSocket.send(json.dumps({
        "name": "client_hello",
        "version": "TLSv1.2",
        "support algorithm": "RSA",
        "data": "DES",
        "hash": "SHA-256",
        "random": _client_random_num
		}).encode('utf-8'))
		
	def certificate(self):#若单向验证，则不需要此步
		with open("key/client.crt","r") as f:
			msg = str(f.read())
		connectionSocket.send(json.dumps({
        "name": "client_certificate",
        "public key": msg
		}).encode('utf-8'))		
		
	def CertificateVerify(self):
		return True
		
	def client_key_exchange(self):
		# get server public key
		#_server_public_key 
		
		# get client premaster key
		random.seed(time.time())
		num = random.randint(1, 999)
		_premaster_key = str(num).encode()
		
		# use RSA encrypt DES_key
		key = rsa.encrypt(_premaster_key,_server_public_key)
		keybyte = base64.b64encode(key).decode()
		_clientSocket.send(json.dumps({
        "name": "client_key_exchange",
        "client key": keybyte
		}).encode('utf-8'))	
		
		#calculate encrtpy master_key
		
			
		
	def client_handshake_done(self):# done
		_clientSocket.send(json.dumps({
        "name": "client_handshake_done"
		}).encode('utf-8'))	
		
	def encrypt_data(self,data):

    """
    DES 加密
    :param data: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = 
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)
    
    def send_data(self,data):
		
	
		
	

if __name__ == "__main__":
	clientSocket = Client()
	####	socket连接	####
	clientSocket.connect() # 向服务器发起连接
	
	####	进行TLS握手协议	####
	clientSocket.client_handshake()
	
	####	TLS加密发送		####
	clientSocket.send()
	
	####	socket连接断开	####
	clientSocket.close()
	