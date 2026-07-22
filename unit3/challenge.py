kilos = float(input("How many kilomiters do you travel: "))
petrol = float(input("What is the current petrol price: R"))

liters_needed = kilos / 10
total_cost = liters_needed * petrol

print(f"The total cost is: R{round(total_cost, 2)}")