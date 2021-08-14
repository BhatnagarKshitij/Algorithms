#Question: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-sum-0423b95e/



for numberOfTestcases in range(int(input())): #Number Of testcases
    
    lengthOfArray,distinctInteger=list(map(int,input().split(" "))) #Length and distinct Integer
    array=list(map(int,input().split())) #Given Array
        
    if lengthOfArray==0: #Checking Base case
        print(0)

    array.sort(reverse=True) #Sorrting in decending order
    newArray=list() #Creating new Array

    lastValue=None #To store last known value
    tempSum=0 #To store sum of consecutive numbers

    for i in array:
        
        if lastValue is None: #first time loop condition to initialize variables 
            lastValue=i
            tempSum=lastValue
            continue
        
        if i==lastValue: #Checking for consecutive numbers
            tempSum+=i #If same value then add up
        else:
            if tempSum!=0: #Checking if We arent adding null values in array
                newArray.append(tempSum)
            tempSum=i
            lastValue=i
            
    if tempSum!=0: #Checking for leftouts
        newArray.append(tempSum)   


    newArray.sort(reverse=True) #Again sorting (decending)
    lengthOfNewArray=len(newArray)
    maxSum=0

    for i in range(len(newArray)):
        if distinctInteger==0: #Checking for max distinct values
            break
        maxSum=max(maxSum,maxSum+newArray[i])
        distinctInteger-=1
    print(maxSum)

