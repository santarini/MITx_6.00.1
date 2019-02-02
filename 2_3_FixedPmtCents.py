balance = 201610
annualInterestRate = 0.15

#define some preliminary stuff
totalPaid = 0
monthlyInterestRate = annualInterestRate/12.0

#define some bounds
lowerBound = balance / 12
lowerBound = round(lowerBound, 2)
ear = (1 + monthlyInterestRate)**12
upperBound = (balance * ear)/12.0
upperBound = round(upperBound, 2)

#figure out the 12 month ending compounded balance
for i in range(1,13):
    balance = balance * (1+monthlyInterestRate)

while totalPaid != balance:
    #reset total paid
    totalPaid = 0
    #figure out the distance of the bounds
    distanceBetweenBounds = round(upperBound,2) - round(lowerBound,2)
    if distanceBetweenBounds == 0:
        print(round(upperBound, 2))
        break
    print("Upper: " +str(upperBound) + " Lower: " + str(lowerBound))
    print("Distance between bounds " +str(distanceBetweenBounds))
    #find the mid point between them
    middleOfBounds = distanceBetweenBounds/2
    print("Mid of bounds " +str(middleOfBounds))
    #get the nubmer in the middle of them
    pmtInMiddle = lowerBound + middleOfBounds
    print("Mid of bounds " +str(pmtInMiddle))
    #set that equal to our fixed pmt
    fixedPayment = pmtInMiddle
    print("Fixed Payment " +str(fixedPayment))
    for i in range(1,13):
        totalPaid = totalPaid + fixedPayment
        totalPaid = totalPaid * (1+monthlyInterestRate)
    print("Total Paid:" + str(totalPaid))
    print("Balance:" + str(balance))
    if round(totalPaid,2) < round(balance, 2):
        #set lower bound to pmtInMiddle and reset
        lowerBound = fixedPayment
    if round(totalPaid,2) > round(balance, 2):
        #set upper bound to pmtInMiddle and reset
        upperBound = fixedPayment
    if round(fixedPayment, 2) == round(balance, 2):
        print(round(fixedPayment, 2))
        
##############
balance = 201610; annualInterestRate = 0.15

print("************")
#define some preliminary stuff
totalPaid = 0

#monthly interest rate
monthlyInterestRate = annualInterestRate/12
#monthlyInterestRate = round(monthlyInterestRate, 3)
print("Monthly Interest Rate: " + str(monthlyInterestRate))

#define some bounds
#lower bound
lowerBound = balance / 12
#lowerBound = round(lowerBound, 4)
print("Lower Bound: " + str(lowerBound))

#upper bound
ear = (1 + monthlyInterestRate)**12
upperBound = (balance * ear)/12.0
#upperBound = round(upperBound, 4)
print("Upper Bound: " + str(upperBound))

#figure out the 12 month ending compounded balance
for i in range(1,13):
    balance = balance * (1+monthlyInterestRate)
#balance = round(balance, 4)
print("Balance: " + str(balance))

#scale the balance
balance = balance * 1000
print("Scaled Balance: " + str(balance))

#scale our bounds by 1000 to move the up 3 decimal places
upperBound = upperBound * 1000
lowerBound = lowerBound * 1000
print("Scaled Upper Bound: " + str(upperBound))
print("Scaled Lower Bound: " + str(lowerBound))

#check if pmt eventually equals balance 
j = 1
while totalPaid != balance:
    print("************" + str(j))
    totalPaid = 0
    #find the distance between our bounds
    print("Scaled Upper Bound: " + str(upperBound))
    print("Scaled Lower Bound: " + str(lowerBound))
    distanceBetweenBounds = upperBound - lowerBound
    if distanceBetweenBounds < 0:
        print("Fixed Payment: " + str(round(midPoint/1000,2)))
        break
    #find the number in between our bounds
    midPoint = (upperBound + lowerBound)/2
    print("Distance Between Bounds: " + str(distanceBetweenBounds))
    print("Midpoint: " + str(midPoint))
    #test if midpoint equals our balance after 12 years
    for i in range(1,13):
        totalPaid = totalPaid + (midPoint)
        totalPaid = totalPaid * (1+monthlyInterestRate)
    print("Total Paid: " + str(totalPaid))
    print("Scaled Balance: " + str(balance))
    print("Error: " + str(balance - totalPaid))
    #if total paid less than our blance
    if totalPaid < balance:
        #change the midpoint to our lower bound
        lowerBound = midPoint
    #if it is more than our blanace
    if totalPaid > balance:
        #change the midpoint to our upper bound
        upperBound = midPoint
    if totalPaid == balance:
        print("Fixed Payment: " + str(round(midPoint/1000,2)))
        break
    j+=1

###################
#define some preliminary stuff
totalPaid = 0

#monthly interest rate
monthlyInterestRate = annualInterestRate/12
#monthlyInterestRate = round(monthlyInterestRate, 3)

#define some bounds
#lower bound
lowerBound = balance / 12
#lowerBound = round(lowerBound, 4)


#upper bound
ear = (1 + monthlyInterestRate)**12
upperBound = (balance * ear)/12.0
#upperBound = round(upperBound, 4)

#figure out the 12 month ending compounded balance
for i in range(1,13):
    balance = balance * (1+monthlyInterestRate)

#balance = round(balance, 4)


#scale the balance
balance = balance * 1000

#scale our bounds by 1000 to move the up 3 decimal places
upperBound = upperBound * 1000
lowerBound = lowerBound * 1000

#check if pmt eventually equals balance 
j = 1
while totalPaid != balance:
    totalPaid = 0
    #find the distance between our bounds
    distanceBetweenBounds = upperBound - lowerBound
    if distanceBetweenBounds < 0.01:
        print("Fixed Payment: " + str(round(midPoint/1000,2)))
        break
    #find the number in between our bounds
    midPoint = (upperBound + lowerBound)/2
    #test if midpoint equals our balance after 12 years
    for i in range(1,13):
        totalPaid = totalPaid + (midPoint)
        totalPaid = totalPaid * (1+monthlyInterestRate)
    #if total paid less than our blance
    if totalPaid < balance:
        #change the midpoint to our lower bound
        lowerBound = midPoint
    #if it is more than our blanace
    if totalPaid > balance:
        #change the midpoint to our upper bound
        upperBound = midPoint
    if totalPaid == balance:
        print("Fixed Payment: " + str(round(midPoint/1000,2)))
        break
    j+=1

#passed!
