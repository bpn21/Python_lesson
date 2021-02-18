marks = input("enter marks obtained by student")
marks  = int(marks)

if(marks>=90):
    grade  = "ex"

elif(marks>=80):
    grade = "A"

elif(marks>=70):
    grade = "B"

elif(marks>=60):
    grade = "C"

elif(marks>=50):
    grade = "D"

elif(marks>=40):
    grade = "E"

elif(marks<40):
    grade = "F"
print('Grade is : ',grade)

