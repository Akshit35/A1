#Assignment-1

#Question1
print("Average Calculator")
number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number:"))
number3=float(input("Enter the third number:"))

average=(number1+number2+number3)/3
print("Average of three numbers is:",average)
print()
print()
print()
print()




#Question2
print("Income Tax Calculator")
gross_income=int(input("Enter your gross income:"))
dep=int(input("Enter the number of dependents:"))
taxable_income=gross_income-10000-(3000*dep)
tax=taxable_income*(20/100)
print("Your total income tax:",tax)
print()
print()
print()
print()


#Question3
print("Student Details list")
name=str(input("Enter your Name:"))
sid=int(input("Enter your Student id:"))
gender=str(input("Gender(F,M,U):"))
cgpa=float(input("CGPA:"))
course_name=input("Course Name:")
student_details=name,[sid,name,gender,course_name,cgpa]
print(student_details)
print()
print()
print()
print()


#Question4
print("Student Mark List")
mark1=input("Marks of first student:")
mark2=input("Marks of second student:")
mark3=input("Marks of third student:")
mark4=input("Marks of fourth student:")
mark5=input("Marks of fifth student:")
SortedMarks=[mark1,mark2,mark3,mark4,mark5]
SortedMarks.sort()
print(SortedMarks)
print()
print()
print()
print()


#Question5
Color=['Red','Green','White','Black','Pink','Yellow']
print(Color)
print()
print()
print()
print()


#PartA
del Color[3]
print('After deleting fourth item,new list is:',Color)
print()
print()
print()
print()


#PartB
Color=['Red','Green','White','Black','Pink','Yellow']
Color[3]=Color[4]="Purple"
print("Final List:",Color[0:4]+Color[5:6
                                     ])
print()
print()
print()
print()


















