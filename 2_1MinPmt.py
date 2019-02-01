#prints each months remaining balance
for i in range(1,13):
    #calculate min pmt
    minimumPayment = balance * monthlyPaymentRate
    #dedcut min pmt from bal
    balance = balance - minimumPayment
    #charge interest on the remaining balance
    monthlyInterest = (balance *(annualInterestRate/12))
    #add the interest to the balance
    balance = balance + monthlyInterest
    #print remaining balance
    print("Month " + str(i) + " Remaining balance: " + str(round(balance, 2)))

#prints single remaining balance at end of year
for i in range(1,13):
    #calculate min pmt
    minimumPayment = balance * monthlyPaymentRate
    #dedcut min pmt from bal
    balance = balance - minimumPayment
    #charge interest on the remaining balance
    monthlyInterest = (balance *(annualInterestRate/12))
    #add the interest to the balance
    balance = balance + monthlyInterest
    #print remaining balance
print("Remaining balance: " + str(round(balance, 2)))

#passed
