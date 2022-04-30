import random
from itertools import combinations
############## -------CLASSES-----------

class Card:
    def __init__(self, number, suit):
        self.number = str(number)
        self.suit = suit

    def __str__(self):
        return self.number + self.suit

    def rank(self):
        if self.number == 'A':
            return 14
        elif self.number == 'K':
            return 13
        elif self.number == 'Q':
            return 12
        elif self.number == 'J':
            return 11
        else:
            return int(self.number)

class Board:
    def __init__(self, flop1, flop2, flop3, turn, river):
        self.flop1 = flop1
        self.flop2 = flop2
        self.flop3 = flop3
        self.turn = turn
        self.river = river

    def __str__(self):
        return 'Board:  ' + self.flop1.__str__() + ', ' + self.flop2.__str__() + ', ' + \
               self.flop3.__str__() + ', ' + self.turn.__str__() + ', ' + self.river.__str__()

class Deck:
    def __init__(self):
        self.deck = [Card('2', 'H'), Card('3', 'H'), Card('4', 'H'), Card('5', 'H'), Card('6', 'H'), Card('7', 'H'),
                     Card('8', 'H'),
                     Card('9', 'H'), Card('10', 'H'), Card('J', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('A', 'H'),

                     Card('2', 'S'), Card('3', 'S'), Card('4', 'S'), Card('5', 'S'), Card('6', 'S'), Card('7', 'S'),
                     Card('8', 'S'),
                     Card('9', 'S'), Card('10', 'S'), Card('J', 'S'), Card('Q', 'S'), Card('K', 'S'), Card('A', 'S'),

                     Card('2', 'C'), Card('3', 'C'), Card('4', 'C'), Card('5', 'C'), Card('6', 'C'), Card('7', 'C'),
                     Card('8', 'C'),
                     Card('9', 'C'), Card('10', 'C'), Card('J', 'C'), Card('Q', 'C'), Card('K', 'C'), Card('A', 'C'),

                     Card('2', 'D'), Card('3', 'D'), Card('4', 'D'), Card('5', 'D'), Card('6', 'D'), Card('7', 'D'),
                     Card('8', 'D'),
                     Card('9', 'D'), Card('10', 'D'), Card('J', 'D'), Card('Q', 'D'), Card('K', 'D'), Card('A', 'D')]

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        x = 'Deck:  '
        for i in range(len(self.deck)):
            x += str(self.deck[i].__str__()) + ','
        return x


class Player:
    handOf7: list[Card] = []
    strength = []
    allCombinations: list[Card] = [[]]

    def __init__(self, card1: Card, card2: Card):
        self.card1 = card1
        self.card2 = card2

    def __str__(self):
        x = ''
        x += 'Card 1: ' + self.card1.__str__()
        x += '  Card 2: ' + self.card2.__str__()
        return x


# # -------METHODS-----------

# DOESNT WORK
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
    return 3
# DOESNT WORK


def sortByRank(hand: list[Card]):
    hand = list(hand)
    for i in range(4):
        for j in range(0, 4 - i):
            if hand[j].rank() < hand[j + 1].rank():
                hand[j], hand[j + 1] = hand[j + 1], hand[j]

    return hand


# takes 7 cards, creates a 2d array of all possible 5 card combinations
def combinationsOfFive(handof7):
    # handof7 = [card1,card2,card3,card4,card5,card6,card7]
    r = 5
    combination = list(combinations(handof7, r))
    return combination


# evaluates all the possible 5 card hands given, returns the highest return value gotten
def evaluteHand(allPossible):
    maximum = [-1]
    for i in allPossible:

        if isRoyal(i)[0] == 9:
            maximum = isRoyal(i)


        elif isStraightFlush(i)[0] == 8:
            if maximum[0] < 8:
                maximum = isStraightFlush(i)
            elif maximum[0] == 8:
                # maximum is a straight flush hand
                if isStraightFlush(i)[1] > maximum[1]:
                    maximum = isStraightFlush(i)


        elif isfourOfAKind(i)[0] == 7:
            if maximum[0] < 7:
                maximum = isfourOfAKind(i)
            elif maximum[0] == 7:
                # maximum is a four of a kind
                if isfourOfAKind(i)[1] > maximum[1]:
                    maximum = isfourOfAKind(i)
                elif isfourOfAKind(i)[1] == maximum[1]:
                    if isfourOfAKind(i)[2] > maximum[2]:
                        maximum = isfourOfAKind(i)


        elif isfullHouse(i)[0] == 6:
            if maximum[0] < 6:
                maximum = isfullHouse(i)
            elif maximum[0] == 6:
                # maximum is a full house hand
                if isfullHouse(i)[1] > maximum[1]:
                    maximum = isfullHouse(i)
                elif isfullHouse(i)[1] == maximum[1]:

                    if isfullHouse(i)[2] > maximum[2]:
                        maximum = isfullHouse(i)


        elif isFlush(i)[0] == 5:
            if maximum[0] < 5:
                maximum = isFlush(i)
            elif maximum[0] == 5:
                # maximum is a flush hand
                if isFlush(i)[1] > maximum[1]:
                    maximum = isFlush(i)
                elif isFlush(i)[1] == maximum[1]:

                    if isFlush(i)[2] > maximum[2]:
                        maximum = isFlush(i)
                    elif isFlush(i)[2] == maximum[2]:

                        if isFlush(i)[3] > maximum[3]:
                            maximum = isFlush(i)
                        elif isFlush(i)[3] == maximum[3]:

                            if isFlush(i)[4] > maximum[4]:
                                maximum = isFlush(i)
                            elif isFlush(i)[4] == maximum[4]:

                                if isFlush(i)[5] > maximum[5]:
                                    maximum = isFlush(i)


        elif isStraight(i)[0] == 4:
            if maximum[0] < 4:
                maximum = isStraight(i)
            elif maximum[0] == 4:
                # maximum is a straight hand
                if isStraight(i)[1] > maximum[1]:
                    maximum = isStraight(i)


        elif isThreeOfAKind(i)[0] == 3:
            if maximum[0] < 3:
                maximum = isThreeOfAKind(i)
            elif maximum[0] == 3:
                # maximum is a three of a kind hand
                if isThreeOfAKind(i)[1] > maximum[1]:
                    maximum = isThreeOfAKind(i)
                elif isThreeOfAKind(i)[1] == maximum[1]:

                    if isThreeOfAKind(i)[2] > maximum[2]:
                        maximum = isThreeOfAKind(i)
                    elif isThreeOfAKind(i)[2] == maximum[2]:

                        if isThreeOfAKind(i)[3] > maximum[3]:
                            maximum = isThreeOfAKind(i)


        elif isTwoPair(i)[0] == 2:
            if maximum[0] < 2:
                maximum = isTwoPair(i)
            elif maximum[0] == 2:

                # maximum is a two pair hand
                if isTwoPair(i)[1] > maximum[1]:
                    maximum = isTwoPair(i)
                elif isTwoPair(i)[1] == maximum[1]:

                    if isTwoPair(i)[2] > maximum[2]:
                        maximum = isTwoPair(i)
                    elif isTwoPair(i)[2] == maximum[2]:

                        if isTwoPair(i)[3] > maximum[3]:
                            maximum = isTwoPair(i)


        elif isOnePair(i)[0] == 1:
            if maximum[0] < 1:
                maximum = isOnePair(i)
            if maximum[0] == 1:
                # maximum is a one pair hand
                #

                # for j in range(len(isOnePair(i))):
                #     if isOnePair(i)[j] >maximum[j]:
                #         maximum = isOnePair(i)
                #

                if isOnePair(i)[1] > maximum[1]:
                    maximum = isOnePair(i)
                elif isOnePair(i)[1] == maximum[1]:

                    if isOnePair(i)[2] > maximum[2]:
                        maximum = isOnePair(i)
                    elif isOnePair(i)[2] == maximum[2]:

                        if isOnePair(i)[3] > maximum[3]:
                            maximum = isOnePair(i)
                        elif isOnePair(i)[3] == maximum[3]:

                            if isOnePair(i)[4] > maximum[4]:
                                maximum = isOnePair(i)


        else:
            if maximum[0] < 0:
                maximum = isHighCard(i)
            if maximum[0] == 0:
                # maximum is a high card hand

                # for j in range(len(isHighCard(i))):
                #     if isHighCard(i)[j] > maximum[j]:
                #         maximum = isHighCard(i)

                if isHighCard(i)[1] > maximum[1]:
                    maximum = isHighCard(i)
                elif isHighCard(i)[1] == maximum[1]:

                    if isHighCard(i)[2] > maximum[2]:
                        maximum = isHighCard(i)
                    elif isHighCard(i)[2] == maximum[2]:

                        if isHighCard(i)[3] > maximum[3]:
                            maximum = isHighCard(i)
                        elif isHighCard(i)[3] == maximum[3]:

                            if isHighCard(i)[4] > maximum[4]:
                                maximum = isHighCard(i)
                            elif isHighCard(i)[4] == maximum[4]:

                                if isHighCard(i)[5] > maximum[5]:
                                    maximum = isHighCard(i)

    return maximum


# hand methods
def isRoyal(hand: list[Card]):
    # 9
    if isStraight(hand) == [4, 14] and isFlush(hand) == [5, 14, 13, 12, 11, 10]:
        return [9]
    else:
        return [-1]


def isStraightFlush(hand: list[Card]):
    # 8
    straightReturn = isStraight(hand)
    flushReturn = isFlush(hand)
    if straightReturn[0] == 4 and flushReturn[0] == 5:
        return [8, straightReturn[1]]
    else:
        return [-1]


def isfourOfAKind(hand: list[Card]):
    # 7 should be good tested light
    isQuads = False
    high = -1
    kicker = -1
    for i in hand:
        count = 0
        temp = i.rank()
        for j in range(5):
            if hand[j].rank() == temp:
                count += 1
            if count == 4:
                isQuads = True
                high = temp
    if isQuads:
        for i in hand:
            if i.rank() != high:
                kicker = i.rank()
        return [7, high, kicker]
    else:
        return [-1]


def isfullHouse(hand: list[Card]):
    # 6
    tripsAns = isThreeOfAKind(hand)
    if tripsAns[0] == 3:
        if tripsAns[2] == tripsAns[3]:
            return [6, tripsAns[1], tripsAns[2]]
        else:
            return [-1]
    else:
        return [-1]


def isFlush(hand: list[Card]):
    # 5
    hand = sortByRank(hand)
    if hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit:
        return [5, hand[0].rank(), hand[1].rank(), hand[2].rank(), hand[3].rank(), hand[4].rank()]
    else:
        return [-1]


def isStraight(hand: list[Card]):
    # 4
    Straight = False
    high = -1
    hand = sortByRank(hand)
    containsAce = False
    containsFive = False
    # find out if it contains an ace and 5
    for i in hand:
        if i.rank() == 14:
            containsAce = True
        if i.rank() == 5:
            containsFive = True
    # check for an ace to 5 straight
    if containsAce and containsFive:
        if hand[1].rank() == 5 and hand[2].rank() == 4 and hand[3].rank() == 3 and hand[4].rank() == 2:
            Straight = True
            high = 5
    # check for all other straights
    else:
        if hand[0].rank() - 1 == hand[1].rank() and hand[1].rank() - 1 == hand[2].rank() and hand[2].rank() - 1 == hand[
            3].rank() and hand[3].rank() - 1 == hand[4].rank():
            Straight = True
            high = hand[0].rank()
    if Straight:
        return [4, high]
    else:
        return [-1]


def isThreeOfAKind(hand: list[Card]):
    # 3
    hand = sortByRank(hand)
    isTrips = False
    high = -1
    kicker1 = -1
    kicker2 = -1
    for i in hand:
        count = 0
        temp = i.rank()
        for j in range(5):
            if hand[j].rank() == temp:
                count += 1
            if count == 3:
                isTrips = True
                high = temp
    if isTrips:
        for i in hand:
            if i.rank() != high:
                kicker1 = i
                break
        for i in hand:
            if i.rank() != high and i.rank() != kicker1:
                kicker2 = i
        return [3, high, kicker1.rank(), kicker2.rank()]
    else:
        return [-1]


def isTwoPair(hand: list[Card]):
    # 2
    hand = sortByRank(hand)
    isOne = False
    isTwo = False
    firstPair = -1
    secondPair = -1
    kicker = -1
    for i in hand:
        count = 0
        temp = i.rank()
        for j in range(5):
            if hand[j].rank() == temp:
                count += 1
            if count == 2:
                isOne = True
                firstPair = temp
            if isOne:
                break
    if isOne:
        for x in hand:
            count = 0
            temptwo = x.rank()
            for y in range(5):
                if hand[y].rank() == temptwo and temptwo != firstPair:
                    count += 1
                if count == 2:
                    isTwo = True
                    secondPair = temptwo
    if isOne and isTwo:
        for e in hand:
            if e.rank() != firstPair and e.rank() != secondPair:
                kicker = e.rank()
        return [2, firstPair, secondPair, kicker]
    else:
        return [-1]


def isOnePair(hand: list[Card]):
    # 1
    hand = sortByRank(hand)
    isOne = False
    pair = -1
    k1 = -1
    k2 = -1
    k3 = -1
    for i in hand:
        count = 0
        temp = i.rank()
        for j in range(5):
            if hand[j].rank() == temp:
                count += 1
            if count == 2:
                isOne = True
                pair = temp
    if isOne:
        for x in hand:
            if x.rank() != pair:
                k1 = x.rank()
            if k1 != -1:
                break
        for x in hand:
            if x.rank() != pair and x.rank() != k1:
                k2 = x.rank()
            if k2 != -1:
                break
        for x in hand:
            if x.rank() != pair and x.rank() != k1 and x.rank() != k2:
                k3 = x.rank()
            if k3 != -1:
                break
        return [1, pair, k1, k2, k3]
    else:
        return [-1]


def isHighCard(hand: list[Card]):
    hand = sortByRank(hand)
    return [0, hand[0].rank(), hand[1].rank(), hand[2].rank(), hand[3].rank(), hand[4].rank()]


############## -------MAIN LOGIC-----------
#
# # initialize and shuffle the deck of cards
# theDeck = Deck()
# theDeck.shuffle()
# # get input for the number of players from the user
# numOfPlayers = input("Input number of players between 2 and 10: ")
# # while not isinstance(numOfPlayers, int):
# #     print('enter int val')
# #     numOfPlayers = input('Input number of players between 2 and 10: ')
#
#
# numOfPlayers = int(numOfPlayers)
# ## create "numOfPLayers" Players as "Player" objects in a Player list called "playerArray"
# playerList = []
# for i in range(numOfPlayers):
#     tempCard1 = Card(theDeck.deck[i].number, theDeck.deck[i].suit)
#     tempCard2 = Card(theDeck.deck[numOfPlayers + i].number, theDeck.deck[numOfPlayers + i].suit)
#     tempPlayer = Player(tempCard1, tempCard2)
#     playerList.append(tempPlayer)
# # initialize the board
# theBoard = Board(theDeck.deck[(numOfPlayers * 2) + 1], theDeck.deck[(numOfPlayers * 2) + 2],
#                  theDeck.deck[(numOfPlayers * 2) + 3], theDeck.deck[(numOfPlayers * 2) + 4],
#                  theDeck.deck[(numOfPlayers * 2) + 5])
# # set each players "hand of 7" variable to a list containing their two hole cards along with the board
# for i in playerList:
#     i.handOf7 = [i.card1, i.card2, theBoard.flop1, theBoard.flop2, theBoard.flop3, theBoard.turn, theBoard.river]
# # send each players "handof7" to the "combinationsOfFive" function and store them in each players "allcombinations" attriubte
# for i in range(numOfPlayers):
#     playerList[i].allCombinations = combinationsOfFive(playerList[i].handOf7)
# # send each players "allcombinations" attribute to the "evaluateHand" function, and store the returned value in that players "strength" attribute
# for i in range(numOfPlayers):
#     playerList[i].strength = evaluteHand(playerList[i].allCombinations)
#
# # compare each players strength and evaluate a winner
#
#
# # winner is the index of each player in playerlist with the best hand
# # winner = [0]
# # for i in range(1, numOfPlayers - 1):
# #     returned = compareStrength(playerList[winner[0]].strength, playerList[i].strength)
# #     if returned == 2:
# #         winner[0] = i
# #     if returned == 3:
# #         winner.append(i)
#
# # print statements
# print(theBoard.__str__())
# for i in range(numOfPlayers):
#     print()
#     print('Player {}'.format(i + 1))
#     print(playerList[i].__str__())
#     print(playerList[i].strength)
#
# print()
# print()
# print()
# print()
# #
# # for i in range(len(winner)):
# #     if len(winner) == 1:
# #         print('Player {} Wins!'.format(winner[i] + 1))
# #         print(playerList[winner[i]].__str__())
# #         print(playerList[winner[i]].strength)
# #     else:
# #         print('Player {} Tied for first'.format(winner[i + 1]))
# #         print(playerList[winner[i]].__str__())
# #         print(playerList[winner[i]].strength)
#
#
#
#
# # winners is a list which will be full of the indexes in playerlist that are all the winners of the hand
# winners = []
# #first determine one winner, and then compare everyone else against that winner, and if they tie, then add their indices to winners[]
# first_winner: Player = playerList[0]
# for i in playerList:
#     ret = compareStrength(first_winner.strength, i.strength)
#     if ret == 2:
#         first_winner = i
#
# print(first_winner)
#
# # for i in range(len(playerList)):
# #     ret = compareStrength(playerList[i].strength, playerList[i+1].strength)
# #
#
#
#



