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

    computerChoice = 'rock'


    # test
    computerLabel = Label(master=topContainer, text= 'comp: ' + computerChoice, font=('Times New Roman', 24))
    computerLabel.pack()


def rockLogic():

    # tie
    if computerChoice == usersChoice:
        resultLabel = Label(master=topContainer, text= 'Tie', font=('Times New Roman', 24))
        resultLabel.pack()

    elif computerChoice in ['rock', 'paper'] and usersChoice in ['rock', 'paper']:
        if computerChoice == 'paper':
            resultLabel = Label(master=topContainer, text= 'Bot wins', font=('Times New Roman', 24))
            resultLabel.pack()
        else:
            resultLabel = Label(master=topContainer, text= 'You wins', font=('Times New Roman', 24))
            resultLabel.pack()

    elif computerChoice in ['rock', 'scissors'] and usersChoice in ['rock', 'scissors']:
        if computerChoice == 'rock':
            resultLabel = Label(master=topContainer, text= 'Bot wins', font=('Times New Roman', 24))
            resultLabel.pack()
        else:
            resultLabel = Label(master=topContainer, text= 'You wins', font=('Times New Roman', 24))
            resultLabel.pack()
        
    elif computerChoice in ['paper', 'scissors'] and usersChoice in ['paper', 'scissors']:
        if computerChoice == 'scissors':
            resultLabel = Label(master=topContainer, text= 'Bot wins', font=('Times New Roman', 24))
            resultLabel.pack()
        else:
            resultLabel = Label(master=topContainer, text= 'You wins', font=('Times New Roman', 24))
            resultLabel.pack()










######################## GUI | Display Elements ########################

######################## Containers ########################

root = Tk()
root.title('Rock Paper Scissors')
# set width x height
root.geometry('1000x700')


bottomContainer = Frame(root)
bottomContainer.pack()


topContainer = Frame(root)
topContainer.pack(side=BOTTOM)


######################## Label ########################

titleLabel = Label(master=topContainer, text='Rock Paper Scissors', font=('Times New Roman', 24))
titleLabel.pack()

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