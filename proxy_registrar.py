#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

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

    def log(
        fichero = Listaprox_xml

if __name__ == "__main__":

    if len(sys.argv) == 2:
        parser = make_parser()
        MyHandler = uaSERVER()
        parser.setContentHandler(MyHandler)
        parser.parse(open(config))
        Listaprox_xml = MyHandler.get_tags()
    else:
        sys.exit("Usage: python proxy_registrar.py config")
