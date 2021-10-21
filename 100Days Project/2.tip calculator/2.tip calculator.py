print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill?"))
price = (bill * ((100 + tip) / 100)) / people
# final_amount = round(price, 2)
final_amount = "{:.2f}".format(price)  # turn to str and abiding the format
print(f"Each person should pay: ${final_amount}")
