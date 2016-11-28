#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class uaCLIENT(ContentHandler):

    def __init__ (self):

        self.Lista = []
        self.Diccionario = {'account': ['username', 'passwd'], 'uaserver': ['ip', 'puerto'], 'rtpaudio': ['puerto'], 'regproxy':['ip', 'puertp'], 'log':['path'], 'audio':['path']}

    if len(sys.argv) != 4:
        sys.exit("Usage: python uaclient.py config method option")

    def startElement(self, etiqueta, atrib)
        Dicc = {}
        etiqueta in self.Diccionario:

if __name__ == "__main__":


    fichero = open(sys.argv[1], "r")
    for archivo in fichero.readlines()
        print(archivo)
    config = sys.argv[2]
    metodo = sys.argv[3]
    opcional = sys.argv[4]

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((config))

