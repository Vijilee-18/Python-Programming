'''
Author : Vijilee George Kurian
Description : Finding the Largest and Smallest Digit of a Number
Example :
Input : N=23004
Output : Largest Digit : 4 and Smallest digit :0
'''
def maxAndMin(num):
    largestDigit=num%10
    smallestDigit=num%10
    while num !=0:
        digit=num%10
        if largestDigit<digit:
            largestDigit=digit
        if smallestDigit>digit:
            smallestDigit=digit
        num=num//10
    print(f"Largest Digit :{largestDigit} and Smallest Digit :{smallestDigit}")
num=int(input("Enter a Number :"))
maxAndMin(num)