import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# ====================================
# LEFT SIDE MOTOR DRIVER
# ====================================

LEFT_FORWARD = 17
LEFT_BACKWARD = 18

# ====================================
# RIGHT SIDE MOTOR DRIVER
# ====================================

RIGHT_FORWARD = 22
RIGHT_BACKWARD = 23

# ====================================
# ALL GPIO PINS
# ====================================

pins = [
    LEFT_FORWARD,
    LEFT_BACKWARD,
    RIGHT_FORWARD,
    RIGHT_BACKWARD
]

# ====================================
# GPIO SETUP
# ====================================

for pin in pins:

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# ====================================
# STOP
# ====================================

def stop():

    for pin in pins:
        GPIO.output(pin, False)

# ====================================
# FORWARD
# ====================================

def forward():

    GPIO.output(LEFT_FORWARD, True)
    GPIO.output(LEFT_BACKWARD, False)

    GPIO.output(RIGHT_FORWARD, True)
    GPIO.output(RIGHT_BACKWARD, False)

# ====================================
# BACKWARD
# ====================================

def backward():

    GPIO.output(LEFT_FORWARD, False)
    GPIO.output(LEFT_BACKWARD, True)

    GPIO.output(RIGHT_FORWARD, False)
    GPIO.output(RIGHT_BACKWARD, True)

# ====================================
# LEFT TURN
# ====================================

def left():

    GPIO.output(LEFT_FORWARD, False)
    GPIO.output(LEFT_BACKWARD, True)

    GPIO.output(RIGHT_FORWARD, True)
    GPIO.output(RIGHT_BACKWARD, False)

# ====================================
# RIGHT TURN
# ====================================

def right():

    GPIO.output(LEFT_FORWARD, True)
    GPIO.output(LEFT_BACKWARD, False)

    GPIO.output(RIGHT_FORWARD, False)
    GPIO.output(RIGHT_BACKWARD, True)