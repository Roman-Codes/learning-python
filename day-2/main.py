print("Welcome to the tip calculator")
bill = float(input("What was the bill?"))
tip = (input("What percent of top you want to give? 10, 12 or 15?"))
num_of_people = int(input("How many people split the bill?"))

tip_rate = float('1.' + tip)

bill_with_tip = bill * tip_rate

bill_per_person = bill_with_tip / num_of_people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay {final_amount} dollars.")