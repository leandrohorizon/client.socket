import socket
from robot import Robot

bot = Robot(nickname='jargo')

def start():
  print('iniciado')
  HOST = ''
  PORT = 5000
  udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  orig = (HOST, PORT)
  udp.bind(orig)
  while True:
    msg, cliente = udp.recvfrom(1024)
    print(f"leanddro: {msg.decode()}")
    bot.speak(msg.decode())

start()
