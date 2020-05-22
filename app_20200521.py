from tkinter import *
from PIL import ImageTk, Image
import random

# user clicks button
    # gives user choice
        # button sets the userChoice var to respectity choice 
    # starts the play function 
# code randomly choices a element and sets computerChoice to it
# logic of what beasts what
# display result screen





######################## Global Variables ########################

usersChoice = ''
computerChoice = ''
choices = ['rock', 'paper', 'scissors']


######################## Functions ########################


def playGame():
    
    computerTurn()
    rockLogic()


### get user input ###

def userRock():
    global usersChoice
    usersChoice = 'rock'

    playGame()

def userPaper():
    global usersChoice
    usersChoice = 'paper'

    playGame()

def userScissors():
    global usersChoice
    usersChoice = 'scissors'

    playGame()




def computerTurn():
    global computerChoice
    computerChoice = random.choice(choices)

    



def rockLogic():
    global resultLabel
    # tie
    if computerChoice == usersChoice:
        resultLabel.config(text='tie')


    elif computerChoice in ['rock', 'paper'] and usersChoice in ['rock', 'paper']:
        if computerChoice == 'paper':            
            resultLabel.config(text='Bot wins')
        else:
            resultLabel.config(text='You win')

    elif computerChoice in ['rock', 'scissors'] and usersChoice in ['rock', 'scissors']:
        if computerChoice == 'rock':
            resultLabel.config(text='Bot wins')
        else:
            resultLabel.config(text='You win')
        
    elif computerChoice in ['paper', 'scissors'] and usersChoice in ['paper', 'scissors']:
        if computerChoice == 'scissors':
            resultLabel.config(text='Bot wins')
        else:
            resultLabel.config(text='You win')
    
    
    choicesLabel.config(text = 'Bot: ' + computerChoice + ' VS. You: ' + usersChoice)









######################## GUI | Display Elements ########################

######################## Containers ########################

root = Tk()
root.title('Rock Paper Scissors')
# set width x height
root.geometry('800x600')


topContainer = Frame(root)
topContainer.pack()


bottomContainer = Frame(root)
bottomContainer.pack(side=BOTTOM)


######################## Label ########################

titleLabel = Label(master=topContainer, text='Rock Paper Scissors', font=('Times New Roman', 32))
titleLabel.pack()


resultLabel = Label(master=topContainer, text='', font=('Times New Roman', 28))
resultLabel.pack(pady=40)

choicesLabel = Label(topContainer, text = '', font=('Times New Roman', 18))
choicesLabel.pack(pady=10)


promptLabel = Label(master=topContainer, text='What is your choice?', font=('Times New Roman', 18))
promptLabel.pack()


######################## Images ########################

rock = Image.open('rock.png')
rock = rock.resize((200, 200))
rock = ImageTk.PhotoImage(rock)

paper = Image.open('paper.png')
paper = paper.resize((200, 200))
paper = ImageTk.PhotoImage(paper)

scissors = Image.open('scissors.png')
scissors = scissors.resize((200, 200))
scissors = ImageTk.PhotoImage(scissors)



######################## Buttons ########################


rockButton = Button(master=bottomContainer, image=rock, command = userRock)
rockButton.pack(side=LEFT)

paperButton = Button(master=bottomContainer, image=paper, command=userPaper)
paperButton.pack(side=LEFT)

scissorButton = Button(master=bottomContainer, image=scissors, command=userScissors)
scissorButton.pack(side=LEFT)



root.mainloop()