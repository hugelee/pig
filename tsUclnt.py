#!/usr/local/bin/python
#author : lizb
#date : 2017/10/30

from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input('> ')
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, addr = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data

udpCliSock.close()