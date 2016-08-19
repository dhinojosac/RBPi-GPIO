#RBPi.py
#
# Raspberry Pi B 2 - Gpio 
#
# 2016 Diego O. Hinojosa Cordova
# d.hinojosa.cordova@gmail.com
#

__version__ = 'v0.0.1'

import platform
import os.path
import time
import sys

if platform.platform().find("Linux-4") != -1:
    legacy_id = True
else:
    legacy_id = False

print "legacy_id: {}".format(legacy_id)

# Ger version 
def getVersion():
    return __version__

# Constans
OUT = "out"
IN = "in"
HIGH = 1
LOW = 0

#MAP RPi Pins

# Setup GPIO function
def setup(pin, mode, pull_up_down=0):
    kernel_id = pin
    export(kernel_id)
    direction(kernel_id, mode)

# Expeort pin to use
def export(kernel_id):
    global legacy_id

    iopath = get_gpio_path(kernel_id)
    if not os.path.exists(iopath):
        f = open('/sys/class/gpio/export','w')
        if legacy_id:
            f.write(str(kernel_id))
        print "f_export: {}".format(f)
        else:
            print "Error no Linux"
        pass
    f.close()


# Define direction INPUT or OUTPUT
def direction(kernel_id, direction):
    iopath = get_gpio_path(kernel_id)
    if os.path.exists(iopath):
    f = open(iopath + '/direction','w')
    f.write(direction)
    print "f: {}".format(f)
    f.close

# Set value to pin
def output(pin, value):
    iopath = get_gpio_path(pin)
    if os.path.exists(iopath):
        f = open(iopath + '/value','w')
    f.write(str(value))
    f.close

# Read pin value
def input(pin):
    iopath = get_gpio_path(pin)
    if os.path.exists(iopath):
        f = open(iopath + '/value','r')
    a = f.read()
    f.close()
    return  int(a)

# Get path for manipulate pins
def get_gpio_path(kernel_id):
    global legacy_id
    kernel_id= kernel_id

    if legacy_id:
        iopath="/sys/class/gpio/gpio%d" % (kernel_id)
    elif not legacy_id:
    print "No Raspberry Pi (platform() not Linux)"
    return "ERROR"
        sys.exit()
    print "iopath: {}".format(iopath)
    return  iopath



if __name__ == '__main__':
    setup(22,OUT)    
    output(22,LOW)
    print "Value of pin {} is {} ".format(22,input(22))    
