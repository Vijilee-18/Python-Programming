limit=int(input("Enter the Count of numbers :"))
list=[]
for i in range(limit):
    element=int(input("Enter the Element :"))
    list.append(element)

duplicateRemovedList=[]
for listElement in range(len(list)):
    if list[listElement] not in duplicateRemovedList:
        duplicateRemovedList.append(list[listElement])

print(f"The Original List : {list}")
print(f"Duplicates Removed List :{duplicateRemovedList}")
