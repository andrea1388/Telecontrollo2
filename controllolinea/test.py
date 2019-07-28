#!/usr/bin/env python2.7
# script by Andrea Carrara https://github.com/andrea1388/Telecontrollo2
# 
# pp c ll
# pp: password 2 chr
# c:  comando [0|1]
# ll: numero linea su 2 chr es. 02

import time 
elementi=0
toni = []
password = ["5","0"]
tempo_ultimotono=time.time()

while True:

    g = raw_input("simbolo [0-9],*#ABCD : ")
    if((time.time()-tempo_ultimotono) > 5) :
        elementi=0
        toni = []
        print("stato 0")
    tempo_ultimotono=time.time()
    toni.append(g)
    if(toni.count()==5) :
        processa
    print (toni)


def processa(toni):
    if(toni[0]!=password[0]):
        print("pass errata")
        return
    if(toni[1]!=password[1]):
        print("pass errata")
        return

    l=ord(toni[4])+10*ord(toni[3])
    if(l<1 | l>16):
        print("linea errata")
        return
    print("linea=",l)
    if(toni[2]=="0"):
        print("spegni")
        return
    if(toni[2]=="1"):
        print("accendi")
        return



