######################
## CODE BRAKER GAME ##
## Nope-Close-Match ##
######################

# INIT
import random

s_num=''
p_num=''
close=False
match=False
win=False

# FUNCTIONS

def get_num():
    num_nok=True
    global p_num
    while num_nok:
        p_num=str(input('What is your guess?'))
        not_int=False
        if len(p_num) != 3:
            print('Number must be 3 digit lenght')
            continue
        for i in range(3):
            if not p_num[i] in str(list(range(10))):
                not_int=True
                break
        if not_int:
            print('You must type 3 integer digit')
            continue
        num_nok=False

def f_close(s_num,p_num):
    global close
    close=False
    for i in list(p_num):
        if i in list(s_num):
            print('CLOSE!')
            close=True
            break


def f_match(s_num,p_num):
    global match
    match=False
    for i in range(3):
        if s_num[i] == p_num[i]:
            print('MATCH!')
            match=True
            break

def f_win(s_num,p_num):
    global win
    if s_num == p_num:
        print('YOU WIN!!')
        win=True

###########
# GAME
##########

# Say Hi!
print('Welcome Code Breaker! Let´s see if you can guess my 3 digit number!')

# Pick a random number
for i in range(3):
    s_num+=str(random.randrange(10))
print(s_num)

# Notify that i have a new code to break
print('Code has been generated, please guess a 3 digit number')

# Ask for number
while not win :
    get_num()
    f_win(s_num,p_num)
    if win :
        continue
    f_match(s_num,p_num)
    if match :
        continue
    f_close(s_num,p_num)
    if close :
        continue
    print('NO LE EMBOCASTE A NADA AMIGO')
