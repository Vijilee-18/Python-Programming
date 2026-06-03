studentName={
    "Abhijith Kumar",
    "Abhishek Babu",
    "Abin kailas",
    "Ayul Sanu"
}
studentsPresentInClass={
    "Abhijith Kumar",
    "Abhishek Babu"
}
status=True
while status:
    print("What would you Like To Do .\n1.Display the Total Students Name\n2.Display Name of Students Present in Class\n3.Display Name of Students Absent\n4.Add a Student\n5.Delete a Student.\n6.Exit")
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        print(studentName)
        continueChoice=input("Would You Like to View Anything Else  (Yes/No) :").upper()
        if continueChoice=="NO":
            status=False
    elif choice==2:
        print(studentsPresentInClass)
        continueChoice=input("Would You Like to View Anything Else  (Yes/No) :").upper()
        if continueChoice=="NO":
            status=False
    elif choice==3:
        student=studentName.difference(studentsPresentInClass)
        print(student)
        continueChoice=input("Would You Like to View Anything Else  (Yes/No) :").upper()
        if continueChoice=="NO":
            status=False
    elif choice==4:
        studentAdd=input("Enter the Name of Student to ADD :")
        studentName.add(studentAdd)
        print(studentName)
        continueChoice=input("Would You Like to View Anything Else  (Yes/No) :").upper()
        if continueChoice=="NO":
            status=False
    elif choice==5:
        print(studentName)
        studentDelete=input("Enter Name of Student to be Deleted :")
        studentName.remove(studentDelete)
        print(studentName)
        continueChoice=input("Would You Like to View Anything Else  (Yes/No) :").upper()
        if continueChoice=="NO":
            status=False
    elif choice==6:
        print("ThankYou...")
        status=False
    else:
        print("Enter a Valid Value .")
    