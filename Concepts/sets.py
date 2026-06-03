'''
set is a collection to store multiple items in a single variable.
it is unordered , unindexed, unchangable , no duplicate value .
We can add and remove items from the set .
'''

myset={"messi","ronaldo","neymar"}
print(myset)

myset1={True,False,0,1} # Here True and 1 , False and 0 . are Considered as the same duplicated value . so 0,1 will not be considered.
print(myset1)

'''
To Access an item we cannot use the index . we can loop through the set and find if the item is present or not .
'''
mySet2={"Argentina","Germany","Brazil","Spain"}
for i in mySet2:
    print(i)

'''
To Add items to a set . use add() , update() methods.
'''
set1={1,2,3}
set1.add("Athul") #add() used to add one item to the set.
print(set1)
set2={4,5,6}
set1.update(set2) #update() adds a set,list,dictionary,tuple to an existing set.
print(set1)
list1=["Orange","Pappaya"]
set1.update(list1)
print(set1)

'''
To Remove Item : we can use remove() and discard()
remove() : gives an error if we try to remove item that doesnot exit . whereas discard() doesn't.
'''
mySet2.remove("Spain")
print(mySet2)
mySet2.discard("India") #will not give error
print(mySet2)
set1.clear()
del set1

'''
To Join sets :
union() combines two or more set and returns a new set. 
update() doesnt returns a new set . updates thee current set with another. 
intersection() returns a new set with only items that are in both set .
intersection_update() doesn't return a new set . instead update the exisiting set with duplicate value from other set.
difference() returns a new set containing items of one set which are not in the other set.
difference_update() does the same as difference() but without returing new set.
symmetric_difference() returns a new set with item that are not common in different sets.
'''
unionSet1={1,2,3,4}
unionSet2={5,6,7}
unionSet3=unionSet1.union(unionSet2)
print(unionSet3)
unionSet1.update(unionSet2)
print(unionSet1)

intersectionSet1={"Alwin","Athul"}
intersectionSet2={"Alwin","Baby"}
intersectionSet3=intersectionSet1.intersection(intersectionSet2)
print(intersectionSet3)
intersectionSet1.intersection_update(intersectionSet2)
print(intersectionSet1)

differenceSet1={1,2,3}
differenceSet2={3,4,5}
differenceSet3=differenceSet1.difference(differenceSet2)
print(differenceSet3)
differenceSet1.difference_update(differenceSet2)
print(differenceSet1)

symmetricDifferenceSet1={1,2,3,"Athul"}
symmetricDifferenceSet2={3,4,"babu"}
symmetricDifferenceSet3=symmetricDifferenceSet1.symmetric_difference(symmetricDifferenceSet2)
print(symmetricDifferenceSet3)
symmetricDifferenceSet1.symmetric_difference_update(symmetricDifferenceSet2)
print(symmetricDifferenceSet1)