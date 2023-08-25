import paho.mqtt.client as mqtt
import time
import random
from mqtt_init import *



def on_log(client, userdata, level, buf):
        print("log: "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
def on_disconnect(client, userdata, flags, rc=0):
        print("DisConnected result code "+str(rc))
def on_message(client,userdata,msg):
        topic=msg.topic
        m_decode=str(msg.payload.decode("utf-8","ignore"))
        print("Message Topic: ", topic)
        print("message received: ", m_decode)


r=random.randrange(1,10000) # for creating unique client ID
clientname="IOT_test-"+str(r)
client = mqtt.Client(clientname, clean_session=True) # create new client instance

client.on_connect=on_connect  #bind call back function
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message
client.username_pw_set(username,password)


print("Connecting to broker ",broker_ip)
client.connect(broker_ip,int(broker_port))     #connect to broker

running_time=60
sub_topic= 'IOT/Smart_Water_Heater/Temperture/sts'
pub_topic= 'pr/home/5216/sts'

client.loop_start()  #Start loop
### part for your change
client.subscribe(sub_topic,qos=0)
#client.publish(pub_topic,"turn on command")
##
time.sleep(running_time)
client.loop_stop()    #Stop loop 
client.disconnect()