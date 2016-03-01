#!/usr/bin/env python3
# echo.py
# author: Sébastien Combéfis
# version: February 15, 2016

import struct
import socket
import sys
from cryptage import *

SERVERADDRESS = (socket.gethostname(), 6000)
CLIENTADDRESS = (socket.gethostname(), 4000)

'''class EchoServer():
    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVERADDRESS)


    def run(self):
        self.__s.listen(5)
        while True:
            client, addr = self.__s.accept()

            print(addr)
            people = []

            try:
                acces, port = self._receive(client)
                if acces == True:
                    i = 0
                    host = socket.gethostname()
                    people.append(host)
                    people.append(port)
                    print(people)''''''

                    self.__s.connect(CLIENTADDRESS)
                    totalsent = 0
                    while i < len(people):
                        msg = people[i].encode
                        print(msg)
                        try:
                            while totalsent < len(msg):
                                sent = client.send(msg[totalsent:])
                                totalsent += sent
                        except:
                            print('pas parti =/')
                        i += 1
                    ''''''
                else:
                    print(acces)
                client.close()
            except OSError:
                print('Erreur lors de la réception du message.')

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
'''

class EchoClient():
    def __init__(self, message):
        self.__message = message
        self.__s = socket.socket()
        self.__s.bind(CLIENTADDRESS)

    def run(self):
        #try:
            self.__s.connect(SERVERADDRESS)
            self._send()
            self.__s.listen(5)
            server, addr = self.__s.accept()
            print(addr)
            #try:
            '''while True:
                self.__s.listen(5)
                server, addr = self.__s.accept()
                chunks = []
                finished = False
                while not finished:
                    data = server.recv(1024)
                    chunks.append(data)
                    finished = data == b''
                    print(b''.join(chunks).decode())'''
            #except:
                    #print('Fail')
            self.__s.close()
        #except OSError:
            print('Serveur introuvable, connexion impossible.')

    def _send(self):
        totalsent = 0
        msg = self.__message
        try:
            while totalsent < len(msg):
                sent = self.__s.send(msg[totalsent:])
                totalsent += sent
        except OSError:
            print("Erreur lors de l'envoi du message.")


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        EchoServer().run()
    elif len(sys.argv) == 3 and sys.argv[1] == 'client':
        EchoClient(sys.argv[2].encode()).run()
