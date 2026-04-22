'''Author :Vijilee George Kurian 
   Description : Palindrome Numbers within a Range 
   Example 1:
   Input :Starting Range =10 , Max Range =50
   Output : 11,22,33,44
'''

def palindromeOrNot(element):
    dummyElement=element
    reversedNumber=0

    while dummyElement !=0:
        digit=dummyElement%10
        reversedNumber=(reversedNumber*10)+digit
        dummyElement=dummyElement//10
    if reversedNumber==element:
        return True
    
startingRange=int(input("Enter the Starting Range :"))
endingRange=int(input("Enter the Finishing Range :"))
for elements in range(startingRange,endingRange+1):
    result=palindromeOrNot(elements)
    if result:
        print(elements)

