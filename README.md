# Drivers for Microchips (Examples)

## Overview
This repository contains Python scripts for interfacing with the following devices:
- **AD7999**: An I2C-based 4-channel 10-bit ADC.
- **CAT5171**: A digital potentiometer with I2C communication.
- **DAC8551**: A SPI-based 16-bit DAC.
- **ADG604**: A CMOS analog multiplexer, comprising four single channels.

The devices were used in circuits implemented on **Raspberry Pi 4**.

## Dependencies
Ensure you have the following dependencies installed before running the scripts:
```bash
pip install smbus2 RPi.GPIO numpy spidev
```

## Files and Functionality
### `AD7999.py`
This script provides an interface for the AD7999 ADC, allowing users to:
- Configure the ADC channel.
- Read raw ADC data.
- Convert ADC data to voltage.


### `cat5171.py`
This script provides an interface for the CAT5171 digital potentiometer, allowing users to:
- Read resistance values.
- Change resistance via 8-bit values or percentage.
- Set operation modes (normal, shutdown, reset).


### `dac8551.py`
This script controls the DAC8551 DAC using SPI communication, allowing users to:
- Output digital-to-analog signals in a continuous loop.

### `ADG604.py`
This script controls the ADG604 Analog Multiplexer, allowing users to:
- Choose a switch position (0–3).
- Control which input/output path is enabled in the ADG604 analog switch.
- Set digital outputs on ports 10 and 12 of the PCA9671, which control the ADG604 switch selection.
- Work with I2C-controlled hardware instead of direct GPIO pins.
