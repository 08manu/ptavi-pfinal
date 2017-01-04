#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import socketserver

config = sys.argv[1]

class uaSERVER(ContentHandler):

    def __init__ (self):

        self.Listaprox = []
        self.Diccionarioprox = {'server': ['name', 'ip', 'puerto'],
                            'database': ['path', 'passwdpath'],
                            'log': ['path'],}

    def startElement(self, etiqueta, atrib):
        if etiqueta in self.Diccionarioprox:
            Diccprox = {}
            for atributo in self.Diccionarioprox[etiqueta]:
                Diccprox[atributo] = atrib.get(atributo, "")
            self.Listaprox.append([etiqueta, Diccprox])

    def get_tags(self):
        return self.Listaprox

class EchoHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        while 1:
            line = self.rfile.read()
            if not line:
                break
            print("El cliente nos manda " + line.decode('utf-8'))
            lista = line.decode('utf-8')
            (account_us, uaserver_puerto, sip) = lista.split()
            if metodo == "REGISTER":
                self.wfile.write(b"SIP/2.0  401 Unauthorized")

if __name__ == "__main__":

    if len(sys.argv) == 2:
        parser = make_parser()
        MyHandler = uaSERVER()
        parser.setContentHandler(MyHandler)
        parser.parse(open(config))
        Listaprox_xml = MyHandler.get_tags()
        regproxy_ip = Listaprox_xml[0][1]['ip']
        regproxy_puerto = int(Listaprox_xml[0][1]['puerto'])
        serv_prox = socketserver.UDPServer((regproxy_ip, regproxy_puerto), EchoHandler)
        print("Listening")
        serv_prox.serve_forever()
        
    else:
        sys.exit("Usage: python proxy_registrar.py config")
