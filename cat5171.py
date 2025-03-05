class digipot:
    import smbus

    bus = smbus.SMBus(1)
    
    def __init__(self, address):
        self.address = address  #Default value in LSB is low so default state is a write operation
        self.instruction = 0x00
        self.operation = "normal"
        
    #Read current byte and resistance (in kohms)
    def readResistance(self):
         data = digipot.bus.read_byte(self.address) #SMBus handles the bit shifting and LSB condition for R/W
         resistance = data/255 * 50
         return [data, resistance, self.operation]
    
    #Instruction byte for shutdown or reset
    def instructionSet(self, state):
        if state == "shutdown":
            digipot.bus.write_byte(self.address, 0x20)
            self.instruction = 0x20
            self.operation = "shutdown"
            return 1
        elif state == "reset":
            digipot.bus.write_byte(self.address, 0x40)
            self.instruction = 0x40
            self.operation = "reset"
            return 1
        elif state == "normal":
            digipot.bus.write_byte(self.address, 0x00)
            self.instruction = 0x00
            self.operation = "normal"
            return 1
        else:
            return 0
        
    #Write 8 bit decimal values
    def writeData(self, data):
        if data <= 0 or data >= 255:
            return 0
        elif data >= 0 and data <= 255:
            digipot.bus.write_i2c_block_data(self.address, self.instruction,[data])
            return 1
            
    #Define resistance 0 - 100kOhm in kOhms, step = 440.6 Ohm per tap
    def resistance(self, resValue):
        if resValue > 100 or resValue < 0:
            return 0
        elif resValue < 0.05:
            data = 0
        
        data = round((resValue)/50 * 255) #Add 50ohm contact resistance
        digipot.bus.write_i2c_block_data(self.address, self.instruction,[data])  
        return 1  
        
    #Define percentage from 0 to 100
    def percentage(self, percent):
        if percent >= 0 and percent <= 100:
            data = round(255*(percent/100))
            digipot.bus.write_i2c_block_data(self.address, self.instruction,[data])
            return 1
        else:
            return 0
        
    
        
    
        