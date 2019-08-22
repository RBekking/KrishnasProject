#V1.1. Moves 2 steppers anti-clockwise by specified number of degrees. No reference position.
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS_A = [11,13,15,16]
PINS_B = [19,21,23,24]

for pin in PINS_A:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

for pin in PINS_B:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

#sequence is anti-clockwise.
seq_A = [ [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]   ]

seq_B = seq_A[::-1]


try:
    while True:
        degrees = input('How many degrees?: ')
        steps = (float(512)/360)*degrees
        print "Degrees entered"
        print degrees
        print "Number of steps" 
        print steps
        if steps < 0:    
            for i in range(int(steps)):
                for halfstep in range(8):
                    for pin in range(4):
                        (GPIO.output(PINS_A[pin], seq_A[halfstep][pin])),(GPIO.output(PINS_B[pin], seq_A[halfstep][pin]))
                    time.sleep(0.001) #Change this time to slow down.
        else:
            for i in range(int(steps * -1)):
                for halfstep in range(8):
                    for pin in range(4):
                        (GPIO.output(PINS_A[pin], seq_B[halfstep][pin])),(GPIO.output(PINS_B[pin], seq_B[halfstep][pin]))
                    time.sleep(0.001) #Change this time to slow down.
                

except KeyboardInterrupt:
    GPIO.cleanup()
