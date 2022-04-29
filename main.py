from tkinter import *
from poker import *

def rungame():
    number_of_players = int(slider.get())
    slider.destroy()
    button.destroy()
    label.destroy()
    root.geometry('1000x650')
    # initialize and shuffle the deck of cards
    theDeck = Deck()
    theDeck.shuffle()

    # create "number_of_players" Players as "Player" objects in a Player list called "playerList"
    playerList = []
    for i in range(number_of_players):
        tempCard1 = Card(theDeck.deck[i].number, theDeck.deck[i].suit)
        tempCard2 = Card(theDeck.deck[number_of_players + i].number, theDeck.deck[number_of_players + i].suit)
        tempPlayer = Player(tempCard1, tempCard2)
        playerList.append(tempPlayer)

    if number_of_players == 2:
        p1 = Label(root, padx=10, pady=10, borderwidth = 3, relief="sunken", text="player 1: "+ str(playerList[0].card1.__str__()) + ' '+ str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth = 3, relief="sunken", text="player 1: "+ str(playerList[1].card1.__str__()) + ' '+ str(playerList[1].card2.__str__()))
        p2. grid(row=1, column=0)
    if number_of_players == 3:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
    if number_of_players == 4:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
        p4 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 4: " + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
        p4.grid(row=3, column=0)
    if number_of_players == 5:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
        p4 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 4: " + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
        p4.grid(row=3, column=0)
        p5 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 5: " + str(playerList[4].card1.__str__()) + ' ' + str(playerList[4].card2.__str__()))
        p5.grid(row=4, column=0)
    if number_of_players == 6:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
        p4 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 4: " + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
        p4.grid(row=3, column=0)
        p5 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 5: " + str(playerList[4].card1.__str__()) + ' ' + str(playerList[4].card2.__str__()))
        p5.grid(row=4, column=0)
        p6 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 6: " + str(playerList[5].card1.__str__()) + ' ' + str(playerList[5].card2.__str__()))
        p6.grid(row=5, column=0)
    if number_of_players == 7:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
        p4 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 4: " + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
        p4.grid(row=3, column=0)
        p5 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 5: " + str(playerList[4].card1.__str__()) + ' ' + str(playerList[4].card2.__str__()))
        p5.grid(row=4, column=0)
        p6 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 6: " + str(playerList[5].card1.__str__()) + ' ' + str(playerList[5].card2.__str__()))
        p6.grid(row=5, column=0)
        p7 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 7: " + str(playerList[6].card1.__str__()) + ' ' + str(playerList[6].card2.__str__()))
        p7.grid(row=6, column=0)
    if number_of_players == 8:
        p1 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 1: " + str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
        p1.grid(row=0, column=0)
        p2 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 2: " + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
        p2.grid(row=1, column=0)
        p3 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 3: " + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
        p3.grid(row=2, column=0)
        p4 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 4: " + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
        p4.grid(row=3, column=0)
        p5 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 5: " + str(playerList[4].card1.__str__()) + ' ' + str(playerList[4].card2.__str__()))
        p5.grid(row=4, column=0)
        p6 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 6: " + str(playerList[5].card1.__str__()) + ' ' + str(playerList[5].card2.__str__()))
        p6.grid(row=5, column=0)
        p7 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 7: " + str(playerList[6].card1.__str__()) + ' ' + str(playerList[6].card2.__str__()))
        p7.grid(row=6, column=0)
        p8 = Label(root, padx=10, pady=10, borderwidth=3, relief="sunken", text="player 8: " + str(playerList[7].card1.__str__()) + ' ' + str(playerList[7].card2.__str__()))
        p8.grid(row=7, column=0)
        theBoard = Board(theDeck.deck[(number_of_players * 2) + 1], theDeck.deck[(number_of_players * 2) + 2], theDeck.deck[(number_of_players * 2) + 3], theDeck.deck[(number_of_players * 2) + 4], theDeck.deck[(number_of_players * 2) + 5])
        board = Label(root, padx=20, pady=20, borderwidth=3, relief='raised', text='BOARD' + '\n' + str(theBoard.flop1) + ' ' + str(theBoard.flop2) + ' ' + str(theBoard.flop3) + ' ' + str(theBoard.turn) + ' ' + str(theBoard.river) )
        board.grid(row=5, column=4)
#Balls

root = Tk()
root.resizable(width=False, height=False)
root.title("Poker")

button = Button(root, width= 8, height=4, text='Start', command=rungame)
button.grid(row=0, column=0)

slider = Scale(root, from_=2, to=8, orient=HORIZONTAL)
slider.grid(row=1, column=0)

label = Label(root, text='How many players are playing?')
label.grid(row=2, column=0)

bg = PhotoImage(file="poker_background.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)



root.mainloop()
