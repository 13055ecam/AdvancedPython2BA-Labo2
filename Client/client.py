# client.py
# author: Chagnot William
# version: March 2, 2016

import threading
import pickle
import struct
import socket
import sys

SERVERADDRESS = ('TourWilliam', 6000)  #instead of 'TourWilliam' you need to put your server address

class EchoClient():
    def __init__(self):
        self.__s = socket.socket()
        CLIENTADDRESS = (socket.gethostbyname(socket.gethostname()), 4000)
        self.__s.bind(CLIENTADDRESS)
        self.message = CLIENTADDRESS

    def run(self):
        self.__s.connect(SERVERADDRESS)
        ip = socket.gethostbyname(socket.gethostname())
        print('Name?')
        name = input()
        print('Password?')
        password = input()
        print('On which port will you listen on?')
        port = input()
        new_co = [name, password, ip, port]
        self.__message = pickle.dumps(new_co)
        self._send()
        bipeople = self.__s.recv(1024)
        people = pickle.loads(bipeople)
        i = 0
        if len(people) == 2:  #len(people) == 2 if the user use a wrong password
            print(people[1])
        else:
            print('People you may try to join')
            while i < len(people):
                print('Name : ', people[i], 'IP : ', people[i+1], 'Port : ', people[i+2])
                i += 3
        self.__s.close()

    def _send(self):
        totalsent = 0
        msg = self.__message
        try:
            while totalsent < len(msg):
                sent = self.__s.send(msg[totalsent:])
                if sent != None:
                    totalsent += sent
        except OSError:
            print("Not send")

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        EchoServer().run()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        EchoClient().run()
