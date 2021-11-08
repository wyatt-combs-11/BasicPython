'''
Wyatt Combs
This program is intended to calculate the principal and interest portions of a specific monthly payment as well as the remaining amount of the loan and the total interest paid. It also displays these values for every month leading up to the one entered.
'''
loan_amount = 250000.00
loan_term = 360 #30 year loan term converted to months
month_interest_rate = (0.0325 / 12)
monthly_payment = 1088.00
i = 1 #Loop Counter
total_interest = 0

print("--Sample Mortgage Caclulator (30 year term)--")

valid_month = False
while valid_month == False: #'While' loop prompts user until valid input entered for month
  payment_month = int(input("What payment month do you want to check (Enter whole number from 1 to 360)? "))
  if (payment_month > 0) and (payment_month <= 360):
    valid_month = True
  else:
    print("Payment month invalid. Please try again.")

for i in range (1, payment_month + 1): #Loop is false after payment deducted from entered month
    interest_portion = loan_amount * month_interest_rate
    principal_portion = monthly_payment - interest_portion
    loan_amount -= principal_portion #Running total (loan_amount)
    total_interest += interest_portion #Running total (interest)
  
    print("Month: " + str(i) + " Interest: $" + str(round(interest_portion, 2)) + " Principal: $" + str(round(principal_portion, 2)) + " Loan Balance: $" + str(round(loan_amount, 2)) + " Total Interest: $" + str(round(total_interest, 2)))
    i += 1
    
