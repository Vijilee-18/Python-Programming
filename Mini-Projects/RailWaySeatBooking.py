passengerList=[]
seatLeft=True
occupiedSeat=0
maxSeat=2
while seatLeft:
    if occupiedSeat<maxSeat:
        passengerName=input(f"Seat Manager : What is Your Name :")
        passengerEntryPoint=input(f"Your Entry Point :")
        passengerDestination=input(f"Your Destinaton :")
        occupiedSeat +=1
        passengerDeatils=(occupiedSeat,passengerEntryPoint,passengerDestination)
        passengerList.append(passengerDeatils)
        print(f"Your Deatils : {passengerDeatils}")
        print("Have a Nice Journey ...")
    else:
        print("Sorry Seat is Full")
        seatLeft=False
print(passengerList)