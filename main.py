import random as rand
import time
# config
deck = []
dealerHand = []
playerHand = []
coins = 300
bet = 0
playerValue = 0
dealerValue = 0
done = False
dealerDone = False
has_ace = False
playerBusted = False
dealerBusted = False
won = False
tie = False
done_playing = False
betOk = False
choiceOk = False
# functions
def CalculateHand(hand, value):
    global playerValue
    global dealerValue
    global has_ace
    has_ace = False
    value = 0
    for i in hand:
        if isinstance(i,int):
            value += i
        else:
            if (i == "A"):
                has_ace = True
                value += 11
            else:
                value += 10
    if has_ace and value > 21:
        value -= 10
    if hand == playerHand:
        playerValue = value
    elif hand == dealerHand:
        dealerValue = value
def reset():
    global playerHand
    global dealerHand
    global playerValue
    global dealerValue
    global playerBusted
    global dealerBusted
    global done_playing
    global done
    global betOk
    done = False
    deck.extend(dealerHand)
    deck.extend(playerHand)
    playerValue = 0
    dealerValue = 0
    playerHand = []
    dealerHand = []
    playerBusted = False
    dealerBusted = False
    betOk = False
    choiceOk = False

# main program
for i in range (0,4):
    deck.extend(["A",2,3,4,5,6,7,8,9,10,"J","Q","K"])
while done_playing == False:
    while betOk == False:
        print("You have", coins,"coins")
        try:
            bet = int(input("Bet? "))
            if bet > coins:
                pass
            else:
                betOk = True
        except:
            pass
    for i in range(2):
        dealing = rand.choice(deck)
        deck.remove(dealing)
        playerHand.append(dealing)
        dealing = rand.choice(deck)
        deck.remove(dealing)
        dealerHand.append(dealing)

    print("Dealer has")
    print(*dealerHand, sep = " and ")
    print("You have")
    print(*playerHand, sep = " and ")
    while done == False:
        while choiceOk == False:
            choice = str(input("1 for stand, 2 for hit: "))
            if choice == "1":
                done = True
                choiceOk = True
            elif choice == "2":
                dealing = rand.choice(deck)
                deck.remove(dealing)
                playerHand.append(dealing)
                choiceOk = True
            else:
                pass
        choiceOk = False
        CalculateHand(playerHand,playerValue)
        print("You have")
        print(*playerHand, sep = " and ")
        if playerValue > 21:
            print("Busted")
            playerBusted = True
            done = True
    print("Dealer go!")
    while dealerDone == False and playerBusted != True:
        CalculateHand(dealerHand,dealerValue)
        print("Dealer has")
        print(*dealerHand, sep = " and ")
        time.sleep(.5)
        if dealerValue > 21:
            print("dealer busted")
            dealerDone = True
            dealerBusted = True
        elif dealerValue >= 17:
            dealerDone = True
        else:
            dealing = rand.choice(deck)
            deck.remove(dealing)
            dealerHand.append(dealing)
    CalculateHand(dealerHand,dealerValue)
    CalculateHand(playerHand,playerValue)
    if playerBusted:
        print("Player busted! Dealer won!")
    elif dealerBusted:
        print("Dealer busted! Player won!")
    else:
        if dealerValue > playerValue:
            print("Dealer has higher score! Dealer wins!")
        elif dealerValue == playerValue:
            print("tie")
            tie = True
        else:
            print("Player has higher score! Player wins!")
            won = True
    if won == True:
        coins = bet * 2
    elif tie == True:
        pass
    else:
        coins = coins - bet
    print(coins)
    while choiceOk == False:
        try:
            choice = int(input("1 to stop playing 2 to keep playing: "))
            if coins == 0:
                print("No more money to bet.")
                done_playing = True
                choiceOk = True

            elif (choice == 1 and done_playing == False):
                done_playing = True
                choiceOk = True
            else:
                pass
            reset()
        except:
            pass
