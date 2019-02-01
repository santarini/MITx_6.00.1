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
