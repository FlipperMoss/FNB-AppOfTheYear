name = input("Enter first name: ")
surname = input("Enter surname: ")
age = int(input("Enter your age: "))
fav_num = float(input("Enter your favourite number: "))

print(f"Welcome, {name} {surname}!")
print(name.upper().title())

month = age * 12
print(f"Your age in months is: {month}")
print(round(fav_num, 2))

print(type(name))
print(type(surname))
print(type(age))
print(type(fav_num))
