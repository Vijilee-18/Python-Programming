limit=int(input("Enter the Count of Numbers :"))
list=[]
for i in range(limit):
    element=int(input("Enter the Element :"))
    list.append(element)

#Largest Element from the list
largestElement=max(list)
print(f"Largest Element from the List :{largestElement}")

#Second Largest 
secondLargestElement=0
for secondLargest in list:
    if secondLargest>secondLargestElement and secondLargest!=largestElement:
        secondLargestElement=secondLargest
print(f"The Second Largest Element from the List :{secondLargestElement}")
