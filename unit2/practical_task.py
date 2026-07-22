name = input("Enter your fist name: ")
surname = input("Enter your last name: ")
bio = input("Enter a bio: ")

username = name[0] + surname

print(f"{name.title()} {surname.title()}")
bio.strip()
length = len(bio)
replace = bio.replace("I am", "I'm")

print(f"Your bio is: {bio}")
print(f"Your username is: {username}")
print(f"The bio replacement: {replace}")
print(f"The length of the bio is: {length}")