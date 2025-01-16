# SPDX-FileCopyrightText: © 2025 Peter Tacon <contacto@petertacon.com>
#
# SPDX-License-Identifier: MIT

"""HTTP Server"""

# Import OS, Wi-Fi, and HTTPServer libraries
import socketpool
import wifi
import os
import board
import microcontroller
import time
from digitalio import DigitalInOut, Direction

# Random number library
from random import randint

"""Creating objects for required libraries"""
#  Onboard LED and Relay setup
led = DigitalInOut(board.LED)
relay1 = DigitalInOut(board.GP16)
relay2 = DigitalInOut(board.GP17)

led.direction = Direction.OUTPUT
relay1.direction = Direction.OUTPUT
relay2.direction = Direction.OUTPUT

led.value = False
relay1.value = True
relay2.value = True

# Web Server and Socketpool libraries
from adafruit_httpserver import Server, Request, Response, GET, POST, FileResponse, MIMETypes

# Unregistering MIME types (saving memory)
MIMETypes.configure(
    default_to="text/plain",
    # Unregistering unnecessary MIME types can save memory
    keep_for=[".html", ".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".ico"],
)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

# Route default static
document_root = '/www'

@server.route("/")
def base(request: Request):
    return FileResponse(request, filename='relay.html', root_path=document_root)

@server.route("/", POST)
def buttonpress(request: Request):
    raw_text = request.raw_request.decode("utf8")
    #print(raw_text)
    
    if "1ON" in raw_text:
        relay1.value = True
        print("Relay 1 ON")
        
    elif "2ON" in raw_text:
        relay2.value = True
        print("Relay 2 ON")
        
    elif "1OFF" in raw_text:
        relay1.value = False
        print("Relay 1 OFF")
        
    elif "2OFF" in raw_text:
        relay2.value = False
        print("Relay 2 OFF")
        
    else:
        print("Unknown command")
        
    return FileResponse(request, filename='relay.html', root_path=document_root)

server.serve_forever(str(wifi.radio.ipv4_address))