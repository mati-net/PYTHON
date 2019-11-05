###########################
###########################
### ROLLING DICE SCRIPT ###
###########################
###########################

#/#/#/#/
# INIT #

from random import randrange
d_min = 0
d_max = 0
dice = 0

#/#/#/#/#/#/#
# FUNCTIONS #

def max_min():
    max=0
    min=0
    num_ok=False
    while not num_ok :
        try:
            min = int(input('Please set de min number: '))
            if min < 98 :
                num_ok=True
        except ValueError:
            print('>> Must be a integer <<')
            continue
    num_ok=False
    while not num_ok :
        try:
            max = int(input('Please set de max number: '))
            if min < max < 99:
                num_ok=True
        except ValueError:
            print('>> Must be a integer <<')
            continue
    return min,max

def ask_yn(p):
    play = {
    'y':True,
    'Y':True,
    'n':False,
    'N':False,
    }
    return play.get(p,False)


#/#/#/#/#/#/#/#/#
# ROLLING LOGIC #

roll = True
repeat = False

while roll :
    while not repeat :
        d_min,d_max = max_min()
        repeat = True
    dice = randrange(d_min,d_max)
    print('>> Rolling dice ... <<')
    print('\n')
    print('Your dice shows: ',dice)
    roll = ask_yn(input('Want to roll again? (y-Y,n-N)'))
    if roll :
        repeat = ask_yn(input('Do you repeat min and max? (y-Y,n-N)'))

print('>> Thanks for rolling dices <<')
