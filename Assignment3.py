#Assignment3

#Question1
print("Question1:")
string=input("Enter the string: ") 
string=string.lower()
print(string)
list_1=string.split(" ")
l=len(list_1)
dict={}
#checking whether a single word is entered in input or not
if l>1:
    for x in list_1:
        if(x in dict):
            e=dict.get(x)
            e=e+1
            dict[x]=e
        else:
            dict[x]=1
if(l==1):
    for x in string:
        if(x in dict):
            e=dict.get(x)
            e=e+1
            dict[x]=e
        else:
            dict[x]=1
print(dict)
print()
print()
print()
print()

#Question 2
print("Question 2:")
def is_leap_year(year: int) -> bool:                                                                                
#Function for checking if the given year is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
#Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          
#Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 
#Condition for no. of days in February
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      
#Setting no. of days in the given month
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                
#Syntax for incrementing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))
print()
print()
print()
print()

#Question 3
print("Question 3:")
list_in = eval(input("Enter the list of integers: "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))                                                                                     
#(i, i**2) is the tuple which is added in the list, i.e. list_out is list of tuples
print("Output:", list_out)
print()
print()
print()
print()

#Question 4
print("Question 4:")
'''given_table is a list of lists'''
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         
#loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                               
#i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))
            break
print()
print()
print()
print()

#Question 5
print("Question 5:")
string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1
print()
print()
print()
print()

#QUESTION_6 
print("Question 6")
condition=True

Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Enter SID of Student: "))
        name=input("Enter the name of the Student: ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N: ")
        condition = True
    else:
        condition = False

print("(a)")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("(b)")
Value_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Value_sort_dict}")
print("")

print("(c)")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("(d)")
SID_details=int(input("Enter SID whose detail you need- "))
if SID_details in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_details]}")
else:
    print("The SID is not present in Data")
print()
print()
print()
print()


#Question 7
print("Question 7:")
'''a is first number, b is second number and c is the extra variable used for adding and reassigning the values'''
a = 0
b = 1
sum = 0
while True:                                                                                                         
#While loop is just for asking the user to input the value again if user enters a -ve value
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break
print()
print()
print()
print()

#Question 8
print("Question 8:")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
