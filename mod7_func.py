# Motor code modified from:
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
import RPi.GPIO as GPIO             
GPIO.setmode(GPIO.BOARD)

def motor_init (in1, in2, en, freq, dutycycle):
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    pwm_pin=GPIO.PWM(en,freq)
    pwm_pin.start(dutycycle)
    return pwm_pin

def motor_message():
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high ")
    print("c- change to floating point duty cycle with user input")
    print("e-exit")
    print("\n")     

def motor_control (x, in1, in2, pwm_pin):
    if x=='r':
        #print("run")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        #print("forward")
        x='z'

    elif x=='s':
        #print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f':
        #print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='b':
        #print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        x='z'

    elif x=='l':
        #print("low")
        pwm_pin.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        #print("medium")
        pwm_pin.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        #print("high")
        pwm_pin.ChangeDutyCycle(75)
        x='z'
    
    elif x=='c':
        newPWM = float (input("Enter a new PWM duty cycle 0-100: "))
        # Caution NO sanity check here
        pwm_pin.ChangeDutyCycle(newPWM)
        x = 'z'
     
    elif x=='e':
        print ("Stopping")
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        x = 'z'

def movingAvg(arr, numvals, size, position):
    sumvals = 0
    for i in range(numvals):
        if (position - i >= 0):
            sumvals = sumvals + arr[position - i]
        else:
            sumvals = sumvals + arr[size + (position - i)]
    return sumvals/numvals
