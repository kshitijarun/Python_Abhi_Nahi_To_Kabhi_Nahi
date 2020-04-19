# Fix the mistakes in this code and test based on the description below
# If I enter 2.00 I should see the message "Tax rate is: 0.07" 
# If I enter 1.00 I should see the message "Tax rate is: 0.07" 
# If I enter 0.50 I should see the message "Tax rate is: 0" 

#price = input('how much did you pay? ') {Gets input in String}
price=float(input())

if price >= 1.00: #Missing symbol '='
	tax = .07
#else {Missing Symbol ':'}
else:
	tax = 0
print('Tax rate is: ' + str(tax))