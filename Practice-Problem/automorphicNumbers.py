'''
Description : To Check Wheather a Number is Automorphic or not.
A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.
Example :
Input Format: N = 76
Result: Automorphic Number
Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.
'''

def automorphicOrNot(num):
    dummyNum=num
    squareOfNum=num**2
    print(squareOfNum)
    count=0
    while dummyNum!=0:
        count +=1
        dummyNum =dummyNum//10
    divisor=10**count
    dividedSquare=squareOfNum%divisor
    if dividedSquare==num:
        return True

num=int(input("Enter a Number :"))
result=automorphicOrNot(num)
if result:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
