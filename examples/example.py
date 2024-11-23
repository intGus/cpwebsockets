# SPDX-FileCopyrightText: © 2024 Gustavo Diaz <contact@gusdiaz.dev>
#
# SPDX-License-Identifier: MIT

# Websockets client for CircuitPython
# Forked from: https://github.com/danni/uwebsockets

import wifi
import time
import cpwebsockets.client

# Wi-Fi credentials
SSID = "SSID" # Your SSID
PASSWORD = "WiFi Password" # Your Password

def connect_to_wifi():
    print("Connecting to Wi-Fi...")
    try:
        wifi.radio.connect(SSID, PASSWORD)
        print("Connected to Wi-Fi!")
        print(f"IP Address: {wifi.radio.ipv4_address}")
    except Exception as e:
        print("Failed to connect to Wi-Fi:", e)
        raise

def main():
    connect_to_wifi()
    
    # WebSocket connection
    try:
        print("Connecting to WebSocket server...")
        websocket = cpwebsockets.client.connect("wss://ws.postman-echo.com/raw", wifi.radio)
        print("Connected!")
        
        # Send and receive a message
        mesg = "The quick brown fox jumps over the lazy dog"
        websocket.send(mesg + "\r\n")
        resp = websocket.recv()
        print("Received:", resp)
        assert(mesg + "\r\n" == resp)
        
        # Close the WebSocket
        websocket.close()
        print("WebSocket connection closed.")
    except Exception as e:
        print("An error occurred:", e)

# Run the program
main()
