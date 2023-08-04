# tip calculator with split bill feature
# work done for 100 days of python coursework on udemy
print("Welcome to the Tip Calculator")
bill_total = float(input("What was the total bill?\n"))
tip_percent = int(
    input("What percentage tip would you like to give 10, 12, or 15?\n"))
split_by = int(input("How many people split the bill?\n"))
tip_owed = (bill_total/split_by)*(tip_percent/100)
total_owed = (bill_total/split_by)+tip_owed
rounded_tip = round(tip_owed, 2)
rounded_tip = "{:.2f}".format(rounded_tip)
rounded_total = round(total_owed, 2)
rounded_total = "{:.2f}".format(rounded_total)
print(f"Each person should tip: ${rounded_tip}")
print(f"Each person owes in total: ${rounded_total}")
