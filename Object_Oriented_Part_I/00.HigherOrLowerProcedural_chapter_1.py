#!/usr/bin/env python3
import random

'''
Chapter 1: Procedural Python Example

The procedural programming style, which involves splitting a program into a
number of functions (also known as procedures or subroutines). You pas data
into functions, each which performs one or more computations and, typically,
passes back results.

Object-oriented programming gives programmers a way to combine code and data
together into cohesive units, thereby avoiding some complications inherent in
procedural programming.

Chapter Goals:
    1) Review of python concepts, by building two small programs
    2) First programs is small card game Higher or Lower
    3) Simulation of a bank, performing operations on one, two, and multiple
        accounts
    4) Later, we'll rewrite these programs using OOP techniques. The main
        purpose of this chapter is to demostrate the key problems inherent
        in procedural programming.
'''

# Program_1: Higher or Lower Card Game

'''

1) Eight cards are randomly chosen from a deck.The first card is shown face up

2) The game asks the player to predict whether the next card in the selection
   will have a higher or lower value than the currently showing card.

3) Ex: say the card that's shown is a 3. The player chooses "higher," and the
   next card is shown. If that card has a higher value, the player is correct.
   In this example, if the player had choosen "lower" they would have been
   incorrect.

4) If the player guesses correctly, they get 20 points. If they choose incorr-
   rectly, they loose 15 points. If the next card to be turned over has the
   same value as the previous card, the player is incorrect.
'''


# Card constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = (
        '',
        'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
        'Queen', 'King')
NCARDS = 8

# Pass in a deck and this retuns a random card from the deck


def getCard(deckListIn):
    thisCard = deckListIn.pop()     # Pop one off the top of the deck & return
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()     # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Main code
print('Welcome to Higher or Lower.')
print('''You have to choose whether the next card to be shown will be higher
or lower than the current card.''')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)
score = 50

while True:     # Play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is: ', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card be higher or lower than the ' +
                        currentCardRank + ' of ' +
                        currentCardSuit + ' ?  (enter h or l):')
        answer = answer.casefold()      # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']   

        print('Next card is: ', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20

            elif answer == 'l':
                if nextCardValue < currentCardValue:
                    score = score + 20
                    print('You got it right, it was lower')
                else:
                    score = score - 15
                    print('Sorry, it was not lower')

            print('Your score is: ', score)
            print()
            currentCardRank = nextCardRank
            cirrentCardValue = nextCardValue    # don't need current suite

    goAgain = input('To play again, press, ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break
print('Ok Bye')
