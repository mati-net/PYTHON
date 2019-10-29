####################
## WAR CARD GAME
####################

import random

#####################
## CARDS DEFINITION 

SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'.split()

#####################
## CLASS DEFINITION

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
        print('Se ha barajado el mazo')


    def split_deck(self):
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


################
## GAME PLAY 

input('Bienvenido a la GUERRA, presiona enter y empecemos ...')

# Defino mi maso como Deck
mydeck=Deck()

# Creo un nuevo maso aleatorio
mydeck.create()

# Divido el maso 2
mydeck.split_deck()
print()

# Le asigno a cada jugador una mitad del mazo aleatorio
player_1=Player(mydeck.hdeck1,[])
player_2=Player(mydeck.hdeck2,[])

# El juego esta ON
game_on= True

# Mientras que todavia el juego esta ON, se juega una mano.
# Al final se verifican la cantidad de cartas.
while game_on:
    input('Presiona enter para Jugar una mano')
    
    # Se inicializa el stack de guerra y se define la mano.
    war_stack=[]
    hand=Hand()
    
    # Se juega una mano
    hand.play(player_1.deck,player_2.deck)
    print('El Jugador 1 ha jugado: ',hand.p1)
    print('El jugador 2 ha jugado: ',hand.p2)

    # Si hay igualdad en el valor de las cartas, hay Guerra.
    if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]): 
        war = True
        while war :
            print('Las cartas tienen el mismo valor!')
            print('GUERRA!')

            if len(player_1.deck) == len(player_2.deck) >= 3:
                hand.war(war_stack,player_1.deck,player_2.deck)
            elif 1 < len(player_1.deck) == len(player_2.deck) < 3 :
                war_stack.append(hand.p1.pop())
                war_stack.append(hand.p2.pop())
                print('No hay suficientes cartas para jugar una guerra normal')
                print('Se descartara solo una carta')
                war_stack.append(p1_deck.pop())
                war_stack.append(p2_deck.pop())
            elif len(player_1.deck) == len(player_2.deck) == 1 :
                print('No hay suficientes cartas para jugar una guerra normal!')
                print('Solo les queda 1 carta a cada uno!')
                print('No se descartan cartas, se juega solo la siguiente')
                war_stack.append(hand.p1)
                war_stack.append(hand.p2)

            input('Presiona enter para Jugar')
            hand.play(player_1.deck,player_2.deck)
            print('El Jugador 1 ha jugado: ',hand.p1)
            print('El Jugador 2 ha jugado: ',hand.p2)

            if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]):
                print('Las cartas tienen el mismo valor de nuevo!')
                print('OMG')
                print('GUERRA!')
                input('Presiona enter para Jugar')
            else:
                war= False

            if len(player_1.deck) == len(player_2.deck) == 0 and  war:
                print('Ya no se puede jugar por falta de cartas!')
                print('Se descarta el stack de ',len(war_stack),' cartas')
                break

    # Si no existe guerra verifico quien gano la mano
    if RANKS.index(hand.p1[:-1]) > RANKS.index(hand.p2[:-1]):
        print('GANO JUGADOR 1')
        player_1.stack.extend(war_stack)
        player_1.stack.append(hand.p1)
        player_1.stack.append(hand.p2)
    elif RANKS.index(hand.p1[:-1]) < RANKS.index(hand.p2[:-1]):
        print('GANO JUGADOR 2')
        player_2.stack.extend(war_stack)
        player_2.stack.append(hand.p1)
        player_2.stack.append(hand.p2)

    if len(player_1.deck) == len(player_2.deck) == 0:
        game_on=False
        print()
        print('SE HAN TERMINADO LAS CARTAS!')
        print('EL JUEGO HA TERMINADO')
        print()

##########################
## FINALIZACION DE JUEGO

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
