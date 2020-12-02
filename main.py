# tip calculator

print("Welcome to the tip calculator")

bill = float(input("What was the total bill ?\n $ ")) 
tip = float(input("What percertage tip would yoo like to give? 10, 12 or 15 ?\n "))
split = int(input("How many people to split the bill ? \n"))

# caluculation the amount 
amount = ((bill * (tip/100))+ bill)/split
msg = round(amount,2)

print(f"Each person should pay $ {msg}")