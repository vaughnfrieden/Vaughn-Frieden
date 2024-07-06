import socket
import random
from time import sleep 

HEADER = 64
TAG = 10
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.15"
ADDR = (SERVER, PORT)

text = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    text = input("> ")
    if text == "!exit":
        send(DISCONNECT_MESSAGE)
        client.close()
    elif text != "!exit": 
        send(text)
