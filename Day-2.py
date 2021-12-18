print("Welcome to the tip calculator")
Bill = int(input("What was the total bill?"))
People = int(input("How many people to split the bill?"))
tippercentage = int(input("How many percent tip would u like to give?"))
Bill = Bill+(Bill*tippercentage/100)
billperperson = Bill/People
final_amount = round(billperperson, 2)
print(f"Each person should pay : ${final_amount}")