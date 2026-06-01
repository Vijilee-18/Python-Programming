'''
Operators are used to perform operations on variables and values .
'''
#Arithmetic Operator 
print(1+2) 
print(1-2)
print(1*2)
print(1/2)   # Returns the Qutient . May or May Not Returns floating values .
print(1%2)   # Modulus Operator returns the Remainder .
print(1//2)  # floor division returns an integer value .

'''
Walrus Operator :=  is used to assign values to a variable as part of a larger Expression .
'''
if name:=input("Enter Your Name"):
    print(name)

listA=[1,2,3,4]
if countOfList:=len(listA) ==4:
    print('Hello...')

'''Ternary Operator
The ternary operator allows  to assign one value if a condition is true, and another if it is false .
'''
age=18
status= "Adult" if age>=18 else "Minor"
print(status)
num=12
oddOrEven="Even" if num%2==0 else "Odd"
print(oddOrEven)

'''IDENTITY OPERATORS 
'is' and 'is not' are the identity operators . 
Identity operators are used to compare the objects, 
not if they are equal, but if they are actually the same object, with the same memory location.
'''
a=1
b=a
print(a is b)
x=[12,3]
y=[12,3]
print(x is y)

'''
Membership Operator 
'in' and 'not in' are the membership operators . 
Used To Check if a sequence is present in an object .
'''
listB=[1,2,3]
print(3 in listB)
string="Vijilee"
print("t" in string)