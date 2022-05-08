import time
import board
import busio
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led_red = digitalio.DigitalInOut(board.GP2)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.GP3)
led_green.direction = digitalio.Direction.OUTPUT
led_blue = digitalio.DigitalInOut(board.GP4)
led_blue.direction = digitalio.Direction.OUTPUT

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=9600)

while True:
    data = uart.read(1)
    #print(data)
    
    if data is not None:
        led.value = True
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")
        led.value = False
        
        if data_string == "G":
            led_green.value = True
            time.sleep(0.5)
            led_green.value = False
            #time.sleep(1)
            
        if data_string == "B":
            led_blue.value = True
            time.sleep(0.5)
            led_blue.value = False
            #time.sleep(1)
        
        if data_string == "R":
            led_red.value = True
            time.sleep(0.5)
            led_red.value = False
            #time.sleep(1)
    
        
    
    
    