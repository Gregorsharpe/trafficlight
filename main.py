#!/usr/bin/env python3

from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import os, sys, time, json

# Grab constants from .env file
load_dotenv()

#----------------------------------[ Callbacks ]----------------------------------#

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT server.")
        client.subscribe(os.getenv('MQTT_COMMAND_TOPIC'))
    else:
        print("Unexpected MQTT connection code {}!".format(rc))

# Callback for recieving a command message.
def on_message(client, userdata, msg):
  message = json.loads(msg.payload)
  print(message)

#----------------------------------[ Main Loop ]----------------------------------#

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
  client.connect_async(os.getenv('MQTT_SERVER_ADDRESS'), int(os.getenv('MQTT_SERVER_PORT')), 60)
  client.loop_forever()
except KeyboardInterrupt:
  print("\nInterrupted, exiting gracefully.")
  