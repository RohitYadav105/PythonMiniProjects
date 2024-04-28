# Input marks for each subject
subj1 = float(input("Enter marks for Subject 1: "))
subj2 = float(input("Enter marks for Subject 2: "))
subj3 = float(input("Enter marks for Subject 3: "))
subj4 = float(input("Enter marks for Subject 4: "))
subj5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks and average
total_marks = subj1 + subj2 + subj3 + subj4 + subj5
average_marks = total_marks / 5

# Determine grade based on average marks
if average_marks >= 90:
    grade = "A++"
elif average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B+"
elif average_marks >= 50:
    grade = "B"
elif average_marks >= 40:
    grade = "C"
else:
    grade = "F"

# Display the grade
print("Your grade is:", grade)