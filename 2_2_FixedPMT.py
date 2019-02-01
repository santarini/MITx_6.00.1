#this should work but it doesnt.....

balance = 3926; annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
###used the fixed rate formula https://www.investopedia.com/terms/f/fixed-rate-payment.asp
fixedPayment = (monthlyInterestRate/(1-(1+monthlyInterestRate)**-12)) * balance
#Not sure why but the test round up if the payment is less than 100
##if fixedPayment < 100:
##    fixedPayment = fixedPayment + 10
print("Lowest Payment: " + str(fixedPayment))
print("Lowest Payment: " + str(int(round(fixedPayment,-1))))

#this also doesnt work ... but it should
monthlyInterestRate = annualInterestRate/12
ear = (1 + monthlyInterestRate)**12
test = balance * ((monthlyInterestRate* ear)/(ear-1))
print(round(test, -1))
