import os
import time
import random

player_score = 0
dealer_score = 0
    
while len(player_card) < 2:
        player_card = random.choice()
        player_card = random.time()
        player_card = random.randint()
 
        player_score += player_card.card_value
 
        if len(player_card) == 2:
            if player_card[0].card_value == 11 and player_card[1].card_value == 11:
                player_card[0].card_value = 1
                player_score -= 10
     
        print("PLAYER CARDS: ")
        print(player_card, False)
        print("PLAYER SCORE = ", player_score)
 
        input()
 
        dealer_card = random.choice()

        dealer_score += dealer_card.card_value
        print("DEALER CARDS: ")
        if len(dealer_card) == 1:
            print(dealer_card, False)
            print("DEALER SCORE = ", dealer_score)
        else:
            print(dealer_card[:-1], True)    
            print("DEALER SCORE = ", dealer_score - dealer_card[-1].card_value) 
        if len(dealer_card) == 2:
            if dealer_card[0].card_value == 11 and dealer_card[1].card_value == 11:
                dealer_card[1].card_value = 1
                dealer_score -= 10
 
        input()   
if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
 
print("DEALER CARDS: ")
print(dealer_card[:-1], True)
print("DEALER SCORE = ", dealer_score - dealer_card[-1].card_value)
 
print("PLAYER CARDS: ")
print(player_card, False)
print("PLAYER SCORE = ", player_score)
while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Wrong choice!! Try Again")
        if choice.upper() == 'H':
 
            player_card = random.choice()

            player_score += player_card.card_value

            c = 0
            while player_score > 21 and c < len(player_card):
                if player_card[c].card_value == 11:
                    player_card[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
  
            print("DEALER CARDS: ")
            print(dealer_card[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_card[-1].card_value)
            print("PLAYER CARDS: ")
            print(player_card, False)
            print("PLAYER SCORE = ", player_score)
             
        if choice.upper() == 'S':
            break 

print("PLAYER CARDS: ")
print(player_card, False)
print("PLAYER SCORE = ", player_score)
print("DEALER IS REVEALING THE CARDS....")
 
print("DEALER CARDS: ")
print(dealer_card, False)
print("DEALER SCORE = ", dealer_score)
 
if player_score == 21:
        print("PLAYER HAS A BLACKJACK")
if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
 
input() 
while dealer_score < 17:
 
        print("DEALER DECIDES TO HIT.....")
        dealer_card = random.choice()
        dealer_card.append(dealer_card)
 
        dealer_score += dealer_card.card_value
        c = 0
        while dealer_score > 21 and c < len(dealer_card):
            if dealer_card[c].card_value == 11:
                dealer_card[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        print("PLAYER CARDS: ")
        print(player_card, False)
        print("PLAYER SCORE = ", player_score)
 
        print("DEALER CARDS: ")
        print(dealer_card, False)
        print("DEALER SCORE = ", dealer_score)      
if dealer_score > 21:        
        print("DEALER BUSTED..! YOU WIN") 
if dealer_score == 21:
        print("DEALER HAS A BLACKJACK..! PLAYER LOSES")
    
if dealer_score == player_score:
        print("TIE GAME")
elif player_score > dealer_score:
        print("PLAYER WINS")                 
else:
        print("DEALER WINS")    

