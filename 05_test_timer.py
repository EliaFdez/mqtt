from paho.mqtt.client import Client
from multiprocessing import Process, Manager
from time import sleep
import paho.mqtt.publish as publish
import time


def on_message(mqttc, data, msg):
    print(f'MESSAGE:data:{data}, msg.topic:{msg.topic}, payload:{msg.payload}')


def on_log(mqttc, userdata, level, string):
    print('LOG', userdata, level, string)


def main(broker):
    data = {'status': 0}
    mqttc = Client(userdata=data)
    mqttc.enable_logger()