__author__ = 'gongzhou'


#!/usr/bin/python

import smbus
import math

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

# convert two-compliment to real number
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

print("gyro data")
print("---------")

GYRO_XOUT_REG=0x43 # 0x43,0x44 high and low byte of X gyro data of register
GYRO_YOUT_REG=0x45 # 0x45,0x46 high and low byte of Y gyro data of register
GYRO_ZOUT_REG=0x47 # 0x47,0x48 high and low byte of z gyro data of register

gyro_xout = read_word_2c(GYRO_XOUT_REG) # interger data of gyro
gyro_yout = read_word_2c(GYRO_YOUT_REG)
gyro_zout = read_word_2c(GYRO_ZOUT_REG)

gyro_xout_scaled = gyro_xout / 131 # 131 corresponds 1 degree/s
gyro_yout_scaled = gyro_yout / 131
gyro_zout_scaled = gyro_zout / 131

print("gyro_xout: {0}, \t scaled: {1} degree/s".format(gyro_xout, gyro_xout_scaled))
print("gyro_yout: {0}, \t scaled: {1} degree/s".format(gyro_yout, gyro_yout_scaled))
print("gyro_zout: {0}, \t scaled: {1} degree/s".format(gyro_zout, gyro_zout_scaled))

print("\n")
print("accelerometer data")
print("------------------")

ACCEL_XOUT_REG = 0x3b # 0x3b,0x3c high and low byte of X acceleration data of register
ACCEL_YOUT_REG = 0x3d # 0x3d,0x3e high and low byte of X acceleration data of register
ACCEL_ZOUT_REG = 0x3f # 0x3f,0x40 high and low byte of X acceleration data of register

accel_xout = read_word_2c(ACCEL_XOUT_REG)
accel_yout = read_word_2c(ACCEL_YOUT_REG)
accel_zout = read_word_2c(ACCEL_ZOUT_REG)

accel_xout_scaled = accel_xout / 16384.0 # 16384 corresponds 1 g
accel_yout_scaled = accel_yout / 16384.0
accel_zout_scaled = accel_zout / 16384.0

print("accel_xout: {0} \t scaled: {1} g".format(accel_xout, accel_xout_scaled))
print("accel_yout: {0} \t scaled: {1} g".format(accel_yout, accel_yout_scaled))
print("accel_zout: {0} \t scaled: {1} g".format(accel_zout, accel_zout_scaled))

print("x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
print("y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))


TEMP_OUT_REG = 0x41  # 0x41,0x42 high and low byte of X acceleration data of register
temp_out = read_word_2c(TEMP_OUT_REG) # integer data of temperature
temp_out_scaled = temp_out/340.0 + 36.53 # according manual
print("\n")
print("temperature")
print("-------")
print("temp_out: {0}, \t sccaled: {1} C".format(temp_out, temp_out_scaled))