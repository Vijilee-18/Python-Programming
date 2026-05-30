'''
global keyword is used to create a scope for a variable outside its function.
'''
var="I am The Variable From Outside the Function."
def globalKeyword():
    global var
    var="I am The Variable From Inside The Function."
globalKeyword()
print(var) 

'''
Here the Value of Variable Var has been Overwritten by the function which is having a global declaration of same variable .
'''