#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.00086
MAX_EXPECTED_AMPS = 30


def read():
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
    ina.configure(ina.RANGE_16V)

    print("Bus Voltage: %.1f V" % ina.voltage())
    try:
        print("Bus Current: %.0f mA" % ina.current())
        print("Power: %.1f W" % (ina.power()/1000))
        print("Shunt voltage: %.1f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
        print(e)


if __name__ == "__main__":
    read()
