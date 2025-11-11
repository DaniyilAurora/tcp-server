import socket
import sys

HEADER = 64
PORT = 5050
SERVER = "192.168.10.143"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

DISCONNECT_MSG = "!disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

inp = input("Write your message: ")
while inp != "-1":
    send(inp)
    inp = input("Write your message: ")

send("!disconnect")
