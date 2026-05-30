'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.
Strings in python are array of unicode character.
'''
var="I am a Single Line String"
var2="""
I am a Multi-Line String , 
Suiiii.....
"""
print(var)
print(var2)
print(len(var)) #len() is used to find the length.

name="I am Tony Stark"
if "Stark" in name:       # in keyword is used to check if a character or word is in string. not in also used in vice versa condition. 
    print("I am IronMan")
else:
    print("I am Iron Man From Naptool...")

#String Slicing 
value="Vijilee George Kurian"
print(value[0:7])
print(value[8:])
print(value[:7])

#String Modification
str1="heLlO sir"
print(str1.upper()) # upper() used to convert into upper case letter.
print(str1.lower()) # lower() used to convert into lower case letter.
print(str1.strip()) # strip() used to remove whitespace from end.
print(str1.replace("h","j")) #replace()  used to replace a character with another character.
print(str1.split("l"))
