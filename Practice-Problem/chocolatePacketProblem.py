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