import paho.mqtt.client as mqttClient
import time
import sys


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print("Message Received is : " + str(message.payload))
    print("Message Received on Topic " + str(message.topic))






Connected = False  # global variable for the state of the connection
client_name="sub" #client name should be unique

broker_address = "127.0.0.1"  # Broker address
port = 1883  # Broker port
user = "admin"  # Connection username
password = "hivemq"  # Connection password


client = mqttClient.Client(client_name)  # create new instance

client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop
#Task1 : Write your code here
client.subscribe(" ")

while Connected != True:  # Wait for connection
    time.sleep(0.1)


try:
    while True:
        time.sleep(2)


except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
