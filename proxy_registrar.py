#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import socketserver
from datetime import date, datetime
import time

config = sys.argv[1]

class uaSERVER_PROX(ContentHandler):

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

    Dicc_serv = {}

    def ServidorRegistro(self):
        fich_serv = open('basededatos.txt', 'w')
        fich_serv.write("Fichero de texto con los usuarios registrados:\r\n")
        print(self.Dicc_serv)
        #dicc_new = self.Dicc_serv
        #dicc_newnew = dicc_new.dict.keys()
        #print(self.dicc_newnew)
        for usuario in self.Dicc_serv.keys():
            us = self.Dicc_serv[usuario][0]
            ip = self.Dicc_serv[usuario][1]
            puerto = self.Dicc_serv[usuario][2]
            fecha_registro = self.Dicc_serv[usuario][3]
            expires = self.Dicc_serv[usuario][4]
            fich_serv.write(us + ' ' + ip + ' ' + puerto + ' ' + str(fecha_registro) + ' ' + str(expires))

    def handle(self):
        while 1:
            line = self.rfile.read()

            if not line:
                break
            print("El cliente nos manda " + line.decode('utf-8'))
            lista = line.decode('utf-8')
            metodo = lista.split(' ')[0]
            print(lista)
            if metodo == "REGISTER":
                print(lista.split())
                us = lista.split(' ')[1].split(':')[1]
                ip = str(self.client_address[0])
                port = lista.split(' ')[1].split(':')[2]
                expires = lista.split(' ')[3]
                fecha_registro = datetime.now()

                if len(lista.split()) == 5:
                    nonce = 898989898798989898989
                    mensaje = "SIP/2.0  401 Unauthorized" + '\r\n'"WWW Authenticate: Digest nonce =" + ' ' + str(nonce) + '\r\n'
                    self.wfile.write(bytes(mensaje, 'utf-8'))
                elif len(lista.split()) > 5:
                    mensaje = "SIP/2.0 200 OK" + '\r\n'
                    self.wfile.write(bytes(mensaje, 'utf-8'))
                    self.Dicc_serv[us] = [us, ip, port, fecha_registro, expires] #insertamos elementos en el diccionario
                #Esto es para Leonard
                #elif len(lista.split()) == 3:
                    #mensaje = "SIP/2.0 200 OK" + '\r\n'
                    #self.wfile.write(bytes(mensaje, 'utf-8'))
                    #self.Dicc_serv[us] = [us, ip, port]
            #elif metodo == "INVITE":
                    

            self.ServidorRegistro()
            self.borrarExpirados()

    def borrarExpirados(self):
        lista_us = []
        for us in self.Dicc_serv:
            fecha_registro = self.Dicc_serv[us][3]
            fecha_registro_seg = fecha_registro.second
            fecha_actual = datetime.now()
            fecha_act_seg = fecha_actual.second
            expiracion = self.Dicc_serv[us][4]
            if (fecha_registro_seg + int(expiracion)  <= fecha_act_seg):
                lista_us.append(us)
        for cliente in lista_us:
            del self.Dicc_serv[cliente] #Eliminamos el elemento del diccionario

                
if __name__ == "__main__":

    if len(sys.argv) == 2:
        #hora = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        #hora_prueba = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(1233213))
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        parser = make_parser()
        MyHandler = uaSERVER_PROX()
        parser.setContentHandler(MyHandler)
        parser.parse(open(config))
        Listaprox_xml = MyHandler.get_tags()
        regproxy_ip = Listaprox_xml[0][1]['ip']
        regproxy_puerto = int(Listaprox_xml[0][1]['puerto'])
        serv_prox = socketserver.UDPServer((regproxy_ip, regproxy_puerto), EchoHandler)
        print("Listening")
        print(hora_actual)
        serv_prox.serve_forever()
        
    else:
        sys.exit("Usage: python proxy_registrar.py config")
