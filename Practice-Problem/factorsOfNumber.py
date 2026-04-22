'''Author : Vijilee George Kurian
   Description : To Find The Factors Of a Given Number
   Example :
   Input :n=6
   Output :[1,2,3,6]
'''
def factorsOfNum(num):
    listOfFactors=[]
    for i in range(1,num+1):
        if num%i==0:
            listOfFactors.append(i)
    print(f"Factors of {num} :{listOfFactors}")
    
num=int(input('Enter a Number to find the factors :'))
factorsOfNum(num)