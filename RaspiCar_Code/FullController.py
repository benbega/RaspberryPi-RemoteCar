# Full controller script, including throttle and steering control

import gpiozero as gp
from gpiozero.pins.rpigpio import RPiGPIOFactory
from time import sleep

#Local Pin Variables
localFactory = RPiGPIOFactory() #gets local pin instances

lm = gp.Motor(23,24,pwm=True); # Left Motor in1/in2
rm = gp.Motor(27,22,pwm=True); # Right motor in3/4
servo = gp.Servo(5)

throttle = gp.RotaryEncoder(17, 18, pin_factory=localFactory, max_steps=20, wrap=False)
    # Rotary encoder for throttle. 20 steps for throttle, LOCAL PIN
steer = gp.RotaryEncoder(22, 23, pin_factory=localFactory, max_steps=20, wrap=False)
    # Rotary encoder for throttle. 20 steps for throttle, LOCAL PIN

lmEnable = gp.LED(25); #EnablePin1
rmEnable = gp.LED(13); #EnablePin2
lmEnable.on(); #enable left motor
rmEnable.on(); #enable right motor

try:
    while(True):
        throttleVal = throttle.value*20
        steerVal = steer.value*20
        if(steerVal > 0):
            print("Going right, steer: ", steerVal)
            scaledSteer = ((steerVal)*5)/100
            servo.value = scaledSteer
            print("Scaled steer: ", scaledSteer)
            
        elif(steerVal == 0):
            print("Going straight")
            servo.value = 0
            
        elif(steerVal < 0):
            print("Going left, steer: ", steerVal)
            scaledSteer = ((steerVal)*5)/100
            servo.value = scaledSteer
            print("Scaled steer: ", scaledSteer)
            
            
            
        if(throttleVal > 0):
            #going forward
            lmEnable.on()
            rmEnable.on()
            print("Going forward, throttle: ", throttleVal)
            scaledThrottle = ((throttleVal)*5)/100
            lm.forward(scaledThrottle)
            rm.forward(scaledThrottle)
            print("Scaled throttle: ", scaledThrottle)
            
        elif(throttleVal == 0):
            print("Throttle off - stopping")
            lmEnable.off()
            rmEnable.off()
            
        elif(throttleVal < 0):
            lmEnable.on()
            rmEnable.on()
            print("Going backward, throttle: ", throttleVal)
            scaledThrottle = (abs((throttleVal))*5)/100
            lm.backward(scaledThrottle)
            rm.backward(scaledThrottle)
            print("Scaled throttle: ", scaledThrottle)
            
finally:
    print("closing")