#!/usr/bin/env python3   #this is the location the file came from 

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #this shows the "greetings!" dialogue
colors = ['red','orange','yellow','green','blue','violet','purple'] #these are the correct color options you can use to answer the question
play_again = '' #since there is nothing in the quotes you restart the game by following the rules listed for line 13.
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #when you input n or no, the game ends. if you input a COLOR, the game restarts.
    match_color = random.choice(colors) #this means that the answer can change and be ANY of the colors listed above and is randomized.
    count = 0 #your start count is 0
    color = '' #this is the random selected color
    while (color != match_color): #this essentially says the answer is whatever random color choice the computer made
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line #includes the dialogue in quotes.
        color = color.lower().strip() #this omits errors due to capitalization or spacing
        count += 1 #you gain a point if you are correct
        if (color == match_color): #this states that if your color matches one of the correct answer options, the next line will happen
            print('Correct!') #this shows the dialogue "correct" when you choose a correct answer
        else: #this is essentially "if you type something else"
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #this shows the dialogue in quotes when your answer is incorrect and tells you the number of answers you input {}
    print('\nYou guessed it in {0} tries!'.format(count)) #this line shows the message when you get the correct answer and shows how many tries it took.
    if (count < best_count): #this line tells the line below it that the following message should appear if your score was better than the number of times you guessed incorrectly per round.
        print('This was your best guess so far!') #this line works with the line above to tell you if you did better if you played a second time.
        best_count = count #this line tells the next line that if your best count is the same, the following dialogue will appear.
    play_again = input("\nWould you like to play again? ").lower().strip() #this creates a dialogue to ask if you want to play again
print('Thanks for playing!') #this is the dialogue that appears when you do not replay