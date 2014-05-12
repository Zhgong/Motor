#
#

#

from motor import motor


def Stopall():
	'''Stop all the motors, with pulswidth 1000 us'''
	for mymotor in Motorlist:
		mymotor.setW(0)

def PowerOffAll():
	'''Power off all the motors'''
	for mymotor in Motorlist:
		mymotor.stop()

Motorlist=[]   

mymotor1 = motor('m1', 17, simulation=False)
Motorlist.append(mymotor1)
#where 17 is  GPIO17 = pin 11
# Front-Right

mymotor2 = motor('m2', 27, simulation=False)
Motorlist.append(mymotor2)
#where 21 is  GPIO27 = pin 13

mymotor3 = motor('m3', 22, simulation=False)
Motorlist.append(mymotor3)
#where 22 is  GPIO22 = pin 15
# Back-Right

mymotor4 = motor('m4', 23, simulation=False)
Motorlist.append(mymotor4)
#where 23 is  GPIO23 = pin 16
# Front-Left


print('***Disconnect ESC power')
print('***then press ENTER')

res = input()
#for mymotor in Motorlist:
#	mymotor.start()
#	mymotor.setW(100)

#NOTE:the angular motor speed W can vary from 0 (min) to 100 (max)
#the scaling to pwm is done inside motor class
print('***Connect ESC Power')
print('***Wait beep-beep')

print('***then press ENTER')
res = input()
for mymotor in Motorlist:
	mymotor.start()
	mymotor.setW(0)
print('***Wait N beep for battery cell')
print('***Wait beeeeeep for ready')
print('***then press ENTER')
res = input()
print ('increase > a | decrease > z | save Wh > n | set Wh > h | Stop all > s | quit > 9')

cycling = True
try:
	while cycling:
		res = input()
		if res == 'a':
			for mymotor in Motorlist:
				mymotor.increaseW()
		if res == 'z':
			for mymotor in Motorlist:
				mymotor.decreaseW()
		if res == 'n':
			for mymotor in Motorlist:
				mymotor.saveWh()
		if res == 'h':
			for mymotor in Motorlist:
				mymotor.setWh()
		if res == 's':
			Stopall()

		if res == '9':
			PowerOffAll()
			cycling = False
finally:
    	# shut down cleanly
	#for mymotor in Motorlist:
	#	mymotor.stop()
	print ("well done!")


