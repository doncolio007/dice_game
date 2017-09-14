#!/usr/bin/env python3 -i
import random

def playGame(playerOne, playerTwo):
    assistant = "Would you like to roll the dice? yes/no"
    playIdOne = "1"
    playIdTwo = "2"
    

    def roll():
        min_roll = 1
        max_roll = 6
        dice = random.randint(min_roll, max_roll)
        print("You rolled: %d" % dice)
        return dice

    def scoreBoard(player, score):
        print('Player %s score: %d' % (player, score))
                

    def rollNext(player):
        print("Passing to next player...")
        print("Player %s, Would you like to play? yes/no" % player)
        response = input()
        return response

    def rollDice(playerX,playerY):
        print("Would player %s like to roll the dice? yes/no" % playerX)
        response = input()
        point = 0
        if response == "yes":
           newRoll = roll()
           if newRoll >= 3:
               point = 1
        else:
            reply = rollNext(playerY)
            if reply == "no":
                point = 1
            else:
                newRoll = roll()
                if newRoll >= 3:
                    point = 2
                else:
                    point = -1
        return point

    print(assistant)

    response = input()

    if response == "yes":
        diceRoll = roll()
        if diceRoll < 3:
            scoreBoard(playIdOne,playerOne)
            scoreBoard(playIdTwo,playerTwo)
            gamePoint = rollDice(playIdTwo, playIdOne)
            if gamePoint > 1:
                playerOne = playerOne + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            elif gamePoint == 1:
                playerTwo = playerTwo + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            else:
                playerOne = playerOne + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
        else:
            playerOne = playerOne + 1
            scoreBoard(playIdOne,playerOne)
            scoreBoard(playIdTwo,playerTwo)
            gamePoint = rollDice(playIdTwo, playIdOne)
            if gamePoint > 1:
                playerOne = playerOne + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo) 
            elif gamePoint == 1:
                playerTwo = playerTwo + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            else:
                playerOne = playerOne + gamePoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)


        newRollPoint = rollDice(playIdOne, playIdTwo)
        if newRollPoint > 1:
            playerTwo = playerTwo + newRollPoint
            scoreBoard(playIdOne,playerOne)
            scoreBoard(playIdTwo,playerTwo) 
        elif newRollPoint == 1:
            playerOne = playerOne + newRollPoint
            scoreBoard(playIdOne,playerOne)
            scoreBoard(playIdTwo,playerTwo)
        else:
            playerTwo = playerTwo + newRollPoint
            scoreBoard(playIdOne,playerOne)
            scoreBoard(playIdTwo,playerTwo)
    else:
        response = rollNext(playIdTwo)
        if response == "yes":
            dice = roll()
            # print("You rolled: %d" % dice)
            if dice >= 5:
                playerTwo = playerTwo + 2
                scoreBoard(playIdOne,playerOne) 
                scoreBoard(playIdTwo,playerTwo)
            elif 3 <= dice < 5 :
                playerTwo = playerTwo + 1
                scoreBoard(playIdOne,playerOne) 
                scoreBoard(playIdTwo,playerTwo)
            else:
                playerOne = playerOne + 2
                scoreBoard(playIdOne,playerOne) 
                scoreBoard(playIdTwo,playerTwo)

                
            newRollPoint = rollDice(playIdOne, playIdTwo)
            if newRollPoint > 1:
                playerTwo = playerTwo + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo) 
            elif newRollPoint == 1:
                playerOne = playerOne + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            else:
                playerTwo = playerTwo + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
        else:
            playerOne = playerOne + 1
            scoreBoard(playIdOne,playerOne) 
            scoreBoard(playIdTwo,playerTwo)
            newRollPoint = rollDice(playIdTwo, playIdOne)
            if newRollPoint > 1:
                playerOne = playerOne + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo) 
            elif newRollPoint == 1:
                playerTwo = playerTwo + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            else:
                playerOne = playerOne + newRollPoint
                scoreBoard(playIdOne,playerOne)
                scoreBoard(playIdTwo,playerTwo)
            

    print("Player 1 total score: %d" % playerOne)
    print("Player 2 total score: %d" % playerTwo)

    quality = ['Star','Gem','Diamond','Joker','Geezer']
    options  = ['Kiss','Pat','Shake','Friend','Love','Simply ignore']

    qualifier = random.choice(quality)
    option = random.choice(options)
    if playerOne > playerTwo:
        print("Player 1 is the winner, player 1 is a %s" % qualifier)
    elif playerOne == playerTwo:
        print("Game is a draw, %s each other" % option)
    else:
        print("Player 2 is the winner, player 2 is a %s" % qualifier)


playerA = 0;
playerB = 0;

playGame(playerA, playerB)



    


