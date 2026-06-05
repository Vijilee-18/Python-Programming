#Contact List Dictionary
contactList={

}
#Fuction To Save Contact
def saveContact(contactName,contactNumber):
    if contactName and contactNumber:
            contactList.update({contactName:contactNumber})
            print("Contact Added Successfully")
    else:
        print("Please Enter the Contact Name and Number.")
        return 
    
#Fuction to Search Contact  
def searchContact(contactName):
    if contactName:
        if contactName in contactList.keys():
            print(f"Contact Number of {contactName} is {contactList.get(contactName)}")
        else:
            print("Contact Doesn't Exisit")
            choice=input("Would You Like to add this into your Contact (Yes/No) :").upper()
            if choice=="YES":
                contactNumber=int(input("Enter the Contact Number : "))
                saveContact(contactName,contactNumber)
            else:
                return
    else:
        print("Please Enter The Contact Name .")
        return   
 
#Function to Update the Contact
def updateContact():
    contactName=input("Enter the Contact Name to get Updated :").upper()
    if contactName:
        if contactName in contactList.keys():
            whatChoice=input("Would You Like to Change the (Name or Number or both) :").upper()
            if whatChoice=="NAME":
                newName=input("Enter the New Name :")
                contactList[newName]=contactList.pop(contactName)
                print(f"New Contact {newName} Phone Number {contactList.get(newName)} has been Updated")
            elif whatChoice=="NUMBER":
                newNumber=int(input("Enter the New Number :"))
                contactList[contactName]=newNumber
                print(f"New Contact {contactName} Phone Number {contactList.get(newName)} has been Updated")
            elif whatChoice=="BOTH":
                newName=input("Enter the New Name :")
                newNumber=int(input("Enter the New Number :"))
                contactList[newName]=contactList.pop(contactName)
                contactList[newName]=newNumber
                print(f"New Contact {newName} Phone Number {contactList.get(newName)} has been Updated")
            else:
                print("Choose a valid option (Name or Number or both")
                return
        else:
            print("Contact doesn't exist.")
            return
    else:
        print("Please Enter the Contact Name.")
        return

#Function to Delete Contact
def deleteContact():
    contactName=input("Enter the Contact Name to be deleted :").upper()
    if contactName:
        if contactName  in contactList.keys():
            contactList.pop(contactName)
            print("Contact Deleted Successfully")
        else:
            print("Contact Doesn't Exist")
            return
    else:
        print("Please Enter a Contact Name.")
        return
toContinue=True
while toContinue:
    print("1.Save Contact\n2.Search Contact\n3.Update Contact\n4.Delete Contact\n5.View Full Contact\n6.Exit")
    choice=int(input("Choose an Option :"))
    match choice:
        case 1:
            contactName=input("Enter the Name of Contact :").upper()
            contactNumber=int(input("Enter the Contact Number :"))
            saveContact(contactName,contactNumber)
        case 2:
            contactName=input("Enter the Name of Contact to be Searched :").upper()
            searchContact(contactName)
        case 3:
            updateContact()
        case 4:
            deleteContact()
        case 5:
            print(contactList)
        case 6:
            toContinue=False
        case _:
            print("Enter a Valid Option")        