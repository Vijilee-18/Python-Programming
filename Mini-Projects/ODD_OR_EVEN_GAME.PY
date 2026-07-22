# ODD OR EVEN GAME
import random 

def playerbatting():
    score=0
    NOT_OUT=True
    while NOT_OUT:
        runs=int(input("Choose a run Between 1 and 6 :"))
        bowlingPrediction=random.randint(1,6)
        print(f"System Predicted Value {bowlingPrediction} .")
        if runs>=1 and runs<=6:
            if runs !=bowlingPrediction:
                score += runs
                print(f"Live Scoreboard : {score}")
            else:
                NOT_OUT=False
                return score
def systemBatting():
    score=0
    NOT_OUT=True
    while NOT_OUT:
        runs=int(input("Choose a run Between 1 and 6 :"))
        bowlingPrediction=random.randint(1,6)
        print(f"System Predicted Value {bowlingPrediction} .")
        if runs>=1 and runs<=6:
            if runs !=bowlingPrediction:
                score += bowlingPrediction
                print(f"Live Scoreboard : {score}")
            else:
                NOT_OUT=False
                return score
def playerBowling(battingScore):
    score=0
    NOT_OUT=True
    while NOT_OUT and score<battingScore:
        runs=int(input("Choose a Number Between 1 and 6 :"))
        bowlingPrediction=random.randint(1,6)
        print(f"System Predicted Value {bowlingPrediction} .")
        if runs>=1 and runs<=6:
                if runs !=bowlingPrediction:
                    score += bowlingPrediction
                    print(f"Live Scoreboard : {score}")
                else:
                    NOT_OUT=False
                    return score
        else:
            print("Choose Number only between 1 and 6 !!!")
    return score

def systemBowling(battingScore):
    score=0
    NOT_OUT=True
    while NOT_OUT and score<battingScore:
        runs=int(input("Choose a Number Between 1 and 6 :"))
        bowlingPrediction=random.randint(1,6)
        print(f"System Predicted Value {bowlingPrediction} .")
        if runs>=1 and runs<=6:
                if runs !=bowlingPrediction:
                    score += runs
                    print(f"Live Scoreboard : {score}")
                else:
                    NOT_OUT=False
                    return score
        else:
            print("Choose Number only between 1 and 6 !!!")
    return score
            
    
            
TOSS=["HEADS","TAILS"]
BATTING_BOWLING=["BAT","BOWL"]
tossUserSelection=input(f"Choose Between {TOSS} :").upper()
tossPrediction=random.choice(TOSS)
if tossUserSelection=="HEADS" or tossUserSelection=="TAILS":
    if tossUserSelection==tossPrediction:
        print("You Have Won the toss .")
        batOrBowlChoice=input(f"Choose between {BATTING_BOWLING} :").upper()
        if batOrBowlChoice=="BAT":
            print("Your Batting...")
            battingScore=playerbatting()
            print("----------------------------------------------")
            print(f"|You have a total of {battingScore} to defend .|")
            print("----------------------------------------------")
            print("Your Bowling...")
            scoreDefended=playerBowling(battingScore)
            if scoreDefended<battingScore:
                print(f"You have won by {battingScore-scoreDefended} runs")
            else:
                print("You have lost...")
        else:
            print("Your Bowling...")
            scoreToChase=systemBatting()
            print("------------------------------------------------")
            print(f"|You have a Total of {scoreToChase} runs to chase .|")
            print("------------------------------------------------")
            print("Your Batting ...")
            scoreChased=systemBowling(scoreToChase)
            if scoreToChase>scoreChased:
                print(f"You have Lost by {scoreToChase-scoreChased}")
            else:
                print("Congrats You have Won")
    else:
        print(f"System Predicted {tossPrediction}")
        batOrBowlChoice=random.choice(BATTING_BOWLING)
        print(f"System has Elected To {batOrBowlChoice} first .")
        if batOrBowlChoice=="BAT":
            print("Your Bowling...")
            scoreToChase=systemBatting()
            print("------------------------------------------------")
            print(f"|You have a Total of {scoreToChase} runs to chase .|")
            print("------------------------------------------------")
            print("Your Batting ...")
            scoreChased=systemBowling(scoreToChase)
            if scoreToChase<scoreChased:
                print("Congrats You have Won")
            else:
                print(f"You have Lost by {scoreToChase-scoreChased}")
        else:
            print("Your Batting ...")
            battingScore=playerbatting()
            print("------------------------------------------------")
            print(f"|You have a total of {battingScore} to defend .|")
            print("------------------------------------------------")
            print("Your Bowling...")
            scoreDefended=playerBowling(battingScore)
            if scoreDefended<battingScore:
                print(f"You have won by {battingScore-scoreDefended} runs")
            elif scoreDefended==battingScore:
                print("Game ended in tie .")
            else:
                print("You have lost...")
else:
    print(f"Choose Only between {TOSS} !!!")
