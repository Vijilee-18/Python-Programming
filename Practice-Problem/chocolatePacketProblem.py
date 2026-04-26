'''
Description : A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. 
              The task is to find the empty packets(0) of chocolate and push it to the end of the array.
Example :
         Input :
                8  – Value of N
                [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline
         Output :
                 4 5 1 9 5 0 0 0
'''

def chocolatePacketCalculation(noPacket):
    packetList=[]

    for i in range(noPacket):
        countInPackage=int(input(f"Enter the Count of Chocolates in Packet_{i+1} :"))
        packetList.append(countInPackage)
    nonEmptyPacket=[]
    emptyPacket=[]

    for i in packetList:
        if i != 0:
            nonEmptyPacket.append(i)
        else :
            emptyPacket.append(i)

    nonEmptyPacket.extend(emptyPacket)
    for i in nonEmptyPacket:
        print(i,end=" ")
chocolatePacket=int(input("Enter the Number of Chocolate Packet's :"))
chocolatePacketCalculation(chocolatePacket)
