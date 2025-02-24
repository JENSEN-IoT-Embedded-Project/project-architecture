import machine
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
'''Declaring address of the device connected to the pico
   the number of rows the lcd screen has 
   number of colums each row has'''
I2C_ADDR = 0x3F
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
#Creating one i2c object to identifie the sda and scl pin
#Creating a lcd object with the i2c connection and the describiton oof the lcd display
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq = 40000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
def displaylcd(row1, row2):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(row1))
    lcd.move_to(8,1)
    lcd.putstr(row2)

'''Button'''
#Button to reset all variables to its original state.
#initialize button to min 14 with input pin(send to pico)
#machine.Pin.PULL_UP resistor for the butto
button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
button_pressed = False

def resetbutton(pin):
    global button_pressed 
    button_pressed = True
'''ULTRASONIC'''
#create the ultrasonic sensor cod
#Measure the distance and create a object for the distance
trigger = machine.Pin(3, machine.Pin.OUT)
echo = machine.Pin(2, machine.Pin.IN)
def sonicsensor():
    #send out signal start at low go to high start at low
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    #check how the duration of the echo pin not reciving anything
    while echo.value() == 0:
        signalOff = utime.ticks_us()
    while echo.value() == 1:
        signalOn = utime.ticks_us()
#Calculate distance in cm
    timepassed = signalOn - signalOff
    distance_cm = (timepassed * 0.0343) / 2
    return distance_cm

'''Alarm button'''
led = machine.Pin(15,machine.Pin.OUT)
alarm = machine.Pin(14,machine.Pin.OUT)
def alarm():
    #alarm.high()
    led.high()
    utime.sleep(2)
    #alarm.low()
    led.low()
    utime.sleep(2)
'''main program'''
iteration = 0
distance_diff = 0
while True:
    distance_cm = sonicsensor()
    displaylcd(distance_cm, "CM")
    #if the distance is anomalied or changes in the data more than 5 cm 
    # trigger alarm. 
    if iteration == 0 :
        distance_diff =  distance_cm
        iteration += 1
    #trigger the alarm.
    if (distance_diff - distance_cm) >= 3:
        while True: 
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Motion detectet")
            lcd.move_to(0,1)
            lcd.putstr("Alarm activated")
            alarm()
            button.irq(trigger = machine.Pin.IRQ_FALLING, handler = resetbutton)      
            if button_pressed == True:
                iteration = 0
                distance_cm = 0
                button_pressed = False
                break


    utime.sleep(1)



