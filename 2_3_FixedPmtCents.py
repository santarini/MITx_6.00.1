
balance = 320000
annualInterestRate = 0.2

#define some preliminary stuff
totalPaid = 0
monthlyInterestRate = annualInterestRate/12.0
monthlyPmtLower = balance / 12
ear = (1 + monthlyInterestRate)**12
monthlyPmtUpper = (balance * ear)/12.0

#figure out the 12 month ending compounded balance
for i in range(1,13):
    balance = balance * (1+monthlyInterestRate)

#figure out the distance of the bounds
distanceBetweenBounds = monthlyPmtUpper - monthlyPmtLower
#find the mid point between them
middleOfBounds = distanceBetweenBounds/2
#get the nubmer in the middle of them
pmtInMiddle = monthlyPmtLower + middleOfBounds
#set that equal to our fixed pmt
fixedPayment = pmtInMiddle
for i in range(1,13):
    totalPaid = totalPaid + fixedPayment
    totalPaid = totalPaid * (1+monthlyInterestRate)
if totalPaid < balance:
    #set lower bound to pmtInMiddle and reset
if pmtInMiddle > balance:
    #set upper bound to pmtInMiddle and reset


print(pmtInMiddle)

