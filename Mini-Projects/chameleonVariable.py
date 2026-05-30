'''
This is a Simple Fun Mini-Project That Uses global Keyword to Increase the Scope of a variable outside the function .

'''

myColor="Green"
def colorChanging():
    global myColor
    myColor=input("To Which Color Do I Have To Change : ")

print(f"Hi I am a Chameleon (In Kerala We Say Onth) . Now I am Having a Color of {myColor} .")
colorChange=input("Would You Like To Change My Color ? (YES/NO) :").upper();
if colorChange=="YES":
    colorChanging()
    print(f"Oh Yeah You Have Changed My Color To {myColor} .")
else:
    print(f"ThankYou For Not Changing My Color .")