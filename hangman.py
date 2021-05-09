import random

def hangman():
    list_of_words=['sagar','sindhu','nirmala','shivaram','ubuntu','cricket','ipl']
    word=random.choice(list_of_words)
    turns=10
    guessmade=""
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        mainword=""

        for letter in word:
            if letter in guessmade:
                mainword=mainword+letter
            else:
                mainword=mainword+'_'

        if(mainword==word):
            print(mainword)
            print('YOU WON!!!')
            break  

        print("Guess the correct letter ",mainword)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print('Enter valid character')
            guess=input()
        
        if guess not in word:
            turns=turns-1
            if(turns==9):
                print('You have {} chances'.format(turns))
                print('----------------------------------')
            elif(turns==8):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
            elif(turns==7):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
                print('              |                  ')
            elif(turns==6):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
                print('              |                  ')
                print('             /                   ')
            elif(turns==5):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
                print('              |                  ')
                print('             / \                 ')   
            elif(turns==4):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
                print('             /|                  ')
                print('             / \                 ')
            elif(turns==3):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o                  ')
                print('             /|\                 ')
                print('             / \                 ')                 
            elif(turns==2):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o-                 ')
                print('             /|\                 ')
                print('             / \                 ')   
            if(turns==1):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('              o---               ')
                print('             /|\                 ')
                print('             / \                 ')   
            elif(turns==0):
                print('You have {} chances'.format(turns))
                print('---------------------------------')
                print('                  |              ')
                print('                  |              ')
                print('              o---               ')
                print('             /|\                 ')
                print('             / \                 ')  
                print(word)
                print("You LOOSE")
                print('You let a Innocent man be hanged!!!!')   
                break              



name=input('Enter Your Name:')
name=name.capitalize()
print('Welcome '+name+"!")
print('Guess the correct word in 10 attempts')

hangman()
