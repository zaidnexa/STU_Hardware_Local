import RPi.GPIO as GPIO

def button_callback(channel):
	print("button was pushed!")
	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

GPIO.add_event_detect(40, GPIO.RISING,callback=button_callback)

message=input("Press enter to quit")

GPIO.cleanup()
