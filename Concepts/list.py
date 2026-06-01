# '''
# List are Used to Store Multiple Items in a Single Variable .
# List items are Ordered , Mutable and allow Duplicates .
# Can have any Data Types in a Single List.
# '''

# firstList=[1,"Abhijith","CSE"]
# print(firstList)
# print(type(firstList))
# #Accessing Items From List Using Index .
# print(firstList[-1]) # Negative Indexing of firstList=[-3,-2,-1]
# print(firstList[-3:-1])

# #Changing Value
# secondList=["Apple","Orange","Bananna"]
# secondList[1]="Cherry"
# print(secondList)
# secondList[2:5]=["Kiwi","Jackfruit","Papaya"]
# print(secondList)
# #Inserting a  value without changing the items in the list. insert() method is used.
# secondList.insert(1,"BlueBerry")
# print(secondList)

# #Adding to the end of the list . append() method is used.
# thirdList=[1,2,3,4]
# thirdList.append(True)
# print(thirdList)

# #To Add Elements of One List To Another . extend() method is used.
# fourthlist=['a','b','c']
# fifthList=[True,False,1,"babu"]
# fourthlist.extend(fifthList)
# print(fourthlist)

# # To Remove Elements .use remove() method .
# fourthlist.remove('c')
# print(fourthlist)

# '''
# To Remove from Specified Index . 
# pop()=> without index specifying value will be removed from last.
# del => keyword can also be used to delete an item from a specifed position in the list or even the list .
# clear()=>Used to clear up the items from the list .
# '''
# fourthlist.pop(0)
# print(fourthlist)
# del fourthlist

# '''
# sort() is a method used to sort the list
# '''
# sixthList=[1,3,54,2,0]
# sixthList.sort()
# print(sixthList)

# seventhList=[0,1,2,3]
# seventhList.sort(reverse=True) # to Sort in Descending Order 
# print(seventhList)

eightList=["ousepp","babu",'benny',"chacko",'thankachan','queashi','a','Bijukuttan']
eightList.sort(key=str.lower) #A key =function to use the sort()
print(eightList)