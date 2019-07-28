#!/usr/bin/env python2.7
# script by Andrea Carrara https://github.com/andrea1388/Telecontrollo2
# 
# pp c ll
# pp: password 2 chr
# c:  comando [0|1]
# ll: numero linea su 2 chr es. 02

import time
import subprocess
import RPi.GPIO as GPIO
import time
toni = []
password = ["1","1"]
tempo_ultimotono=time.time()
parametriE2speak = "-v it -p 70 -s 155 2>/dev/null"
clpath="/usr/Telecontrollo2/controllolinea/"
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both

chan_list = [17,21,22,23,24]
GPIO.setup(chan_list, GPIO.IN)
carattere = ["D","1","2","3","4","5","6","7","8","9","0","*","#","A","B","C"]


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
        subprocess.check_output([clpath+"controllolinea.sh",str(l),"off"])
        subprocess.call([clpath + "parla.sh","spento "+str(l)])
        # print(cmd)
        return
    if(toni[2]=="1"):
        subprocess.check_output([clpath+"controllolinea.sh",str(l),"on"])
        subprocess.call([clpath + "parla.sh","acceso "+str(l)])
        # print(cmd)
        return
    if(toni[2]=="2"):
        out=subprocess.check_output([clpath+"leggilinea.sh",str(l)])
        if(out[0] == "0"):
            #subprocess.call(["./parla.sh"])
            subprocess.call([clpath + "parla.sh",str(l)+ "spento "])
        if(out[0] == "1"):
            subprocess.call([clpath + "parla.sh",str(l)+ "acceso "])
        # print(cmd)
        return
    return


def my_callback(channel):
    print GPIO.input(21),GPIO.input(22),GPIO.input(23),GPIO.input(24)
    t=GPIO.input(21) + GPIO.input(22)*2 + GPIO.input(23)*4 + GPIO.input(24) *8
    print "Ricevuto tono", carattere[t]
    if((time.time()-tempo_ultimotono) > 5) :
        toni = []
        print("stato 0")
    tempo_ultimotono=time.time()
    toni.append(carattere[t])
    if(len(toni)==5) :
        processa(toni)
        toni = []
    print (toni)





# when a falling edge is detected on port 17, regardless of whatever 
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback, bouncetime=300)
print "ciao"

while True:
    # print GPIO.input(27),GPIO.input(22),GPIO.input(23),GPIO.input(24)
    time.sleep(1)




GPIO.cleanup()           # clean up GPIO on normal exit
