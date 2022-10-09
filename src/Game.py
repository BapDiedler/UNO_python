from telnetlib import GA
import Packet, Player

#the game is defined by a packet his players and a statue
class Game:
    nbPlayers = 0
    end = False
    Players = [Player]*nbPlayers
    packet = Packet

    ##fonction who creat a game
    def initGame(nb):
        Game.nbPlayers = nb
        Game.packet = Packet.initPacket108()
        for i in range(nb):
            Game.Players[i] = Player.initPlayer(Game.packet)