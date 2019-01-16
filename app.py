import datetime
import time
import os
import sys

import paho.mqtt.client as mqtt


## Get configuration

fault = False

if 'MQTT_SERVER' not in os.environ.keys():
    print("MQTT_SERVER environment variable missing")
    fault = True
else: 
    server = os.environ['MQTT_SERVER']

if 'MQTT_TOPIC' not in os.environ.keys():
    print("MQTT_TOPIC environment variable missing")
    fault = True
else:
    topic = os.environ['MQTT_TOPIC']

if fault:
    sys.exit(1)


## MQTT connection

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect(server, 1883, 60)

client.loop_start()

while True:
    client.publish(topic, "OK")
    time.sleep(10)

client.loop_stop()
