import paho.mqtt.client as mqttClient
import time
import ast
import random

def location_generator():
    corr={'x':random.randrange(0,250,1),
          'y':random.randrange(0,250,1)}
    return corr



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed Return Code : ",rc)


Connected = False  # global variable for the state of the connection
client_name="pub"
broker_address = "127.0.0.1"  # Broker address
port = 1883  # Broker port
curr=location_generator()

client = mqttClient.Client(client_name)  # create new instance


client.on_connect = on_connect  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop


while Connected != True:  # Wait for connection
    time.sleep(0.1)


try:
    while True:
        client.publish("location/"+client_name,str(curr))
        time.sleep(2)
        curr=location_generator()

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
