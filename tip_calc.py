print("Welcome to the tip calculator! 💰")
bill = float(input("What is the total bill? ₹"))
tip = int(input("What percentage of tip would you like to give? 2%, 5%, 10% ?"))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ₹{final_amount}")



