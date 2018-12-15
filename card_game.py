# card_game.py
#
# A object oriented card game program which hosts different functions to deal a card from a deck, shuffle the deck,
# display the entire deck of cards, checks if the deck is ordered or not, sorts a shuffled deck of cards. 
#
# Author: Ranjeeta Bhattacharya


import random                         # Importing random module

original_list = []                    # Declaring global variables
shuffled_list = []
sorted_card_list = []

sorted_list_flag = "N"
shuffled_deck = False                 

# Card class definition representing card features like suit and rank

class Card():
    
    # Creating suit list with initials
    
    card_suits = ['C','D','H','S']                                       
    
    # Creating rank list in desired order. 2 being lowest and A (Ace) being highest
    
    card_ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']  
    
    def __init__(self,suit=0,rank=0):                                    # Creating constructor method for card class
        self.suit = suit
        self.rank = rank
       
    def __str__(self):
        return '%s%s' % (Card.card_ranks[self.rank],                     # Creating special method to represent string
                         Card.card_suits[self.suit])          
   
    def __cmp__(self, other):             # Creating special method for comparing suit and rank objects
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)
 
       
    def __lt__(self, other):             # Creating special method for comparing suit and rank objects
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.rank < other.rank

class Deck():              # Deck class definition for deck of cards
    
    def __init__(self):    # Creating an empty list of cards. Constructor.
        self.cards = []   
        original_list = []
        
        for suit in range(4):
            for rank in range(13):
                card = Card(suit,rank)
                self.cards.append(card)
                
        original_list = self.cards    
    
    def deal(self, i=-1):                  # Method to deal the top most card of the deck
        return self.cards.pop(i)
    
    def add_card(self, card):              # Method to add the dealt card back to deck
        self.cards.append(card)
        
    
    def shuffle(self):                     # Method to shuffle the deck of cards
        
        global shuffled_list               # Declaring the scope of the variable as global to access locally  
        
        global shuffled_deck               # Declaring the scope of the variable as global to access locally
        
        random.shuffle(self.cards)         # Shuffling the card deck  
        
        shuffled_list = random.sample(self.cards,len(self.cards))  # Extracting the shuffled list
            
        shuffled_deck = True               # Setting shuffled flag as True post shuffle
    
    def fan(self):                         # Method to display the entire card deck
        for card in self.cards:
            print("",card)
            
    def isOrdered(self):                   # Method to check if the deck of cards is ordered or not
            
        global shuffled_deck               # Explicitly declaring global variable
        
        global original_list               # Explicitly declaring global variable
        
        global sorted_list_flag            # Explicitly declaring global variable
        
        copyList = self.cards.copy()       # Making a copy of the current card list        
            
        if sorted_list_flag == 'Y':
            #sorted_list_flag = 'N'
            return True
        else:            
            if shuffled_deck == True:      # Comparing the present card deck with previously shuffled list  
                for item in copyList:
                    for item1 in shuffled_list:
                        if item == item1:
                            return True
                        else:
                            return False        
            else:
                return True
        
    def Order(self):                      # Method to sort the current deck of cards in ascending order
        self.cards.sort()
        
        
# Function definition of cont_game. This checks continuity of the program.
        
def cont_game():
    choice = input(" Do you want to continue? Type Y/N: ")

    if (choice == "Y" or choice == "y"):
        return True
    else:
        print(" Entered 'N/n' or invalid input") 
        return False


# Main Program

print(" You are about to enter the interactive card program")
print(" Please select amongst the choice given below")
print(" ---------------------------------------------------")

test_deck = Deck()                # Creating object of Deck class

bool_val = cont_game()            # Invoking function cont_game to check continuity

while(bool_val):                  # Loop will continue untill Quitting

    inputChoice = input("\n Type D to Deal the top deck card \n Type S to Shuffle deck \n Type F to display deck \n Type I to check if ordered \n Type O to order deck \n Type Q to quit \n ----------------------------------------\n")  
  
    if inputChoice.upper() == "D":
        top_card = test_deck.deal()           # Invoking deal method to pop card
        print("\n Top dealt card of the current deck: ",top_card)
        
        choice = input(" Do you want to put the dealt card back to the deck? Type Y/N: ")

        if (choice == "Y" or choice == "y"):
            print("\n Adding the dealt card '",top_card,"' back to the deck")
            test_deck.add_card(top_card)          # Invoking add_card method to add the dealt card back to deck                
        else:
            print("\n Dealt card '",top_card,"' NOT put back to the deck") 
            pass
            
        test_deck.shuffle()                   # Shuffling the entire deck post shuffling
        print("\n Deck shuffled post deal")
        sorted_list_flag = "N"
            
    elif inputChoice.upper() == "S":
        test_deck.shuffle()                   # Invoking shuffle method to shuffled card deck
        print("\n Current deck of cards shuffled")
        sorted_list_flag = "N"

    elif inputChoice.upper() == "F":
        print("\n Current deck of cards displayed:\n") # Invoking fan method to display card deck
        test_deck.fan()

    elif inputChoice.upper() == "I":
        boolean_val = test_deck.isOrdered() # Invoking isOrdered method to check if card deck is ordered
        print("\n Ordering status of current deck: ",boolean_val)

    elif inputChoice.upper() == "O":
        sorted_card_list = test_deck.Order()  # Invoking order method to order the card deck
        print("\n Current deck of cards sorted/ordered")
        sorted_list_flag = "Y"       

    elif inputChoice.upper() == "Q":
        print("\n Bye Bye.")
        break
    else:
        print("\n Invalid input entered.")
        break

print(" Quitting Program....")

