num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication =  num1 * num2
division = num1 / num2

floor = num1 // num2
modular = num1 % num2

if num2 == 0:
    print("cannot divide with 0")
    
print(f"The addition: {addition}")
print(f"The subtraction: {abs(subtraction)}")
print(f"The multiplication: {round(multiplication, 2)}")
print(f"The division: {round(division, 2)}")
print(f"The floor division: {floor}")
print(f"The modular division: {round(modular, 2)}")
