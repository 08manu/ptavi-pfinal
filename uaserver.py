#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import time
from datetime import date

config = sys.argv[1]

class uaSERVER(ContentHandler):

    def __init__ (self):

        self.Listaserv = []
        self.Diccionarioserv = {'account': ['username', 'passwd'],
                            'uaserver': ['ip', 'puerto'],
                            'rtpaudio': ['puerto'], 'regproxy':['ip', 'puerto'],
                            'log':['path'], 'audio':['path']}

    def startElement(self, etiqueta, atrib):
        if etiqueta in self.Diccionarioserv:
            Diccserv = {}
            for atributo in self.Diccionarioserv[etiqueta]:
                Diccserv[atributo] = atrib.get(atributo, "")
            self.Listaserv.append([etiqueta, Diccserv])

    def get_tags(self):
        return self.Listaserv

if __name__ == "__main__":

    if len(sys.argv) == 2:
        parser = make_parser()
        MyHandler = uaSERVER()
        parser.setContentHandler(MyHandler)
        parser.parse(open(config))
        Listaserv_xml = MyHandler.get_tags()
        account_us = Listaserv_xml[0][1]['username']
        account_passwd = Listaserv_xml[0][1]['passwd']
        uaserver_ip = Listaserv_xml[1][1]['ip']
        uaserver_puerto = Listaserv_xml[1][1]['puerto']
        rtpaudio_puerto = Listaserv_xml[2][1]['puerto']
        regproxy_ip = Listaserv_xml[3][1]['ip']
        regproxy_puerto = Listaserv_xml[3][1]['puerto']
        log_path = Listaserv_xml[4][1]['path']
        audio_path = Listaserv_xml[5][1]['path']

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((regproxy_ip, int(regproxy_puerto))) #Conecto con el proxy

        #suponemos que Leonard ya esta autorizado
        peticion = "REGISTER" + " sip:" + account_us + ":" + uaserver_puerto + " " + "SIP/2.0\r\n"
        print("Enviando:", peticion)
        my_socket.send(bytes(peticion, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido --', data.decode('utf-8'))

        
    else:
        sys.exit("Usage: python uaserver.py config")
