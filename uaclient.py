#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import time
from datetime import date

config = sys.argv[1]
metodo = sys.argv[2]
opcion = sys.argv[3]
peticion = config + ' ' + metodo + ' ' + opcion 

class uaCLIENT(ContentHandler):

    def __init__ (self):

        self.Lista = []
        self.Diccionario = {'account': ['username', 'passwd'],
                            'uaserver': ['ip', 'puerto'],
                            'rtpaudio': ['puerto'], 'regproxy':['ip', 'puerto'],
                            'log':['path'], 'audio':['path']}

#    if len(sys.argv) != 4:
#        sys.exit("Usage: python uaclient.py config method option")

    def startElement(self, etiqueta, atrib):
        if etiqueta in self.Diccionario:
            Dicc = {}
            for atributo in self.Diccionario[etiqueta]:
                Dicc[atributo] = atrib.get(atributo, "")
            self.Lista.append([etiqueta, Dicc])

    def get_tags(self):
        return self.Lista

if __name__ == "__main__":

    parser = make_parser()
    MyHandler = uaCLIENT()
    parser.setContentHandler(MyHandler)
    parser.parse(open(config))
    Lista_xml = MyHandler.get_tags()
    account_us = Lista_xml[0][1]['username']
    account_passwd = Lista_xml[0][1]['passwd']
    uaserver_ip = Lista_xml[1][1]['ip']
    uaserver_puerto = Lista_xml[1][1]['puerto']
    rtpaudio_puerto = Lista_xml[2][1]['puerto']
    regproxy_ip = Lista_xml[3][1]['ip']
    regproxy_puerto = Lista_xml[3][1]['puerto']
    log_path = Lista_xml[4][1]['path']
    audio_path = Lista_xml[5][1]['path']

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((uaserver_ip, int(uaserver_puerto)))

def log(formato, evento, linea)
    fichero = log_path
    fichero_log = open(fichero, 'a')
    formato = '%Y%m%d%H%M%S'
    hora_actual = datetime.now().strftime(formato)
    hora = fich.write(hora_actual())

    if evento == "enviar":
        fichero_log.write(' Sent to ' + regproxy_ip + ":" + str(regproxy_puerto) +
                        ": " + linea + '\r\n')
    elif evento == "recibir":
        fichero_log.write(' Received from ' + regproxy_ip + ":" + str(regproxy_puerto) +
                        ": " + linea + '\r\n')
    elif evento == "error":
        fichero_log.write(' Error: ' + linea + '\r\n')
    elif evento == "Comenzar"
        fichero_log.write(' Starting... ')
    elif evento == "Finalizar"
        fichero_log.write('


    
    
    
    

    if metodo == "REGISTER" or "INVITE" or "ACK" or "BYE":
        print("Enviando:", peticion)
        my_socket.send(bytes(peticion, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)

print('Recibido --', dara.decode('utf-8'))
print("Terminando socket...")

