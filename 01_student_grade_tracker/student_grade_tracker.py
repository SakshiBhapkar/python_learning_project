#student grade checker
stud_name=input("Enter your name:")
stud_age=int(input("Enter your age:"))
Maths=int(input("Enter  maths subject marks:"))
English=int(input("Enter  English subject marks:"))
Science=int(input("Enter  Science subject marks:"))
Attendance=int(input("Enter your attendance in percentage:"))

print("Student Result:")
print("Name:",stud_name)
print("Age:",stud_age,"\n\n")


Total_marks=Maths+English+Science
print("Total marks obtained:",Total_marks)
Average_marks=Total_marks/3
print("Average marks obtained:",Average_marks,"\n\n")

#grade

if Average_marks >= 90:
    print("Grade:A+")
elif Average_marks >= 80:
    print("Grade:A")
elif Average_marks >= 70:
    print("Grade:B")
elif Average_marks >= 60:
    print("Grade:C")
elif Average_marks >= 50:
    print("Grade:D")
else:
    print("Grade:F")

#check pass or fail
if Maths >= 35 and English >= 35 and Science >= 35:
    print("Result:Passed")
else:
    print("Result:Failed")

#Eligibility for exam
if Attendance >= 75:
    print("Exam Eligibility:Eligible")
else:
    print("Exam Eligibility:Not Eligible ")

#scholarship eligibility
if Average_marks >= 85 and Attendance >= 80:
    print("You are eligible for scholarship.")
else:
    print("You are not eligible for scholarship.")