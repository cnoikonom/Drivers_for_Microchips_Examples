import spidev

spi = spidev.SpiDev()
spi.open(1,0)

spi.max_speed_hz = 1000000
#spi.mode = 0b01

while True:
	for i in range(0, 65536, 16):
		spi.xfer2([0b00011000, i>>8, i&0xff])

