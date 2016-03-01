#!/usr/bin/env python3
# echo.py
# author: Sébastien Combéfis
# version: February 15, 2016

import struct
import socket
import sys
from cryptage import *

SERVERADDRESS = (socket.gethostname(), 6000)
#CLIENTADDRESS = (socket.gethostname(), 4000)

class EchoServer():
    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVERADDRESS)


    def run(self):
        self.__s.listen(5)
        while True:
            client, addr = self.__s.accept()
            print(addr)
            people = []

            #try:
            acces, port = self._receive(client)
            if acces == True:
                i = 0
                people.append(addr)
                people.append(port)
                print(people[i])
                client.sendall('prout')
                '''
                while 1:
                    sendpeople = people[i]
                    if not sendpeople: break
                    client.sendall(str(sendpeople[1]).encode())
                    '''
            else:
                print(acces)
            client.close()
            #except OSError:
                #print('Erreur lors de la réception du message.')

    def _receive(self, client):
        chunks = []
        finished = False
        acces = 'nop'
        while not finished:
            data = client.recv(1024)
            chunks.append(data)
            finished = data == b''
        message = b''.join(chunks).decode()
        password, port = message.split(':')
        with open('mdp.txt', 'r') as us:
            user_pass = us.read()
        if check_password(user_pass, password):
            acces = True
        return acces, port

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        EchoServer().run()
    elif len(sys.argv) == 3 and sys.argv[1] == 'client':
        EchoClient(sys.argv[2].encode()).run()
