name = input("Enter your name")
mark1 = float(input("Enter mark1: "))
mark2 = float(input("Enter mark2: "))
mark3 = float(input("Enter mark3: "))
grade = ''
status = ""
intervention = ""

average = (mark1 + mark2 + mark3) / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
    
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

if mark1 <= 40:
    intervention = "Mark1 Need intervention"
else:
    intervention = ""
    
if mark2 <= 40:
    intervention = "Mark2 Need intervention"
else:
    intervention = ""
    
if mark3 <= 40:
    intervention = "Mark3 Need intervention"
else:
    intervention = ""

print("=== Report Card ===")
print(f"Mark1 is : {mark1}")
print(f"Mark2 is : {mark2}")
print(f"Mark3 is : {mark3}")
print(f"The average is: {round(average,2)}")
print(f"The grade is: {grade}")
print(f"Status is: {status}")
print(intervention)    