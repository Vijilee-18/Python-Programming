limit=int(input("Enter the Count of numbers :"))
numbersList=[]
for i in range(limit):
    numbersList.append(int(input("Enter the number :")))

minNumber=min(numbersList)
maxNumber=max(numbersList)

for i in range(minNumber,maxNumber+1):
    if i not in numbersList:
        print(f"Missing Number : {i}")


