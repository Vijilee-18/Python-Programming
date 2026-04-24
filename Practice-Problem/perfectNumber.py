def perfectNumberOrNot(num):
    if num<0:
        return False
    else:
        sumOfFactors=0
        for i in range(1,num):
            if num%i==0:
                sumOfFactors +=i
        return sumOfFactors==num

num=int(input("Enter a Number :"))
result=perfectNumberOrNot(num)
if result:
    print("Its a Perfect Number")
else:
    print("Its not a Perfect Number")
        
