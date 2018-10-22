#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
import time
#time_stamp = time.time()
#import cv2
def printFunction(channel):
        print("Button 1 pressed!")
        GPIO.output(4,1)
        time.sleep(1)
        GPIO.output(4,0)
        time.sleep(1)
#        print("Note how the bouncetime affects the button press")
GPIO.add_event_detect(21, GPIO.RISING, callback=printFunction, bouncetime=300)
def printFunction12(channel):
        print("Button 3 pressed!")
	GPIO.output(22,1)
        time.sleep(1)
        GPIO.output(22,0)
        time.sleep(1)
#        print("Note how the bouncetime affects the button press")
GPIO.add_event_detect(12, GPIO.RISING, callback=printFunction12, bouncetime=300)
def printFunction16(channel):
        print("Button 2 pressed!")
        GPIO.output(17,1)
        time.sleep(1)
        GPIO.output(17,0)
        time.sleep(1)
#        print("Note how the bouncetime affects the button press")
GPIO.add_event_detect(16, GPIO.RISING, callback=printFunction16, bouncetime=300)
#while True:
#	GPIO.wait_for_edge(16, GPIO.FALLING)
#	print("Button 2 Pressed")
#	GPIO.wait_for_edge(16, GPIO.RISING)
#	print("Button 2 Released")
#        print("Button 2 pressed!")
#	GPIO.output(17,1)
#	time.sleep(1)
#	GPIO.output(17,0)
#	time.sleep(1)
#	except KeyboardInterrupt:
#    	print('interrupted!')
def main():
    while 1:
        print "I'm in main!"
        time.sleep(1)

def stop():
    print "got KeyboardInterrupt, stopping."

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        stop()
GPIO.cleanup()
