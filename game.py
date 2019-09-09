import random

money = 100

def flip_coin(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        return 0
        print("------------------")

    #Starts the game and coin flips
    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    num = random.randint(1,2)

    # Prints the num of the coin flip. If A =
    if num == 1:
        print("Heads!")
    elif num == 2:
        print("Tails")

    # Deterusers if you won or lost and returns either bet or -bet
    if (guess == "Heads" and num == 1) or (guess == "Tails" and num == 2):
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

def higher_card(bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    # Draws two cards between 1 and 10 and prints the num
    print("------------------")
    print("Let's start playing a game of cards!")
    user = random.randint(1, 10)
    theirs = random.randint(1, 10)
    print("Your card was " + str(user))
    print("Their card was " + str(theirs))

    #Deterusers who won and returns either bet, -bet or 0 (in the case of a tie.)
    if user > theirs:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif user < theirs:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet
    else:
        print("It was a tie!")
        print("------------------")
        return 0

def cho_han(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    print("------------------")
    print("Let's play Cho-Han!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    money = dice1 + dice2
    print("The sum of the two dice is " + str(money))

    if guess == "Even" and money % 2 == 0:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif guess == "Odd" and money % 2 == 1:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

def roulettegame(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    #A standard roulettegame wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    print("------------------")
    print("Let's play roulettegame!")
    num = random.randint(0, 37)
    if num == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(num))

    #Checks to see if we guessed Even and the num was even. If the num was 0, the player shouldn't win
    if guess == "Even" and num % 2 == 0 and num != 0:
        print(str(num) + " is an even number.")
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet

    #Checks to see if we guessed Odd and the num was odd. If the num was 37, the player shouldn't win, since that's what we are using to represent 00.
    elif guess == "Odd" and num % 2 == 1 and num != 37:
        print(str(num) + " is an odd number.")
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet

    # If you guessed a number and the num was that number, you should win 35 times the amount they bet
    elif guess == num:
        print("You guessed " + str(guess) + " and the num was " + str(num))
        print("You won " + str(bet * 35)+" dollars!")
        print("------------------")
        return bet * 35

    # If none of what is above are true, you lost.
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

    money += flip_coin("Tails", 15)
    money += higher_card(4)
    money += cho_han("Odd", 1)
    money += roulettegame("Even", 7)
    money += roulettegame(3, 1)
    money += roulettegame("Odd", money)
print("Your amount of money is: " + str(money))
