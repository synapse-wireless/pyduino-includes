SNAPpy Includes for the Pyduino Development Board
===================================

Introduction
------------

`pyduinoincludes` is a SNAPpy library that is designed to make development for the Synapse Pyduino board easier. It
allows references to the nifty Pyduino IO names (like D3, AD0, or SCL) instead of the underlying SNAPpy GPIO numbers.
It also provides a bit-banged SPI implementation that can be used for shields that utilize the SPI pins.

Installation
------------

### For use in Portal

Download and extract the latest release zip file to Portal's `snappyImages` directory. 
By default, this is located at `...\Documents\Portal\snappyImages` on Windows.

### For use with SNAPbuild

The easiest way to install `pyduinoincludes` for use with SNAPbuild is using 
[pip](https://pip.pypa.io/en/latest/installing.html):

    pip install git+https://github.com/synapse-wireless/pyduino-includes.git@master

Alternatively you can download the source, extract it, and install it:

    python setup.py install

Usage
-------------

In order to use the nice IO names, simply import `pyduinoincludes` in your SNAPpy script like this:

```python
from pyduinoincludes import *
    
def drive_d4_pin_high():
    setPinDir(D4, True)
    writePin(D4, True)
```

Pins can be referenced as follows:

| Pin Type | Pyduino IO Name |
|----------|-----------------|
| Digital  | D0 - D13        |
| Analog   | A0 - A5         |
| i2c      | SDA, SCL        |

Setting up the SPI pins is very simple, too:

```python
from pyduinoincludes.spi import *

def my_spi_function():
    spi_init()  # Sets up the bit-banged SPI
    spi_write("\x12\x34\x56")  # Write data to the SPI bus
    spi_read(4)  # Read four bytes from the SPI bus
```
