'''
Boolean Type Will be having Two Values either True or False 
'''
print(8==9)
if(1<2):
    print("I am The True Statement")

'''
bool() method is Used to Evaluate any Value and gives Tue or False .
Gives True in majority of Situation Where it has atleast some sort of value.
Gives False When : {} ,[], " " , 0 , 0.0 , False  .
'''
name=input("Enter Your Name :")
if(bool(name)):
    print(f"My Name is {name}")
else:
    print("Please Enter Your Name...")

'''
isinstance() is a method used to check if a variable is of certain data type . 
Gives either True or False .
'''
name="abhi"
print(isinstance(name,str))