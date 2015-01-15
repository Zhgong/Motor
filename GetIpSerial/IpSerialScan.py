__author__ = 'gong'
import GetIP
import serialScan
import datetime
import time
import subprocess as sp
import platform
from simpleconfigparser import simpleconfigparser


def scan():
    global ips
    global serialports
    ips = GetIP.scan()
    serialports = serialScan.scan()

def readConfig():
    global WaitTime
    config = simpleconfigparser()
    config.read('config.ini')
    WaitTime = float(config.setting.WaitTime)
    # print(config.setting.WaitTime)

def printing():
    now = datetime.datetime.now()
    print("Computer name:%s \n Refreshing every %s s, \t%s \n"%(name,WaitTime,now))
    print("####################")
    print("Network interfaces:")
    print("####################")
    for interface,ip, netmask,timeStamp in ips:
        print("%s %s \t %s " % (interface,ip,netmask,))
    print("\n")
    print("#############")
    print("Serial ports:")
    print("#############")
    for n,s,bdrate,timeStamp in serialports:
        print("(%d) %s baudrate: %s " % (n,s,bdrate))

if __name__ == "__main__":
    name = platform.node()
    readConfig()
    while True:
        scan()
        sp.call('cls',shell=True)
        printing()
        time.sleep(WaitTime)