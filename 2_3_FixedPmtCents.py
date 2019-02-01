
balance = 320000
annualInterestRate = 0.2


totalPaid = 0
monthlyInterestRate = annualInterestRate/12.0
monthlyPmtLower = balance / 12
ear = (1 + monthlyInterestRate)**12
monthlyPmtUpper = (balance * ear)/12.0

for i in range(1,13):
    balance = balance * (1+monthlyInterestRate)

distanceBetweenBounds = monthlyPmtUpper - monthlyPmtLower
middleOfBounds = distanceBetweenBounds/2
pmtInMiddle = monthlyPmtLower + middleOfBounds

if pmtInMiddle < balance:
    
if pmtInMiddle > balance:
##for i in range(1,13):
##    totalPaid = totalPaid + fixedPayment
##    totalPaid = totalPaid * (1+monthlyInterestRate)
##    #print(str(i)+ " " + str(totalPaid))


print(pmtInMiddle)
