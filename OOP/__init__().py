'''
__init__() is a special python method that automatically runs when an instance of a class is created.
it basically assign the attribute value to the object .
self parameter  refers to the current object created.
'''

class Student:
    def __init__(self,studentName, studentAge,studentRollNo):
        self.Name=studentName
        self.Age=studentAge
        self.RollNo=studentRollNo
    def display(self):
        print(self.Name)
        print(self.Age)
        print(self.RollNo)

std1=Student("Vijilee George Kurian",19,72)
std1.display()
