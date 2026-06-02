'''
Tuple is One of the 4 in built data type of python .
It is used to store a collection of ordered , unchangable , duplicate values .
'''
firstTuple=("India","China","England","India")
print(firstTuple)

singleValueTuple=(1,) #To define a Tuple with a single value . after the value put a single comma . Otherwise the type would be int.
print(type(singleValueTuple))

'''
To Change the Value in Tuple . Existing Tuple  can't be changed new tuple has to be created
We Can Change the tuple to list . in the list we can modify . and again covert the list back to tuple.
'''
myTuple=(1,2,3)
print(id(myTuple)) # id() is a built in function used to get the unique identity of an object.
convertedList=list(myTuple)
convertedList.append(4)
myTuple=tuple(convertedList) #Here Python Creates a new tuple myTuple. Old Tuple is changed to garbage value . id of both myTuple is different.
print(myTuple,id(myTuple))