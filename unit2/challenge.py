password = input("Enter your password: ")

password.strip()

hintA = password[0]
hintB = password[-1]

print(f"Your password hint: it starts with {hintA.upper()} and ends with {hintB.upper()}")