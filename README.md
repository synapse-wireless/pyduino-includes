SNAPpy Includes for the Pyduino Development Board
===================================

Introduction
------------

`pyduino-includes` is a SNAPpy library that is designed to make development for the Synapse Pyduino board easier. It
allows references to the nifty Pyduino IO names (like D3, AD0, or SCL) instead of the underlying SNAPpy GPIO numbers.

Installation
------------

The easiest way to install `pyduino-includes` is using 
[pip](https://pip.pypa.io/en/latest/installing.html):

    pip install git+ssh://git@git.synapse-wireless.com/tyler.crumpton/pyduino-includes.git@master

Alternatively you can download the source, extract it, and install it:

    python setup.py install
    
(Eventually the package will be pushed to our pip repo, and won't require GitLab access.)

Usage
-------------

In order to use the nice IO names, simply import `pyduino-includes` in your SNAPpy script like this:

```python
from PyduinoIncludes import *
    
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

