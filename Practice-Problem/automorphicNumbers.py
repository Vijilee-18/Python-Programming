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