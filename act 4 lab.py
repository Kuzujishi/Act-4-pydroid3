def assign_grade(score):
    if score < 0 or score > 100:
        print("Walang ganyang score bossing!! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

#grading system
assign_grade(95)
assign_grade(85)
assign_grade(75)
assign_grade(65)
assign_grade(50)
assign_grade(-5)
assign_grade(105)

#EPHRAIM JESTIE G. ROSARIO
#12-BSCPE-01