"""
A simple example that connects to the Adafruit IO MQTT server
and subscribes to a topic, which will signal the onboard LED
to turn ON or OFF
"""

import time
import network
from machine import Pin
from umqtt.simple import MQTTClient
import dht
dataPin = 16
myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
sensor = dht.DHT11(myPin)
# Setup the onboard LED so we can turn it on/off
led = Pin("LED", Pin.OUT)

# Fill in your WiFi network name (ssid) and password here:
wifi_ssid = "ZTE_7VPQPK_2.4G"
wifi_password = "2cT5554hn67"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
mqtt_host = "io.adafruit.com"
mqtt_username = "Ted_1958"  # Your Adafruit IO username
mqtt_password = "aio_EtES27xF1Bi7MCsMEltwZ9Ey82aL"  # Adafruit IO Key
mqtt_receive_topic = "Ted_1958/feeds/led-feed"  # The MQTT topic for your Adafruit IO Feed
#mqtt_publish_topic_temp = "Ted_1958/feeds/dht11-temp"  # The MQTT topic for your Adafruit IO Feed
mqtt_publish_topic_temp ="Ted_1958/feeds/nikolai.temp"
mqtt_publish_topic_hum ="Ted_1958/feeds/nikolai.hum"
# Enter a random ID for this MQTT Client
# It needs to be globally unique across all of Adafruit IO.
mqtt_client_id = "somethingreallyrandomandunique123"

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)


# So that we can respond to messages on an MQTT topic, we need a callback
# function that will handle the messages.
def mqtt_subscription_callback(topic, message):
    # Umwandlung von Byte-Strings in normale Zeichenketten
    topic_str = topic.decode('utf-8')
    message_str = message.decode('utf-8')

    print (f'Topic {topic} received message {message}')  # Debug print out of what was received over MQTT
    if message_str == "on":
        print("LED ON")
        led.value(1)
    elif message_str == "off":
        print("LED OFF")
        led.value(0)

# Before connecting, tell the MQTT client to use the callback
mqtt_client.set_callback(mqtt_subscription_callback)
mqtt_client.connect()

# Once connected, subscribe to the MQTT topic
mqtt_client.subscribe(mqtt_receive_topic)
print("Connected and subscribed")
led.value(1)
counter = 0
while True:
    print(f'counter ={counter}')
    counter += 1
    sensor.measure()
    print(f'checkpoint = 1')
    temp = sensor.temperature()
    print(f'checkpoint = 2')
    hum = sensor.humidity()
    print(f'checkpoint = 3')
    # Daten auf der immer gleichen Zeile darstellen
    # im Print-Befehl "\r", voranstellen, am Ende schreibst Du end=''
    print("Temperatur: {}°C, Luftfeuchtigkeit: {}%".format(temp, hum))
    # Publish the data to the topic!
    try:
        mqtt_client.publish(mqtt_publish_topic_temp, str(temp))
        print("published successfully")
    except Exception as e:
        print(f"Failed to publish temp: {e}")
    try:
        mqtt_client.publish(mqtt_publish_topic_hum, str(hum))
        print("published successfully")
    except Exception as e:
        print(f"Failed to publish hum: {e}")
    
    # Delay a bit to avoid hitting the rate limit
    time.sleep(3)
