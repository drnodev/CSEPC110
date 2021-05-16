""" 
File:meal_price_calculator.py
Author: NO

Purspose:  Compute the price of a meal as follows by asking for the price of child and adult meals, 
the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. 
Then, ask for the payment amount and compute the amount of change to give back to the customer.
"""

child_price     = float(input("What is the price of a child's meal? "))
adult_price     = float(input("What is the price of an adult's meal? "))
child_number    = int(input("How many children are there? "))
adult_number    = int(input("How many adults are there? "))
tax_rate        = float(input("What is the sales tax rate? "))
subtotal        = (child_number * child_price) + (adult_number * adult_price)
sales_tax       = subtotal * (sales_tax / 100)
total           = subtotal + sales_tax

#print results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

payment         = float(input("What is the payment amount? "))

print(f"Change: ${payment-total}") 


yes_no = input("Did you enjoy your meal? (Y/N) ")
starts = int(input("Give us your opinion, how many stars would you give to this restaurant? "))

print(f"The customer rated the restaurant with {starts} stars")
print(f"The customer enjoyed his meal: {yes_no}")