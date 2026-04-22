'''
Description : To Check Wheather a Number is Abundant or Not
Example :
Input: 18
Output: Abundant Number
Explanation: Divisors of 18 are 1,2,3,6,9. 
1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

'''
def abundantOrNot(num):
    list=[]
    for i in range(1,num):
        if num%i==0:
            list.append(i)
    listSum=sum(list)
    if listSum>num:
        print("Abundant Numer")
    else:
        print("Not Abundant Number")
num=int(input("Enter a Number :"))
abundantOrNot(num)