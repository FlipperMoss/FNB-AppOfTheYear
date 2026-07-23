# ==========================================
# 1. INITIALIZE DATA STRUCTURES
# ==========================================
students = [
    {"name": "oba", "math": 65, "english": 75, "science": 90},
    {"name": "tumi", "math": 54, "english": 32, "science": 43},
    {"name": "ike", "math": 43, "english": 12, "science": 64},
    {"name": "thato", "math": 12, "english": 43, "science": 65},
    {"name": "phumi", "math": 65, "english": 65, "science": 54}
]

# List to build out with processed individual results
results = []

# Tracker variables for class-wide statistics
total_class_marks = 0
total_subjects_count = 0
highest_mark = -1
lowest_mark = 101

# ==========================================
# 2. MAIN LOOP: CALCULATE AVERAGES AND GRADES
# ==========================================
for student in students:
    # Extract name and numeric marks
    name = student["name"]
    math_mark = student["math"]
    eng_mark = student["english"]
    sci_mark = student["science"]
    
    # Calculate individual student metrics
    student_total = math_mark + eng_mark + sci_mark
    student_avg = student_total / 3
    
    # Accumulate class data for final statistics
    total_class_marks += student_total
    total_subjects_count += 3
    
    # Track overall highest and lowest marks across all individual tests
    for mark in [math_mark, eng_mark, sci_mark]:
        if mark > highest_mark:
            highest_mark = mark
        if mark < lowest_mark:
            lowest_mark = mark
            
    # Apply Unit 5 Grade & Status Logic
    if student_avg >= 80:
        grade = "A"
    elif student_avg >= 70:
        grade = "B"
    elif student_avg >= 60:
        grade = "C"
    elif student_avg >= 50:
        grade = "D"
    else:
        grade = "F"
        
    status = "Pass" if student_avg >= 50 else "Fail"
    
    # Build the dictionary and append to results list
    student_report = {
        "name": name,
        "average": student_avg,
        "grade": grade,
        "status": status
    }
    results.append(student_report)

# ==========================================
# 3. POST-LOOP CLASS STATISTICS
# ==========================================
class_average = total_class_marks / total_subjects_count

# ==========================================
# 4. DISPLAY FORMATTED CLASS REPORT
# ==========================================
print("\n" + "=" * 65)
print(f"{'INDIVIDUAL CLASS REPORT':^65}")
print("=" * 65)
print(f"{'NAME':<15} | {'AVERAGE':<12} | {'GRADE':<10} | {'STATUS':<12}")
print("-" * 65)

for report in results:
    print(f"{report['name'].capitalize():<15} | {report['average']:<12.2f} | {report['grade']:<10} | {report['status']:<12}")

print("=" * 65)
print(f"{'CLASS SUMMARY STATISTICS':^65}")
print("=" * 65)
print(f"Class Average Metric:  {class_average:.2f}%")
print(f"Highest Single Mark:   {highest_mark}%")
print(f"Lowest Single Mark:    {lowest_mark}%")
print("=" * 65 + "\n")

# ==========================================
# 5. WHILE LOOP: INTERACTIVE SEARCH INTERFACE
# ==========================================
print("--- Student Search Interface Active ---")
while True:
    search_query = input("Enter a student's name to look up records (or type 'exit' to quit): ")
    search_query = search_query.strip().lower()
    
    if search_query == "exit":
        print("Closing report search engine. Goodbye!")
        break
        
    # Search for structural matches inside the results profile
    match_found = None
    for report in results:
        if report["name"] == search_query:
            match_found = report
            break
            
    if match_found:
        print("\n" + "-" * 40)
        print(f"Match found for: {match_found['name'].capitalize()}")
        print(f"Term Average:    {match_found['average']:.2f}%")
        print(f"Final Grade:     {match_found['grade']}")
        print(f"Academic Status: {match_found['status']}")
        print("-" * 40 + "\n")
    else:
        print(f"\nError: No record matching '{search_query}' found in our system.\n")

    


