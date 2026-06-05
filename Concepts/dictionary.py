'''
Dictionaires are used to store data values in key:value pairs.
Its an Ordered , Changable ,No duplication allowed collection.
'''
firstDict={
    "Name":"Gustavo Fring",
    "Age":54,
    "Drug Dealear":True,
    "OwnerShip":"Los Pollos Hermanos"
}
print(firstDict)

'''
Accessing Items of Dictionary.
We Can refer the Key name in a square bracket to access. 
get() is a method used to get the value of an item.
keys() is a method that returns a list conatining all the keys of the dictionary.
values() is a method that returns a list containing all values of the dictionary.
items() is a method that returns a list conatining tuples of keys and values .
'''
name,Age=firstDict["Name"],firstDict["Age"]
print(name,Age)

getName=firstDict.get("Name")
getOwnerShip=firstDict.get("OwnerShip")
print(getName,getOwnerShip)

allKeys=firstDict.keys()
print(allKeys)
allValues=firstDict.values()
print(allValues)

allItems=firstDict.items()
print(allItems)

'''
To Change Values
We can change values of specific item by reffering to its key name.
update() method will update the dictionary with items from given argument . Argument must be a dictionary or an iterable object.
'''
firstDict["Drug Dealear"]=False
print(firstDict)
firstDict.update({"Name":"Gus"})
print(firstDict)

'''
To add items
done by using a new index key and assigning a value to it.
'''
firstDict["Death Reason"]="Dead by a Bomb Explostion"
print(firstDict)

'''
To Remove items 
pop() method removes the item with the specified key name.
popitem() method removes the last inserted item.
'''
firstDict.pop("Death Reason")
print(firstDict)
firstDict.popitem()
print(firstDict)

#clear() removes all items and values from dictionary results {}
firstDict.clear()
print(firstDict)
#del completely deletes the dictionary
del firstDict
print(firstDict)