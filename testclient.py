#!/usr/bin/env python3
# echo.py
# author: Sébastien Combéfis
# version: February 15, 2016

import struct
import socket
import sys
from cryptage import *

SERVERADDRESS = ('TourWilliam', 6000)
CLIENTADDRESS = (socket.gethostname(), 6000)

class EchoClient():
    def __init__(self, message):
        self.__message = message
        self.__s = socket.socket()

    def run(self):
        try:
            self.__s.connect(SERVERADDRESS)
            self._send()

            '''
            data = self.__s.recv(4096)
            print(data)
            '''

            self.__s.close()
        except OSError:
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
