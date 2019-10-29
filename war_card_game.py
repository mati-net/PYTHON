####################
## WAR CARD GAME
####################

import random

SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the deck Class. This Object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the Deck. It should also
    have a method for splitting/cutting the deck in half and shuffling the deck.
    """
    def __init__(self,suite=SUITE,ranks=RANKS,deck=[],hdeck1=[],hdeck2=[]):
        self.suite = suite
        self.ranks = ranks
        self.deck = deck
        self.hdeck1= hdeck1
        self.hdeck2= hdeck2


    def create(self):
        for i in range(len(self.suite)):
            for n in range(len(self.ranks)):
                self.deck.append(self.ranks[n]+self.suite[i])
        random.shuffle(self.deck)
        print('Se creo un nuevo mazo')


    def split(self):
        self.hdeck1=self.deck[0:26]
        self.hdeck2=self.deck[26:52]
        print('El mazo se a partido en 2')


class Hand():
    """
    This is the Hand class. Each player has a hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def __init__(self,p1=[],p2=[]):
        self.p1 = p1
        self.p2 = p2

    def play(self,p1_deck,p2_deck):
        war=False
        self.p1 = p1_deck.pop()
        self.p2 = p2_deck.pop()
        print('')

    def war(self,war_stack,p1_deck,p2_deck):
        war_stack.append(self.p1)
        war_stack.append(self.p2)
        for i in range(2):
            war_stack.append(p1_deck.pop())
            war_stack.append(p2_deck.pop())
        print('Ambos jugadores han quitado 2 cartas')
        return war_stack

class Player():
    """
    This is the Player class, which takes in a name and an instance of a hand
    class object. The player can then play cards and check if they still have cards.
    """
    def __init__(self,deck,stack):
        self.deck = deck
        self.stack = stack

#    def mod_stack(self,action,value):
#        if action == 'a' :
#            self.stack.append(value)
#        if action == 'e' :
#            self.stack.extend(value)

## GAME PLAY

input('Bienvenido a la GUERRA, presiona enter y empecemos ...')

# Defino mi maso como Deck
mydeck=Deck()

# Creo un nuevo maso aleatorio
mydeck.create()
#print(mydeck.deck)

# Divido el maso 2
mydeck.split()
print()

player_1=Player(mydeck.hdeck1,[])
player_2=Player(mydeck.hdeck2,[])

#print(player_1.deck)
#print(player_2.deck)

game_on= True

while game_on:
    input('Presiona enter para Jugar una mano')
    war_stack=[]
    hand=Hand()
    hand.play(player_1.deck,player_2.deck)
    print('El Jugador 1 ha jugado: ',hand.p1)
    print('El jugador 2 ha jugado: ',hand.p2)

    if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]) and len(player_1.deck) == len(player_2.deck) => 3:
        print('Las cartas tienen el mismo valor!')
        print('GUERRA!')
        input('Presiona enter para Jugar')
        war = True
        while war:
            hand.war(war_stack,player_1.deck,player_2.deck)
            hand.play(player_1.deck,player_2.deck)
            print('El Jugador 1 ha jugado: ',hand.p1)
            print('El Jugador 2 ha jugado: ',hand.p2)
            if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]):
                print('Las cartas tienen el mismo valor de nuevo!')
                print('OMG')
                print('GUERRA!')
            else:
                war= False
            print('el stack de guerra es: ',war_stack)
    elif RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]) and 1 < len(player_1.deck) == len(player_2.deck) < 3 :
        print('No hay suficientes cartas para jugar una guerra normal')
        print('Se descartara solo una carta')
        war_stack.append(hand.p1)
        war_stack.append(hand.p1)
    if RANKS.index(hand.p1[:-1]) > RANKS.index(hand.p2[:-1]):
        print('GANO JUGADOR 1')
        player_1.stack.extend(war_stack)
        player_1.stack.append(hand.p1)
        player_1.stack.append(hand.p2)
    else:
        print('GANO JUGADOR 2')
        player_2.stack.extend(war_stack)
        player_2.stack.append(hand.p1)
        player_2.stack.append(hand.p2)


    #print('Stack jugador 1',player_1.stack)
    #print('Deck jugador 1',player_1.deck)
    #print('Stack jugador 2',player_2.stack)
    #print('Deck jugador 2',player_2.deck)
    if len(player_1.deck) == len(player_2.deck) == 0:
        game_on=False
        print()
        print('SE HAN TERMINADO LAS CARTAS!')
        print('EL JUEGO HA TERMINADO')
        print()

input('Presiona enter para contabilizar las cartas y saber el ganador')
print('El GANADOR ES:')
if len(player_1.stack) > len(player_2.stack):
    print('JUGADOR 1 con ',len(player_1.stack),' cartas')
    print('jugador 2 tenia ',len(player_2.stack),' cartas')
elif len(player_1.stack) < len(player_2.stack):
    print('JUGADOR 2 con ',len(player_2.stack),' cartas')
    print('jugador 1 tenia ',len(player_1.stack),' cartas')
else:
    print('AMBOS JUGADORES TIENEN IGUAL CANTIDAD DE CARTAS!')
    print('ES UN EMPATE!')
