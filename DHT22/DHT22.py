import subprocess
import datetime
import logging
import time
import os

def dht22():
    '''read raw data from DHT22 sensor'''
    p = subprocess.Popen("sudo loldht", stdout=subprocess.PIPE, shell=True)
    #print("reading DHT22 sensor ...")
    (output, err) = p.communicate() # output is with bytes format
    #print("reading finished")
    sOutput=output.decode('utf-8') # convert bytes to string
    return sOutput,err

def Humd_Temp(sOutput):
    '''sort the humidity and temperatur from raw data'''
    ls=sOutput.split() # split strings
    #print(ls)
    posHumd=ls.index("Humidity")+2
    posTemp=posHumd + 4

    Humidity=ls[posHumd]
    Temperature=ls[posTemp]
    return Humidity,Temperature

def Humid_Temp_msg():
    # get humidity and temperatur raw data
    rawData,err = dht22()
    # extract humidity and temperatur values
    Humidity, Temperature = Humd_Temp(rawData)
    # time stamp
    TimeStamp=datetime.datetime.now()
    Temp_info='Humidity: {0} %, Temperature: {1} C'.format(Humidity, Temperature)
	
    print('{0}: Humidity: {1} %, Temperature: {2} C'.format(TimeStamp, Humidity, Temperature))
    return Temp_info


def Log_Humid_Temp(LogFile,msg):
    
    # log information
    # logging format:
    # 2014-12-21 17:37:07,717 Humidity: 46.00, Temperatur 20.40 C
    logging.basicConfig(filename=LogFile,level=logging.DEBUG,format='%(asctime)s %(message)s')
    logging.info(msg)
    
LOG_FILE='/home/pi/git/DHT22/DHT22.log'
T_SLEEP=300 # sleep 300 seconds (5 min)

while True:
    Temp_msg=Humid_Temp_msg()
    Log_Humid_Temp(LOG_FILE,Temp_msg)
    time.sleep(T_SLEEP)




