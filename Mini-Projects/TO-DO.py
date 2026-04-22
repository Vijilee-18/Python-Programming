#To-Do stimulator 

toDoList=[]
choice=True
while choice:
    print('1.Add an Activity ')
    print('2.View the Activities')
    print('3.Delete an Activity')
    print('4.Exit ') 
    optionChoice =int(input("Choose an Option :"))
    if optionChoice ==1:
        activityToAdd=input("Enter the Activity to Add :").lower()
        toDoList.append(activityToAdd)
        print("ACtivity Added Successfully !!!")

    elif optionChoice ==2:
        if len(toDoList)==0:
            print("!!! You Have to Add an Activity before Viewing  it Dump !!!")
        else:
            print(f"Activities To Do are : {toDoList}")

    elif optionChoice==3:
        if len(toDoList)==0:
            print("No Activities is there to be deleted :")
        else:
            print(f"These are the Activities Remaining :{toDoList}")
            activityToDelete=input("Choose the Activity to be Deleted :").lower()  
            if activityToDelete not in toDoList:
                print("Please select an activity you have added from the List")
            else:
                toDoList.remove(activityToDelete)
                print(f"Hurray Activity Reduced , Remaining Activities are :{toDoList}")

    elif optionChoice==4:
        print("Thank You...")
        choice=False

    else:
        print("Choose a Correct identification number ")

        
