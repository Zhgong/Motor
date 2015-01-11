import netifaces as ni

def getip(iface):
    ip = ni.ifaddresses(iface)[2][0]['addr']
    # print(type(ip))
    return ip  

print("\nthis is new")
print(getip('wlan0'))

