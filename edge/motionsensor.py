import utime
import machine

from machine import Pin
from machine import I2C  
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#configure the lcd screen
I2C_ADDR = 0x3F  
I2C_NUM_ROWS = 2 
I2C_NUM_COLS = 16 
i2c = I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=40000) 
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#variables to keep track of distance first iteration and to check diffs in distance
iterator = 0 
distance = 0
distance_diff = 0;
#function to display distance measured
def display_cm(row1,row2):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(row1))
    lcd.move_to(7,0)
    lcd.putstr(row2)
    utime.sleep(0)
#function to display that motion is detected
def display_motion(row1, row2):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(row1)
    lcd.move_to(0,1)
    lcd.putstr(row2)
    utime.sleep(0)
#trigger object and echo object intialized on the ultrasonic sensor
trigger = Pin(3,Pin.OUT) 
echo  = Pin(2,Pin.IN)
#led object and alarm object initalized 
led = machine.Pin(15, machine.Pin.OUT)
alarm = machine.Pin(14,machine.Pin.OUT)
'''function to run the ultrasonic sensor and to measure the distance,
   if distance is chaing rapidly(motion detected) the sensor will activate alarm(led, alarm sound and print to screen)
   otherwise it will display the distance measured '''
def ultra():
    
    global iterator
    global distance 
    global distance_diff 
    trigger.low()
    utime.sleep_us(1)
    trigger.high()
    utime.sleep_us(1)
    trigger.low()
    while echo.value() == 0:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff 
    if iterator == 0 :
        distance = (timepassed * 0.0343) / 2
        distance_diff = distance    
        display_cm(distance,"CM")
        iterator += 1
    if iterator > 0 : 
        distance = (timepassed * 0.0343) / 2
        if (distance - distance_diff) > 2:
            display_motion("Motion detected", "activate alarm")
            led.high()
            alarm.high()
        else:
            distance_diff = distance
            display_cm(distance,"CM")
            led.low() 
            alarm.low()

#loop to run the ultrasonic sensor.
while True:
    ultra()
    utime.sleep(1)





k
