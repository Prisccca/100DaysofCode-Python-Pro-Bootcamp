print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = (tip / 100)
bill_plus_tip = bill * tip_percent
total_bill = bill_plus_tip + bill
should_pay = total_bill / people
final_amount = round(should_pay, 2)
print(f"Each person should pay:${final_amount}")
