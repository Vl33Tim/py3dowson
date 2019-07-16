#flip the coin
import random
count = 0
head = 0
tails = 0
while count != 100 :
    flip_coin = random.choice([True,False])
    if flip_coin == True:
        head  += 1
        count += 1
    elif flip_coin == False:
        tails += 1
        count += 1
    else: print('Something went wrong!')
input('Coin have fliped head {0} times and tails {1} times.'.format(head, tails))
