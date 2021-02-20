print("Do you want to play Rock Paper Scissors game ?")
abc = input("Yes or No (Y/n):")
abc = abc.capitalize()
if(abc == 'Y'):
    pass
else:
    exit()


import random
comp = ''
rand_num = random.randint(1,3)
if(rand_num==1):
    comp = 'r'

elif(rand_num==2):
    comp = 's'
elif(rand_num==3):
    comp = 'p'

print("Computer : ",comp)

player = input("Your turn \n R = Rock\t P=Paper\t S=scissors ?\n")

def gameWin(comp,player):
    if(comp=='r'):
        if(player=='p'):
            return True
        if(player=='s'):
            return False

    if(comp=='p'):
        if(player=='r'):
            return False
        if(player==s):
            return True

    if(comp=='s'):
        if(player=='r'):
            return True
        if(player=='p'):
            return False

if(gameWin(comp,player)):
    print("You Win")
elif(gameWin(comp,player)==False):
    print("You loose")
else:
    print('Draw')