#solenero.tech@gmail.com
#solenerotech.wordpress.com

#solenerotech 2013.09.06

from motor import motor

mymotor1 = motor('m1', 17, simulation=False)
#where 17 is  GPIO17 = pin 11

mymotor2 = motor('m2', 21, simulation=False)
#where 21 is  GPIO17 = pin 13

mymotor3 = motor('m3', 22, simulation=False)
#where 22 is  GPIO17 = pin 15

mymotor4 = motor('m4', 23, simulation=False)
#where 23 is  GPIO17 = pin 16

Motorlist=[mymotor1,mymotor2,mymotor3,mymotor4]   

print('***Disconnect ESC power')
print('***then press ENTER')

res = input()
for mymotor in Motorlist:
	mymotor.start()
	mymotor.setW(100)

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
print ('increase > a | decrease > z | save Wh > n | set Wh > h|quit > 9')

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
		if res == '9':
            		cycling = False
finally:
    	# shut down cleanly
	for mymotor in Motorlist:
		mymotor.stop()
	print ("well done!")


