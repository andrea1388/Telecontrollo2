#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
import threading
import socket
import time

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

SHUNT_OHMS = 0.00086
MAX_EXPECTED_AMPS = 30
i=0
valori=[]


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


print "Server partito"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
x = threading.Thread(target=network, args=(s,))
x.start()
try:
    while True:
        valori.append(read())
        i=i+1
        if(i>24):
            valori.pop(0)
        print "v=", valori
        time.sleep(24*3600)
except KeyboardInterrupt:
    print('interrupted!')
    s.close()



# echo "da telecontrollo" | mail -s "test" iz3kzx@gmail.com