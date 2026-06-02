print("Welcome To Basic Python Quiz Compettion")
choice=input("Would you like to start  (Yes/No) :").upper()
if choice=="YES":
    correctAnswerCount=0
    wrongAnswerCount=0
    answerMap=0
    print("There is a Total of 7  Question")
    qusetion1=input("Is Python an Interpreter or Complier Language :").upper()
    question2=input("Do Python Considers the Identation (YES/NO):").upper()
    question3=input("Do We Need to Explicitly Declare the Data type of a variable  in python (YES/NO):").upper()
    question4=input("Which is correct way to get the datatype of a variable type OR typeof :").upper()
    question5=input("Can a complex type variable converted into any other numeric type (YES/NO):").upper()
    question6=input("Is List Mutable or Immutable :").upper()
    question7=input("Pick the odd one (list , tuple ,set,dictionary,int) :").upper()
    questionList=[qusetion1,question2,question3,question4,question5,question6,question7]
    answerList=["INTERPRETER","YES","NO","TYPE","NO","MUTABLE","INT"]

    for answer in questionList:
        if answer==answerList[answerMap]:
            correctAnswerCount +=1
            answerMap +=1
        else:
            wrongAnswerCount+=1
            answerMap+=1
    print(f"Out of 7 Question You Got {correctAnswerCount} right and {wrongAnswerCount} wrong")
elif choice=="NO":
    print("Then why do you came...")
else:
    print("Enter a Valid Option (YES/NO)")