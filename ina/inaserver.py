#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
import threading
import socket
import time
import os


HOST = '127.0.0.1'
PORT = 50007

SHUNT_OHMS = 0.00086
MAX_EXPECTED_AMPS = 30
i=0
valori=[]
VAllarme=12.0
VRiarmo=12.3
InibisciAllarmi=True

def MandaAllarme():
    myCmd = 'echo "da telecontrollo Cesen 1500" | mail -s "Allarme tensione" iz3kzx@gmail.com iw3gcb@gmail.com'
    os.system(myCmd)

def read():
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
    ina.configure(ina.RANGE_16V)
    return ina.voltage()
"""     print("Bus Voltage: %.1f V" % ina.voltage())
    try:
        print("Bus Current: %.0f mA" % ina.current())
        print("Power: %.1f W" % (ina.power()/1000))
        print("Shunt voltage: %.1f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
        print(e)
 """
def network(s):
    print "listener partito"
    while True:
        try:
            conn, addr = s.accept()
        except socket.error as msg:
            print msg
            break
        print 'Connected by', addr
        conn.sendall(str(valori))
        conn.close()
    print "listener morto"



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
x = threading.Thread(target=network, args=(s,))
x.start()
print "Server partito"
try:
    while True:
        v=read()
        valori.append(v)
        i=i+1
        if(i>24):
            valori.pop(0)
        print "v=", valori
        if(v<VAllarme and InibisciAllarmi==False):
            MandaAllarme()
            InibisciAllarmi=True
            print('Inviato allarme')
        if(v>VRiarmo):
            InibisciAllarmi=False
            print('Riabilitato invio allarmi')
        time.sleep(3600)
except KeyboardInterrupt:
    print('interrupted!')
    s.close()



# echo "da telecontrollo" | mail -s "test" iz3kzx@gmail.com