# Card_Games_Projects

This folder consists of list of Python scripts for playing popular card games in a interactive fashion.

Script card_game.py is a object-oriented programming version of playing with a deck of cards having different methods like:

deal - a method that returns the value of the card on top of the deck.  Once a card is dealt it cannot be dealt again until the deck is shuffled.
shuffle - a method that returns to the deck all dealt cards (for a total of 52, no Jokers) and places it in a random order.
fan - fan is a method that will simply list the cards in the deck from the top card to the card on the bottom of the deck.
isOrdered - a method that returns True if the deck is in order and False if it is not.  If an ordered deck has a few cards dealt off of the top it is still in order. You do not need a full deck to be in order.
Order - a method that sorts the deck or puts the cards in order with the 2 of clubs beings lowest and the ace of spades being highest (while there is no real ranking of suits we’ll go with the standard poker/bridge ranking of clubs(lowest), diamonds, hearts, spades(highest).  We will also count the Ace as a high card and not a low card. The Ace of a particular suit should be the highest card when a suit is sorted (2 thru A). 

Script acey_duecy.py is a object-oriented programming version of interactive card game Acey Duecy (https://en.wikipedia.org/wiki/Acey_Deucey_(card_game)).
