import socket
from player import *
import random

class Game:
    def __init__(self, count_player, n, m):
        self.players = []
        self.count_player = count_player
        self.n = n
        self.m = m

    def start_server(self):
        new_socket = socket.socket()
        port = 8080
        new_socket.bind(("localhost", port))
        new_socket.listen(self.count_player)

        for i in range(self.count_player):
            conn, add = new_socket.accept()
            client_name = (conn.recv(1024)).decode()
            print(f'Присоединился новый игрок: {client_name}')
            player = Player(client_name, conn)
            player.send_message(f'{self.n} {self.m}')
            self.players.append(player)


    def lucky_player(self):
        p = random.choice(self.players)
        return p


    def start_game(self):
        loser = None
        while self.n > 0:
            lucky = self.lucky_player()
            for p in self.players:
                if p == lucky:
                    p.send_message('Вы счастливчик, можете положить часть палок на стол')
                    p.send_message(f'{self.n}')
                    count_items = int(p.receive())
                    self.n += count_items
                else:
                    p.send_message("Ваш ход")
                    p.send_message(f'{self.n}')
                    count_items = int(p.receive())
                    self.n -= count_items
                    print(f'Игрок: {p.name} взял {count_items} предметов. Осталось {self.n}')
                if self.n == 0:
                    loser = p
                    break
        for p in self.players:
            p.send_message('Конец игры')
            if p != loser:
                p.send_message(f'Проиграл {loser.name}')
            else:
                p.send_message('Вы проиграли')
