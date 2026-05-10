import RPi.GPIO as GPIO

# Motor Pins
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

GPIO.setmode(GPIO.BCM)

pins = [IN1, IN2, IN3, IN4]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

def stop():
    for pin in pins:
        GPIO.output(pin, False)

def forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)

    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)

    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)

    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)

    GPIO.output(IN3, False)
    GPIO.output(IN4, True)