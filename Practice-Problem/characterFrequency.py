def maxMinCount(string):
    if string:
        maxCount=0
        minCount=string.count(string[0])
        maxOccurenceCharacter=""
        minOccurenceCharacter=""
        nonRepeatingCharacter=""
        for i in string:
            stringCount=string.count(i)
            if stringCount==1:
                if nonRepeatingCharacter=="":
                    nonRepeatingCharacter =i
                else:
                    continue
            if stringCount>=maxCount:
                maxCount=stringCount
                maxOccurenceCharacter=i
            if stringCount<=minCount:
                minCount=stringCount
                minOccurenceCharacter=i
        print(f"The Most Repeated Character is {maxOccurenceCharacter} . Least Repeated Character is {minOccurenceCharacter} . Non Repeated Character is {nonRepeatingCharacter}.")
    else:
        print("Enter a String")
inputString=input("Enter a String :").upper()
maxMinCount(inputString)
