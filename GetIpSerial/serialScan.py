__author__ = 'gong'
import serial
import datetime

def scan():
   # scan for available ports. return a list of tuples (num, name)
   available = []
   now = datetime.datetime.now()
   for i in range(256):
       try:
           s = serial.Serial(i)
           available.append( (i, s.portstr,s.getBaudrate(),now))
           s.close()
       except serial.SerialException:
           pass
   return available

if __name__ == "__main__":
    print("Found ports:")
    for n,s,bdrate,timeStamp in scan():
        print("(%d) %s baudrate: %s \t %s" % (n,s,bdrate,timeStamp))

