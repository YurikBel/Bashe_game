import socket
from game import *

count_players = int(input('Введите кол-во игроков: '))
N = int(input('Введите кол-во предметов: '))
M = int(input('Введите кол-во предметов за один ход: '))

game = Game(count_players, N, M)
game.start_server()
game.start_game()