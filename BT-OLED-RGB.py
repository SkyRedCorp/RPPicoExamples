#Nova Labs, Bluetooth USB control
#May 2021

#Importing Libraries
#OS required
import time
import board
import busio
import digitalio
#OLED Required
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

#OLED display is controlled by SSD1306
#I2C Config
displayio.release_displays()
i2c_oled = busio.I2C(scl=board.GP19, sda=board.GP18)
display_bus = displayio.I2CDisplay(i2c_oled, device_address=0x3C)
#SSD1306 Config
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

#It's been arranged a RGB led, for indication
#GPIO Setup
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
    text_group = displayio.Group()
    
    if data is not None:
        led.value = True
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")
        led.value = False
        
        if data_string == "G":
            text = "Green"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_green.value = True
            time.sleep(0.5)
            led_green.value = False
            
        elif data_string == "B":
            text = "Blue"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_blue.value = True
            time.sleep(0.5)
            led_blue.value = False
        
        elif data_string == "R":
            text = "Red"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_red.value = True
            time.sleep(0.5)
            led_red.value = False
            
        elif data_string == "Y":
            text = "Yellow"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_red.value = True
            led_green.value = True
            time.sleep(0.5)
            led_red.value = False
            led_green.value = False
        
        elif data_string == "P":
            text = "Pink"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_red.value = True
            led_blue.value = True
            time.sleep(0.5)
            led_red.value = False
            led_blue.value = False
            
        elif data_string == "A":
            text = "Aqua"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_green.value = True
            led_blue.value = True
            time.sleep(0.5)
            led_green.value = False
            led_blue.value = False
        
        elif data_string == "W":
            text = "White"
            text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=5)
            text_group.append(text_area)
            led_red.value = True
            led_blue.value = True
            led_green.value = True
            time.sleep(0.5)
            led_red.value = False
            led_green.value = False
            led_blue.value = False
            
        display.show(text_group)
        time.sleep(0.5)
    
