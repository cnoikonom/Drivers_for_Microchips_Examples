class ad7999:
    from smbus2 import SMBus, i2c_msg
    import RPi.GPIO as GPIO
    import time
    import numpy as np

    bus = SMBus(1)

    def __init__(self, Vref, addr):
        self.Vref = Vref
        self.address = addr

    def writeData(self, channel):
        if channel < 0 or channel > 3:
            raise ValueError("Value must be 0-3")
        
        configs = 0x03

        if channel == 0:
            configs |= 0x10
        elif channel == 1:
            configs |= 0x20
        elif channel == 2:
            configs |= 0x40
        elif channel == 3:
            configs |= 0x80
        
        self.bus.write_i2c_block_data(self.address, configs, [])
        return 1
    
    def readData(self):
        msg =  self.i2c_msg.read(self.address, 2)
        self.bus.i2c_rdwr(msg)
        data_list = list(msg)
        data = ((data_list[0] & 0x0F) << 4) | (data_list[1] >> 4)
        return data
    
    def readVoltage(self):
        data = self.readData()
        voltage = (data / 256) * self.Vref
        return voltage


        
