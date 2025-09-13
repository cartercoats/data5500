# Import Packages
import sys

# Ask if user wants to play
while True:
    play = input("Would you like to play Blackjack? (y/n)") 

    if play == "n":
        print("Good for you. Gambling is wrong")
        sys.exit()
    elif play == "y":
        print("Ok, let's begin")
        break
    else:
        print("Your answer needs to be y or n")

# Import Deck
from deck import *
deck = Deck()
while True:
    while True:
        print("Deck before shuffle")
        deck.print_deck()
        deck.shuffle_Deck()
        print("Deck after shuffle")
        deck.print_deck()
        # deck.get_card()

        # count aces
        aces = 0
        d_aces = 0

        # deal two cards to the user
        card = deck.get_card()
        print("You drew: " + str(card))
        if card.face == "Ace":
            aces += 1
        card2 = deck.get_card()
        if card2.face == "Ace":
            aces += 1
        print("You drew: " + str(card2))

        # secretly deal two cards to the dealer
        dcard = deck.get_card()
        if dcard.face == "Ace":
            d_aces += 1
        dcard2 = deck.get_card()
        if dcard2.face == "Ace":
            d_aces += 1

        score = 0
        # calculate the user's hand score
        score += card.value
        score += card2.value
        print("Your score is: ", score)

        # ask user if they would like a "hit" (another card) alternatively pass turn to dealer
        hit = input("would you like a hit? y/n")
        if hit == 'y':
            card3 = deck.get_card()
            print("You drew: " + str(card3))
            if card3.face == "Ace":
                aces += 1
            score += card3.value
            # print("new score: ", score)
        else:
            print("Dealer turn")
            break

        if score > 21 and aces > 0:
            aces -= 1
            score -= 10
            # print("new score: ", score)

        print("new score: ", score)

        if score > 21 and aces == 0:
            break

        # ask user if they would like a "hit" (another card) alternatively pass turn to dealer
        hit = input("would you like another hit? y/n")
        if hit == 'y':
            card4 = deck.get_card()
            print("You drew: " + str(card4))
            if card4.face == "Ace":
                aces += 1
            score += card4.value
        else:
            print("Dealer turn")
            break

        if score > 21 and aces > 0:
            aces -= 1
            score -= 10
            #print("new score: ", score)

        print("new score: ", score)

        if score > 21 and aces == 0:
            break

        # ask user if they would like a "hit" (another card) alternatively pass turn to dealer
        hit = input("would you like another hit? y/n")
        if hit == 'y':
            card5 = deck.get_card()
            print("You drew: " + str(card5))
            if card5.face == "Ace":
                aces += 1
            score += card5.value
            #print("new score: ", score)
        else:
            print("Dealer turn")
            break

        if score > 21 and aces > 0:
            aces -= 1
            score -= 10
            #print("new score: ", score)

        print("new score: ", score)

        if score > 21 and aces == 0:
            break

    # Dealer's turn
    dscore = 0
    if score > 21:
        pass
    else:
        while dscore < 17:
            print("Dealer drew: ", str(dcard), "and", str(dcard2))
            dscore = dcard.value + dcard2.value
            print("Dealer score: ", dscore)
            if dscore < 17:
                dcard3 = deck.get_card()
                print("Dealer drew: " + str(dcard3))
                dscore += dcard3.value
                if dscore > 21 and d_aces > 0:
                    d_aces -= 1
                    dscore -= 10
                    
                if dscore > 21 and d_aces == 0:
                    print("Dealer new score: ", dscore)
                    break

                print("Dealer new score: ", dscore)

            if dscore < 17:
                dcard4 = deck.get_card()
                print("Dealer drew: " + str(dcard4))
                dscore += dcard4.value
                if dscore > 21 and d_aces > 0:
                    d_aces -= 1
                    dscore -= 10
                    
                if dscore > 21 and d_aces == 0:
                    print("Dealer new score: ", dscore)
                    break

                print("Dealer new score: ", dscore)

            if dscore < 17:
                dcard5 = deck.get_card()
                print("Dealer drew: " + str(dcard5))
                dscore += dcard5.value
                if dscore > 21 and d_aces > 0:
                    d_aces -= 1
                    dscore -= 10
                    
                if dscore > 21 and d_aces == 0:
                    print("Dealer new score: ", dscore)
                    break
                print("Dealer new score: ", dscore)

    # Resuts
    if dscore >= score and dscore <= 21  and score <= 21:
        print("Dealer's", dscore, "beats your", score, "you lose")
    elif dscore < score and dscore <= 21  and score <= 21:
        print ("Your", score, "beats Dealer's", dscore, "you win!!")
    elif score > 21:
        print("Your score exceeds 21. You lose.")
    elif score <= 21 and dscore > 21:
        print("Dealer's score exceeds 21. You win!")

    play_again = input("Do you want to play again? y/n")
    if play_again == "y":
        pass
    else:
        print("Have a nice day")
        break


