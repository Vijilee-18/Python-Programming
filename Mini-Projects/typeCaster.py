value=int(input("Enter a Numeric Value :"))
choice=True
while choice:
    print("--Type Caster--")
    print("1.To Sting Data Type")
    print("2.To Float Data Type")
    print("3.Exit")
    choiceValue=int(input("Enter Your Choice :"))
    if choiceValue==1:
        stringType=str(value)
        print(f"Type Casted to String Successfull... Type :{type(stringType)}")
    elif choiceValue==2:
        floatType=float(value)
        print(f"Type Casted to Float Successfull... Type :{type(floatType)}")
    elif choiceValue==3:
        print("Thank You...")
        choice=False
    else:
        print("Invalid Choice...!!!")
    

