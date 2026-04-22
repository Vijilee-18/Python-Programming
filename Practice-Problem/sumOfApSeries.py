'''Author : Vijilee George Kurian
   Description : Sum of an Arithmetic Series
   Example:
   Input : n=8,a=2,d=5
   Output : 156
'''
def arithmeticProgressionSeries(countOfNumber,firstElement,commonDifference):
    sumOfSeries=firstElement
    series=firstElement
    for i in range(1,countOfNumber):
        series += commonDifference
        sumOfSeries +=series
    print(f"Sum of the Series :{sumOfSeries}")
    
countOfNumber=int(input('Count of Numbers in the Arithmetic Progression:'))
firstElement=int(input("Enter the First Element :"))
commonDifference=int(input("Enter the Common Difference :"))
arithmeticProgressionSeries(countOfNumber,firstElement,commonDifference)