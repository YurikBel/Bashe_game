import socket
import sys
import time

socket_server = socket.socket()
port = 8080

server_host = 'localhost'
name = input('Enter name: ')

socket_server.connect((server_host, port))
socket_server.send(name.encode())

params_game = socket_server.recv(1024).decode()
n,m = list(map(int, params_game.split()))
print(f'Параметры игры. Кол-во предметов = {n}, за ход можно взять {m} предметов')
print('Ожидайте начала игры')

while True:
    message = (socket_server.recv(1024)).decode()
    print(message)
    if message == 'Конец игры':
        message = (socket_server.recv(1024)).decode()
        print(message)
        break
    n = int((socket_server.recv(1024)).decode())
    print(f'Текущее кол-во предметов = {n}')

    count_items = int(input('Введите кол-во предметов: '))
    socket_server.send(str(count_items).encode())
    print('Ожидайте вашего хода')
