SA = float(input("Enter SA grade: "))
FA = float(input("Enter FA grade: "))
current_grade = SA * 0.7 + FA * 0.3
previous_quarter_grade = float(input("Enter previous quarter grade: "))
final_quarter_grade = (previous_quarter_grade + current_grade * 20) / 3
if final_quarter_grade == 1.00:
    print("Status: EXCELLENT!")
elif final_quarter_grade >= 1.50 and final_quarter_grade < 1.00:
    print("Status: VERY GOOD!")
elif final_quarter_grade >= 2.00 and final_quarter_grade < 1.50:
    print("Status: GOOD!")
elif final_quarter_grade >= 2.50 and final_quarter_grade < 2.00:
    print("Status: SATISFACTORY!")
elif final_quarter_grade >= 3.00 and final_quarter_grade < 2.50:
    print("Status: FAIR!")
elif final_quarter_grade >= 4.00 and final_quarter_grade < 3.00:
    print("Status: FAILED ON CONDITION!")
else:
    print("Status: FAILED!")

# The smaller the number, the better the grade. 1.00 is the highest grade, while 5.00 is the lowest grade.