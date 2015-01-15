__author__ = 'gong'
import netifaces as ni
import datetime



def GetIP(iface):
    ip = ni.ifaddresses(iface)[2][0]['addr']
    netmask = ni.ifaddresses(iface)[2][0]['netmask']
    #print(type(ip))
    return ip, netmask

# ifaces=ni.interfaces()
# print(ifaces)
# print(ni.ifaddresses('wlan0'))
# print("\n")
# print("ifaddresses",ni.ifaddresses('{57F9C543-6ADB-4BCB-8FFB-A707C9CB9969}'))
# print("\n")

# print(GetIP('wlan0'))
# print(GetIP('{D429C1A9-0E61-416E-9313-25E4072338EB}'))

def scan():
    """
    scan ips, return interface, ip, netmask as list
    """
    ifaces=ni.interfaces()
    available = []
    now = datetime.datetime.now()
    for interface in ifaces:
    #     ip = GetIP(interface)
    #     available.append((interface, ip))
        try:
            ip, netmask = GetIP(interface)
            available.append((interface, ip, netmask, now))
        except KeyError :
            pass
    return available

if __name__ == "__main__":
    for interface, ip, netmask in scan():
        print("%s %s \t %s" % (interface,ip,netmask))

