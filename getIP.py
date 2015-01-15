import netifaces as ni


def getip(iface):
    ip = ni.ifaddresses(iface)[2][0]['addr']
    # print(type(ip))
    return ip  

print("\nthis is new")
# list all interfaces
print(ni.interfaces())
print("wlan0: ", getip('wlan0'))
# print("eth0: ", getip('eth0'))

