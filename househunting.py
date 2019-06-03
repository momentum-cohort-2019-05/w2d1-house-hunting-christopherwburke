portion_down_payment = 0.25

current_savings = 0

r = (.04/12)

#ask input for annual_salary , savings_rate, and cost_of_home

annual_salary=int(
    input("What is your annual salary? "))

savings_rate=float(input("What percentage of your annual salary will you save each month? Answer in the form of a decimal. "))

cost_of_home=int(input("How expensive is your dream home? "))

#Down Payment Amount = portion_down_payment * total_cost

down_payment = portion_down_payment * cost_of_home

### monthly_savings = annual salary /12 * savings rate ###

monthly_savings = (annual_salary / 12) * savings_rate

months = 0

while (current_savings < down_payment):
    current_savings = current_savings + ((current_savings + monthly_savings)*r)
    months=months+1
    print(months)