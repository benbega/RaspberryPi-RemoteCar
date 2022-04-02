# Test motor controller script for single motor.
# Proves connection between Raspberry Pis using Remote GPIO via gpiozero
# Increases speed of left motor going forward, then reverses. 

#### Usage
##
#### $ GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=<IP address of Pi to be controlled> python3 MotorController_1.py
##
####
import gpiozero as gp
from time import sleep

lm = gp.Motor(24,23,pwm=True); # Left Motor in1/in2

lmEnable = gp.LED(25); #Bridge enable PIN
lmEnable.on(); #enable left motor

while(True):
    print("front front front")
    for x in range(50, 100):#Incrementally increases speed of left motor, forwards
        lm.forward(x/100);
        sleep(0.1)
        
    for x in range(100, 50):
        #Incrementally decreases speed of left motor to avoid harsh changes in direction
        lm.forward(x/100);
        sleep(0.1)
        
    print("back back back") 
    for y in range(50, 100):#Incrementally increases speed of left motor, backwards
        lm.backward(y/100)
        sleep(0.1)
        
    for y in range(100, 50):
        #Incrementally decreases speed of left motor to avoid harsh changes in direction
        lm.backward(y/100)
        sleep(0.1)
        
gp.close()#cleanly closes GPIO