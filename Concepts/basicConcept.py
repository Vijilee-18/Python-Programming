'''
Python is an interpreter based Programming Language .
Python can be treated in a procedural way , an object oriented way or a functional way.
Used for server-side web development , software development , mathematics , system scripting.
Each of the Programming Instruction is reffered as a statement.
'''

# First Program 
print("Hello World ...") # Used for printing our output .

#various way to print
print("First Printing Statement...",end=" ") # Usually when each print() is called , it is loaded in the new line . To avoid that we use, end=" "
print("Statement 1");print("Statement 2") # Multiple Statement can be used in one line . To Separate the Statement we use semicoloun(;)

#Variables

'''
Variables are containers for storing data values.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
'''
#Example :
age=18
print(age)
print(type(age)) # Type : int
age='Eligible for Driving...' # Changes int -> str
print(age)
print(type(age)) # Type : str

num=str(18) # We can type cast the variable . 
print(num)

name1,name2,name3="abhi","Adhi","alwin" #Can declare different variable in same statement.
print(name1,name2,name3) 

