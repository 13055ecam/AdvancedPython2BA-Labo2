# server.py
# author: Chagnot William
# version: March 2, 2016

import threading
import pickle
import struct
import socket
import sys
from cryptage import *

SERVERADDRESS = (socket.gethostbyname(socket.gethostname()), 6000)

class EchoServer():
    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVERADDRESS)


    def run(self):
        self.__s.listen(5)
        people = []
        while True:
            client, addr = self.__s.accept()
            acces, name, ip, port = self._receive(client)
            if acces == True:
                people.append(name)
                people.append(ip)
                people.append(port)
                msg_people = pickle.dumps(people)
                client.send(msg_people)
                client.close()
            else:
                wrongco = []
                wrongco.append(acces)
                wrongco.append('Wrong password')
                msg_wrongco = pickle.dumps(wrongco)
                client.send(msg_wrongco)
                client.close()

    def _receive(self, client):
        acces = False
        data = client.recv(1024)
        self.__message = pickle.loads(data)
        password = self.__message[1]
        with open('mdp.txt', 'r') as us:
            user_pass = us.read()
        if check_password(user_pass, password):
            acces = True
        return acces, self.__message[0], self.__message[2], self.__message[3]

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        EchoServer().run()
    elif len(sys.argv) == 3 and sys.argv[1] == 'client':
        EchoClient(sys.argv[2].encode()).run()
