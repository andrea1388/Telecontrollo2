#!/usr/bin/env python2.7
# script by Andrea Carrara https://github.com/andrea1388/Telecontrollo2
# 
# pp c ll
# pp: password 2 chr
# c:  comando [0|1]
# ll: numero linea su 2 chr es. 02

import time
import subprocess
elementi=0
toni = []
password = ["1","1"]
tempo_ultimotono=time.time()
parametriE2speak = "-v it -p 70 -s 155 2>/dev/null"



def processa(toni):
    """Processa la sequenza di toni"""
    if(toni[0]!=password[0]):
        print("pass errata")
        return
    if(toni[1]!=password[1]):
        print("pass errata")
        return

    l=int(toni[4])+10*int(toni[3])
    if(l<1 or l>16):
        print("linea errata")
        return
    print("linea=",l)
    if(toni[2]=="0"):
        subprocess.check_output(["controllolinea",str(l),"off"])
        # print(cmd)
        return
    if(toni[2]=="1"):
        subprocess.check_output(["controllolinea",str(l),"on"])
        # print(cmd)
        return
    if(toni[2]=="2"):
        out=subprocess.check_output(["leggilinea",str(l)])
        subprocess.call(["espeak"])
        # print(cmd)
        return
    return






while True:

    g = raw_input("simbolo [0-9],*#ABCD : ")
    if((time.time()-tempo_ultimotono) > 5) :
        elementi=0
        toni = []
        print("stato 0")
    tempo_ultimotono=time.time()
    toni.append(g)
    if(len(toni)==5) :
        processa(toni)
        toni = []
    print (toni)


