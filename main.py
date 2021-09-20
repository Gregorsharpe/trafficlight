#!/usr/bin/env python3
import os, sys, json
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import unicornhat

# Helper module contains all supported "actions" to be displayed.
from actions import getSupportedActions

#------------------------------------[ Init ]-------------------------------------#
load_dotenv()
supportedActions = getSupportedActions()
unicornhat.set_layout(unicornhat.AUTO)
unicornhat.rotation(270)
unicornhat.brightness(0.25)
width, height = unicornhat.get_shape()

#----------------------------------[ Callbacks ]----------------------------------#

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT server.")
        client.subscribe(os.getenv('MQTT_COMMAND_TOPIC'))
    else:
        sys.exit("Unexpected MQTT connection code {}!".format(rc))

# Callback for recieving a command message.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    action = payload["action"].lower()
    if action in supportedActions:
        supportedActions[action]()
        print(F"Executed \"{action}\".")
    else:
        print(F"Got unknown instruction: \"{payload}\"")

#----------------------------------[ Main Loop ]----------------------------------#

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print(F"{width} x {height} grid detected!")
print(F"Loaded {len(supportedActions)} supported actions.")

try:
    client.connect_async(os.getenv('MQTT_SERVER_ADDRESS'), int(os.getenv('MQTT_SERVER_PORT')), 60)
    client.loop_forever()
except KeyboardInterrupt:
    print("\nInterrupted, exiting gracefully.")

