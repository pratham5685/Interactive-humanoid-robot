from flask import Flask, render_template
import motor_control

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():
    return render_template('index.html')

# =========================
# MOVEMENT ROUTES
# =========================

@app.route('/forward')
def forward():

    motor_control.forward()
    return "FORWARD"

@app.route('/backward')
def backward():

    motor_control.backward()
    return "BACKWARD"

@app.route('/left')
def left():

    motor_control.left()
    return "LEFT"

@app.route('/right')
def right():

    motor_control.right()
    return "RIGHT"

@app.route('/stop')
def stop():

    motor_control.stop()
    return "STOP"

# =========================
# RUN SERVER
# =========================

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)