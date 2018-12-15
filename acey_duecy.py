# acey_duecy.py
#
# This program replicates card game Acey Duecy card.  
#
# Author: Ranjeeta Bhattacharya

import random           # Importing random class

class Card():           # Card class definition of cards
    
    card_suits = ['C','D','H','S']                                       # Creating suit list with initials
    
    card_ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']  # Creating rank list in desired order
    
    def __init__(self,suit=0,rank=0):                                    # Creating constructor method for card class
        self.suit = suit
        self.rank = rank
       
    def __str__(self):
        return '%s%s' % (Card.card_ranks[self.rank],                     # Creating special method to represent string
                         Card.card_suits[self.suit]) 

   
class Deck():                             # Deck class definition for deck of cards
    
    def __init__(self):                   # Creating an empty list of cards. Constructor.
        self.cards = []   
        
        for suit in range(4):
            for rank in range(13):
                card = Card(suit,rank)
                self.cards.append(card)
                    
    
    def deal(self, i=-1):                  # Method to deal the top most card of the deck
        return self.cards.pop(i)
    
    
    def shuffle(self):                     # Method to shuffle the deck of cards
        random.shuffle(self.cards)         # Shuffling the card deck  


# Created a key value dictionary pair for extracting numeric value of a card

card_dict = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

# Global variable flag to control game continuity

deal_flag = True 


def definition():
# """Prints a brief explanation of the game Acey-Deucey"""
 
    print ("Acey-Deucey is played in the following manner")
    print ("---------------------------------------------\n")
    print ("-> You have a starting wager amount which can be used to place a bet")
    print ("-> The dealer (computer) deals two cards face up")
    print ("-> You have an option to bet or not bet depending")
    print ("   on whether or not you feel the card will have")
    print ("   a value between the first two.")
    print ("-> If you don't want to bet, input a 0")
    print ("-> You cannot bet more than you have")
    print ("-> You win if rank of the card you draw is between the ")
    print ("   rank of the cards drawn by the computer ")
    print ("-> On winning, the amount placed as bet gets added to player wager")
    print ("-> On losing, the amount placed as bet gets deducted to player wager")
    print ("-> Game ends if there is no more money left to bet")
    

# Function body declaration for controling playing choice

def again():
    global deal_flag
    input_prompt = input("Do you want to play? (Y/N) \n")
    print("--------------------------")

    if (input_prompt.upper() == 'Y'):
        return deal_flag
    else:
        print("Invalid input or 'N' entered. Quitting Game...")
        deal_flag = False
        return deal_flag

# Function body declaration for checking the input bet value

def enter_bet():
    
    while True:
        try:
            bet_val = int(input("\nWhat is your bet?($): "))
            return bet_val
        except ValueError:
            print("\nNot a valid bet number. Please enter again.....")    

# Function body declaration to control all card hand dealings and produce approriate comparison results

def deal(stake):    
    
    print("\nDealing two cards from the shuffled deck")
    
    deal_first = card_deck.deal()   # Dealing first card
    deal_second = card_deck.deal()  # Dealing second card
    
    print("\nFirst dealt card: ",deal_first)
    print("\nSecond dealt card: ",deal_second)
    
    bet_val = enter_bet()
    
    if (bet_val == 0):
        print("\nNothing to bet. Deal again..")
        return stake
    else:
        pass
    
    
    while (bet_val > stake):
        print("\nSorry! You cannot bet more than you have. Try again: ")
        bet_val = enter_bet()
    else:
        bet_flag = True
        pass
    
            
    deal_bet = card_deck.deal()  
    print("\nThird dealt card: ",deal_bet)   # Dealing the third card on behalf of user
    
    # Next few lines converts card object to string and slices the same to get the rank value
    
    first_int = deal_first.__str__()
    first_int = first_int[:1]
    first_int = card_dict[first_int]
    first_int = int(first_int)
        
    second_int = deal_second.__str__()
    second_int = second_int[:1]
    second_int = card_dict[second_int]
    second_int = int(second_int)
        
    third_int = deal_bet.__str__()
    third_int = third_int[:1]
    third_int = card_dict[third_int]
    third_int = int(third_int)
        
    if first_int > second_int:                       # Swap the cards in correct order for comparison   
        first_int, second_int = second_int, first_int
            
    if third_int in range(first_int,second_int):
        print("\nCongratulations! You win. Winning amount added to the current wager balance\n")
        print("-----------------------------------------------------------------------------\n")
        bet_val = stake + bet_val
    else:
        print("\nSorry! You lose. Loosing amount deducted from the current wager balance")
        print("-------------------------------------------------------------------------\n")
        bet_val = stake - bet_val        
    
    return bet_val
        

# Main Program

print("Welcome to the card game Acey-Deucey ")
print("-------------------------------------")

definition()                    # Calling function to print a brief summary of the game

deal_flag = again()             # Calling function to check playing choice

card_deck = Deck()              # Create an object of card class

card_deck.shuffle()             # Shuffling the deck of cards

choice = True

# Implementing exception handling to check the validity of input values 

while(choice and deal_flag):
    try:
        current_stake = int(input("You want to play the game with how much money?($):"))
        choice = False
    except ValueError:        
        print("\nNot a valid monetary value. Please enter again.....")    
    
# Loop will continue as long as player wants to play

while (deal_flag):    
    print("Your current wager balance (in $):",current_stake)  # Current balance in hand
    
    if (current_stake == 0):
        print("\nSorry! No wager balance left to play.Game ending..")
        break
    else:
        current_stake = deal(current_stake)
            
    if current_stake <= 0:
        print("\nSorry! No wager balance left to play.Game ending..")
        break
    else:   
        deal_flag = again()
        if (deal_flag):
            print("Your current wager balance (in $):",current_stake)
            if (current_stake == 0):
                print("\nSorry! No wager balance left to play.Game ending..")
                break
            else:
                current_stake = deal(current_stake)
        else:
            break
