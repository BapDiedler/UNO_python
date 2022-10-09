import Card

class Packet:##the packet is defined by his size and his cards               
        size = 0
        cards = [None]*size
        
        ##fonction who creat a packet of 108 cards
        def initPacket108():
            Packet.size = 108
            for i in range(108):
                Packet.cards[i].Card.initCard()

        ##fonction who creat a packet of 10 cards
        def initPacket7(packet):
            Packet.size = 7
            for i in range(7):
                Packet.cards[i] = packet.cards[i]
                del[packet.cards[i]]