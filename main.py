from tkinter import *
from poker import *

def rungame():
    #get number of players from slider on beginnning page
    global number_of_players
    number_of_players = int(slider.get())

    #get rid of evrrything on the previous screen
    slider.destroy()
    button.destroy()
    label.destroy()

    #make the window bigger
    root.geometry('1001x651')




    #add in 49 frames as a grid for where to put stuff in the root

    #example
    # [frame00]     [frame10]     [frame20]
    # [frame10]
    # [frame20]                   [frame22]
    #
    #
    global frame00
    global frame01
    global frame02
    global frame03
    global frame04
    global frame05
    global frame06
    global frame10
    global frame11
    global frame12
    global frame13
    global frame14
    global frame15
    global frame16
    global frame20
    global frame21
    global frame22
    global frame23
    global frame24
    global frame25
    global frame26
    global frame30
    global frame31
    global frame32
    global frame33
    global frame34
    global frame35
    global frame36
    global frame40
    global frame41
    global frame42
    global frame43
    global frame44
    global frame45
    global frame46
    global frame50
    global frame51
    global frame52
    global frame53
    global frame54
    global frame55
    global frame56
    global frame60
    global frame61
    global frame62
    global frame63
    global frame64
    global frame65
    global frame66
    frame00 = Frame(root)
    frame00.grid(row=0, column=0)
    frame00.config(width=143, height=93, bg='#35654d')
    frame00.propagate(0)

    frame01 = Frame(root)
    frame01.grid(row=1, column=0)
    frame01.config(width=143, height=93, bg='#35654d')
    frame01.propagate(0)

    frame02 = Frame(root)
    frame02.grid(row=2, column=0)
    frame02.config(width=143, height=93, bg='#35654d')
    frame02.propagate(0)

    frame03 = Frame(root)
    frame03.grid(row=3, column=0)
    frame03.config(width=143, height=93, bg='#35654d')
    frame03.propagate(0)

    frame04 = Frame(root)
    frame04.grid(row=4, column=0)
    frame04.config(width=143, height=93, bg='#35654d')
    frame04.propagate(0)

    frame05 = Frame(root)
    frame05.grid(row=5, column=0)
    frame05.config(width=143, height=93, bg='#35654d')
    frame05.propagate(0)

    frame06 = Frame(root)
    frame06.grid(row=6, column=0)
    frame06.config(width=143, height=93, bg='#35654d')
    frame06.propagate(0)

    frame10 = Frame(root)
    frame10.grid(row=0, column=1)
    frame10.config(width=143, height=93, bg='#35654d')
    frame10.propagate(0)

    frame11 = Frame(root)
    frame11.grid(row=1, column=1)
    frame11.config(width=143, height=93, bg='#35654d')
    frame11.propagate(0)

    frame12 = Frame(root)
    frame12.grid(row=2, column=1)
    frame12.config(width=143, height=93, bg='#35654d')
    frame12.propagate(0)

    frame13 = Frame(root)
    frame13.grid(row=3, column=1)
    frame13.config(width=143, height=93, bg='#35654d')
    frame13.propagate(0)

    frame14 = Frame(root)
    frame14.grid(row=4, column=1)
    frame14.config(width=143, height=93, bg='#35654d')
    frame14.propagate(0)

    frame15 = Frame(root)
    frame15.grid(row=5, column=1)
    frame15.config(width=143, height=93, bg='#35654d')
    frame15.propagate(0)

    frame16 = Frame(root)
    frame16.grid(row=6, column=1)
    frame16.config(width=143, height=93, bg='#35654d')
    frame16.propagate(0)

    frame20 = Frame(root)
    frame20.grid(row=0, column=2)
    frame20.config(width=143, height=93, bg='#35654d')
    frame20.propagate(0)

    frame21 = Frame(root)
    frame21.grid(row=1, column=2)
    frame21.config(width=143, height=93, bg='#35654d')
    frame21.propagate(0)

    frame22 = Frame(root)
    frame22.grid(row=2, column=2)
    frame22.config(width=143, height=93, bg='#35654d')
    frame22.propagate(0)

    frame23 = Frame(root)
    frame23.grid(row=3, column=2)
    frame23.config(width=143, height=93, bg='#35654d')
    frame23.propagate(0)

    frame24 = Frame(root)
    frame24.grid(row=4, column=2)
    frame24.config(width=143, height=93, bg='#35654d')
    frame24.propagate(0)

    frame25 = Frame(root)
    frame25.grid(row=5, column=2)
    frame25.config(width=143, height=93, bg='#35654d')
    frame25.propagate(0)

    frame26 = Frame(root)
    frame26.grid(row=6, column=2)
    frame26.config(width=143, height=93, bg='#35654d')
    frame26.propagate(0)

    frame30 = Frame(root)
    frame30.grid(row=0, column=3)
    frame30.config(width=143, height=93, bg='#35654d')
    frame30.propagate(0)

    frame31 = Frame(root)
    frame31.grid(row=1, column=3)
    frame31.config(width=143, height=93, bg='#35654d')
    frame31.propagate(0)

    frame32 = Frame(root)
    frame32.grid(row=2, column=3)
    frame32.config(width=143, height=93, bg='#35654d')
    frame32.propagate(0)

    frame33 = Frame(root)
    frame33.grid(row=3, column=3)
    frame33.config(width=143, height=93, bg='#35654d')
    frame33.propagate(0)

    frame34 = Frame(root)
    frame34.grid(row=4, column=3)
    frame34.config(width=143, height=93, bg='#35654d')
    frame34.propagate(0)

    frame35 = Frame(root)
    frame35.grid(row=5, column=3)
    frame35.config(width=143, height=93, bg='#35654d')
    frame35.propagate(0)

    frame36 = Frame(root)
    frame36.grid(row=6, column=3)
    frame36.config(width=143, height=93, bg='#35654d')
    frame36.propagate(0)

    frame40 = Frame(root)
    frame40.grid(row=0, column=4)
    frame40.config(width=143, height=93, bg='#35654d')
    frame40.propagate(0)

    frame41 = Frame(root)
    frame41.grid(row=1, column=4)
    frame41.config(width=143, height=93, bg='#35654d')
    frame41.propagate(0)

    frame42 = Frame(root)
    frame42.grid(row=2, column=4)
    frame42.config(width=143, height=93, bg='#35654d')
    frame42.propagate(0)

    frame43 = Frame(root)
    frame43.grid(row=3, column=4)
    frame43.config(width=143, height=93, bg='#35654d')
    frame43.propagate(0)

    frame44 = Frame(root)
    frame44.grid(row=4, column=4)
    frame44.config(width=143, height=93, bg='#35654d')
    frame44.propagate(0)

    frame45 = Frame(root)
    frame45.grid(row=5, column=4)
    frame45.config(width=143, height=93, bg='#35654d')
    frame45.propagate(0)

    frame46 = Frame(root)
    frame46.grid(row=6, column=4)
    frame46.config(width=143, height=93, bg='#35654d')
    frame46.propagate(0)

    frame50 = Frame(root)
    frame50.grid(row=0, column=5)
    frame50.config(width=143, height=93, bg='#35654d')
    frame50.propagate(0)

    frame51 = Frame(root)
    frame51.grid(row=1, column=5)
    frame51.config(width=143, height=93, bg='#35654d')
    frame51.propagate(0)

    frame52 = Frame(root)
    frame52.grid(row=2, column=5)
    frame52.config(width=143, height=93, bg='#35654d')
    frame52.propagate(0)

    frame53 = Frame(root)
    frame53.grid(row=3, column=5)
    frame53.config(width=143, height=93, bg='#35654d')
    frame53.propagate(0)

    frame54 = Frame(root)
    frame54.grid(row=4, column=5)
    frame54.config(width=143, height=93, bg='#35654d')
    frame54.propagate(0)

    frame55 = Frame(root)
    frame55.grid(row=5, column=5)
    frame55.config(width=143, height=93, bg='#35654d')
    frame55.propagate(0)

    frame56 = Frame(root)
    frame56.grid(row=6, column=5)
    frame56.config(width=143, height=93, bg='#35654d')
    frame56.propagate(0)

    frame60 = Frame(root)
    frame60.grid(row=0, column=6)
    frame60.config(width=143, height=93, bg='#35654d')
    frame60.propagate(0)

    frame61 = Frame(root)
    frame61.grid(row=1, column=6)
    frame61.config(width=143, height=93, bg='#35654d')
    frame61.propagate(0)

    frame62 = Frame(root)
    frame62.grid(row=2, column=6)
    frame62.config(width=143, height=93, bg='#35654d')
    frame62.propagate(0)

    frame63 = Frame(root)
    frame63.grid(row=3, column=6)
    frame63.config(width=143, height=93, bg='#35654d')
    frame63.propagate(0)

    frame64 = Frame(root)
    frame64.grid(row=4, column=6)
    frame64.config(width=143, height=93, bg='#35654d')
    frame64.propagate(0)

    frame65 = Frame(root)
    frame65.grid(row=5, column=6)
    frame65.config(width=143, height=93, bg='#35654d')
    frame65.propagate(0)

    frame66 = Frame(root)
    frame66.grid(row=6, column=6)
    frame66.config(width=143, height=93, bg='#35654d')
    frame66.propagate(0)









    # initialize and shuffle the deck of cards
    global theDeck
    theDeck = Deck()
    theDeck.shuffle()

    # create "number_of_players" Players as "Player" objects in a Player list called "playerList"
    global playerList
    playerList = []
    for i in range(number_of_players):
        tempCard1 = Card(theDeck.deck[i].number, theDeck.deck[i].suit)
        tempCard2 = Card(theDeck.deck[number_of_players + i].number, theDeck.deck[number_of_players + i].suit)
        tempPlayer = Player(tempCard1, tempCard2)
        playerList.append(tempPlayer)

















    global winner



















    #put a label in the cooresponding frame depending on how many players there are
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8

    p1 = Label(frame35, padx=10, pady=10, borderwidth = 3, relief="sunken", text="You: "+ str(playerList[0].card1.__str__()) + ' ' + str(playerList[0].card2.__str__()))
    p1.pack()
    p2 = Label(frame24, padx=10, pady=10, borderwidth = 3, relief="sunken", text="Player 2: ")
    p2.pack()
    if number_of_players >= 3:
        p3 = Label(frame13, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 3: ")
        p3.pack()
    if number_of_players >= 4:
        p4 = Label(frame22, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 4: ")
        p4.pack()
    if number_of_players >= 5:
        p5 = Label(frame31, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 5: ")
        p5.pack()
    if number_of_players >= 6:
        p6 = Label(frame42, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 6: ")
        p6.pack()
    if number_of_players >= 7:
        p7 = Label(frame53, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 7: ")
        p7.pack()
    if number_of_players >= 8:
        p8 = Label(frame44, padx=10, pady=10, borderwidth=3, relief="sunken", text="Player 8: ")
        p8.pack()
    global theBoard
    theBoard = Board(theDeck.deck[(number_of_players * 2) + 1], theDeck.deck[(number_of_players * 2) + 2], theDeck.deck[(number_of_players * 2) + 3], theDeck.deck[(number_of_players * 2) + 4], theDeck.deck[(number_of_players * 2) + 5])
    global board
    board = Label(frame33, padx=20, pady=20, borderwidth=3, relief='raised', text='BOARD')
    board.pack()
    global next_button
    next_button = Button(frame60, text="Next Round", command=flop)
    next_button.pack()

    #set each players "hand of 7" variable to a list containing their two hole cards along with the board
    for i in playerList:
        i.handOf7 = [i.card1, i.card2, theBoard.flop1, theBoard.flop2, theBoard.flop3, theBoard.turn, theBoard.river]
    # send each players "handof7" to the "combinationsOfFive" function and store them in each players "allcombinations" attriubte
    for i in range(number_of_players):
        playerList[i].allCombinations = combinationsOfFive(playerList[i].handOf7)
    # send each players "allcombinations" attribute to the "evaluateHand" function, and store the returned value in that players "strength" attribute
    for i in range(number_of_players):
        playerList[i].strength = evaluteHand(playerList[i].allCombinations)


    # compare each players strength and evaluate a winner
    def compareStrength(p1: list[int], p2: list[int]):
        size = None
        if len(p1) > len(p2):
            size = len(p2)
        else:
            size = len(p1)
        for i in range(size):
            if p1[i] > p2[i]:
                return 1
            elif p2[i] > p1[i]:
                return 2
        return 2

    for i in range(len(playerList)-1):
        tempwinner = playerList[0]
        if compareStrength(playerList[i].strength, playerList[i+1].strength) == 2:
            tempwinner = i+1
    winner = 'Player '+str(i)+'!'
    print(winner)

# "player 8: " + str(playerList[7].card1.__str__()) + ' ' + str(playerList[7].card2.__str__())
#'BOARD' + '\n' + str(theBoard.flop1) + ' ' + str(theBoard.flop2) + ' ' + str(theBoard.flop3) + ' ' + str(theBoard.turn) + ' ' + str(theBoard.river)


def flop():
    board.config(text='BOARD'+'\n'+str(theBoard.flop1)+ ' ' + str(theBoard.flop2) + ' ' + str(theBoard.flop3))
    next_button.config(command=turn)

def turn():
    board.config(text='BOARD' + '\n' + str(theBoard.flop1) + ' ' + str(theBoard.flop2) + ' ' + str(theBoard.flop3) + ' ' + str(theBoard.turn))
    next_button.config(command=river)

def river():
    board.config(text='BOARD' + '\n' + str(theBoard.flop1) + ' ' + str(theBoard.flop2) + ' ' + str(theBoard.flop3) + ' ' + str(theBoard.turn) + ' ' + str(theBoard.river))
    next_button.config(command=reveal_others)

def reveal_others():
    p2.config(text='Player 2: ' + str(playerList[1].card1.__str__()) + ' ' + str(playerList[1].card2.__str__()))
    p3.config(text='Player 3: ' + str(playerList[2].card1.__str__()) + ' ' + str(playerList[2].card2.__str__()))
    p4.config(text='Player 4: ' + str(playerList[3].card1.__str__()) + ' ' + str(playerList[3].card2.__str__()))
    p5.config(text='Player 5: ' + str(playerList[4].card1.__str__()) + ' ' + str(playerList[4].card2.__str__()))
    p6.config(text='Player 6: ' + str(playerList[5].card1.__str__()) + ' ' + str(playerList[5].card2.__str__()))
    p7.config(text='Player 7: ' + str(playerList[6].card1.__str__()) + ' ' + str(playerList[6].card2.__str__()))
    p8.config(text='Player 8: ' + str(playerList[7].card1.__str__()) + ' ' + str(playerList[7].card2.__str__()))


    #only gets displayed if theres 8 players, bc if there is 7 or less, p8.config is an error and it stops working
    winner_label = Label(frame36, text="The Winner is"+'\n'+str(winner))
    winner_label.pack()
    next_button.config(command=doNone)
def doNone():
    pass


root = Tk()
root.resizable(width=False, height=False)
root.title("Poker")

button = Button(root, width= 8, height=4, text='Start', command=rungame)
button.grid(row=0, column=0)

slider = Scale(root, from_=2, to=8, orient=HORIZONTAL)
slider.grid(row=1, column=0)

label = Label(root, text='How many players are playing?')
label.grid(row=2, column=0)





root.mainloop()
