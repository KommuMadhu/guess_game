#taken variable ,list 
print('______GUESS THE NUMBER U THINK______')
number_guess = [1,3,5,10]

for x in (1,4):#given choice for guess 
    guess=int(input('guess the number :) '))#user input
    if guess in number_guess:
        print('you guessed right :) ') # reward
        break # break if he guess the number
    else:
        print('you lost try again :( ')