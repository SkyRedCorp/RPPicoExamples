#Nova Labs
#Bad USB project

#OS required libraries
import time
import board

#USB HID Libraries
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

#Feather RP2040 has integrated LED
#LED required libraries
import neopixel

#Random number library
from random import randint

#Creating objects for required libraries
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
pixle = neopixel.NeoPixel(board.NEOPIXEL, 1)

#Arrays for different messages and keystrokes
key_str = ["NO DEBO DEJAR LA PC DESATENDIDA\n", "notepad \n", ":D",
           "cmd\n", "shutdown /r /t 0 /c \"Sorry, not sorry xD\" \n",
           "you have been hacked"]
key_pad = [Keycode.GUI, Keycode.R, Keycode.M, Keycode.UP_ARROW,
           Keycode.ENTER, Keycode.DELETE, Keycode.DOWN_ARROW]

def notepad_open():
    pixle.fill((7,225,25))
    keyboard.send(key_pad[0], key_pad[1])
    time.sleep(0.5)
    layout.write(key_str[1])
    
def randomouse():
    pixle.fill((7,224,208))
    start = time.monotonic()
    while time.monotonic() - start < 20:
        mouse.move(x=randint(-20, 20), y=randint(-20, 20))
        mouse.move(x=randint(-20, 20), y=randint(-20, 20))

def redbutton():
    pixle.fill((255,0,0))
    keyboard.send(key_pad[0], key_pad[1])
    time.sleep(0.1)
    layout.write(key_str[3])
    time.sleep(0.5)
    layout.write(key_str[4])
    
def joketype():
    count = 100
    while count > 0:
        layout.write(key_str[6])
        time.sleep(0.02)
        break
        count -= 1
        
def notepad_max():
    pixle.fill((7,224,225))
    keyboard.send(key_pad[0], key_pad[3])
    
def notepad_min():
    pixle.fill((78,230,12))
    keyboard.send(key_pad[0], key_pad[6])
    
def all_minimize():
    pixle.fill((16,171,227))
    keyboard.send(key_pad[0], key_pad[2])
    
def write_message():
    pixle.fill((255,0,0))
    for i in range(10):
        layout.write(key_str[0])

while True:
    all_minimize()
    time.sleep(1)
    notepad_open()
    time.sleep(1)
    notepad_max()
    time.sleep(1)
    write_message()
    time.sleep(1)
    randomouse()
    time.sleep(10)
    