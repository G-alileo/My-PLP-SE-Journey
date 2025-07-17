# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
if marks >= 70 and marks <= 100:
    print("Grade: Distinction 🏆")
elif marks >= 60 and marks < 70:
    print("Grade: Credit 🎖️")
elif marks >= 50 and marks < 60:
    print("Grade: Pass 👍")
elif marks < 50 and marks >= 0:
    print("Grade: Fail ❌")
else:
    print("Invalid marks entered! Please enter a number between 0 and 100. 🚫")