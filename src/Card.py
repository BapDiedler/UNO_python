import random

#the carte is a color and a value
class Card:
    value = None
    color = None

    ##fonction who creat a card
    def initCard():
        Card.value = random.randint(1, 9)
        Card.color = random.randint(1, 4)
    
    ## fonction who return the value
    def getValue():
        return Card.value
    
    ## fonction who return the color
    def getColor():
        return Card.color

    ##fonction who check if two cards are similar ( UNO )
    def equal(carte):
        valColor = Card.color==carte.color
        valValue = Card.value==carte.value
        return valValue or valColor