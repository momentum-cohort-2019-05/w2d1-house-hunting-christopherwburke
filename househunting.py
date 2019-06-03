# househunting assignment

#solve for how many months needed to save for down payment
#ask input for annual_salary , portion_saved, and total_cost

#Months = Down Payment Amount / portion_saved
#Down Payment Amount = portion_down_payment * total_cost

portion_down_payment = 0.25

current_savings = 0

r = .04

annual_salary = input("What is your annual salary? ")

portion_saved = input("What percentage of your annual salary will you save each month? Answer in the form of a decimal. ")

total_cost = input("How expensive is your dream home? ")

Months = portion_down_payment * total_cost / portion_saved

print(Months)

# current savings at i = 0, 0
# current savings at i = n, (i= n-1) + (annual_salary * portion_saved / 12) + (current_savings * r/12)

# at end of month, 
# i = 0
# while i 

# test for money saved
# keep_going = True
# while keep_going:
# while 
# if current_savings = (total_cost * portion_down_payment):
    #print(Months)
# else 

