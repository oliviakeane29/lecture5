#lottery game
yourguess= int(input('enter your guess:'))

if (yourguess==10) or (yourguess==100):
    print ('you win, with operator')
else:
    print ('you guessed wrong, with operator')

#without using or operator
if (yourguess==10):
    print ('you win, without operator')
elif (yourguess==100):
    print ('you win, without operator')
else:
    print ('you guessed wrong, without operator')