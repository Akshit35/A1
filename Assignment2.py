#Question_1
print("Question1:")
String="Python is a case sensitive language"

#Part(a)
length=len(String)
print("(a) length of string:",length)

#Part(b)
reversed_string= (String)[::-1]
print("(b) reversed string:",reversed_string)

#Part(c)
print("(c) new string:", String[10:26] )

#Part(d)
after_replacing= String.replace("a case sensitive","object oriented")
print("(d) after replacing:",after_replacing)

#Part(e)
index= String.find("a")
print("(e) index of a:",index)

#Part(f)
remove_white_spaces= String.replace(" ","")
print("(f) after removing white spaces:",remove_white_spaces)
print()
print()
print()
print()



#Question_2
print("Question2:")
name= input("Name: ")
sid= int(input("SID: "))
dept_name= input("Department Name: ")
cgpa= float(input("CGPA: "))
print("\nHey, %s Here!\nMy SID is %d \nI am from %s department and my CGPA is %f"%(name,sid,dept_name,cgpa))
print()
print()
print()
print()



#Question_3
print("Question3:")
a=56
b=10

#Part(a)
print("(a)a&b:",a&b)

#Part(b)
print("(b)a|b:",a|b)

#Part(c)
print("(c)a^b:",a^b)

#Part(d)
print("(d)Left shift a with 2 bits:",a<<2)
print("   Left shift b with 2 bits:",b<<2)

#Part(e)
print("(e)Right shift a with 2 bits:",a>>2)
print("   Right shift b with 4 bits:",b>>4)
print()
print()
print()
print()

 #Question4:
print("Question4:")
first_number= int(input("Enter first number : "))
second_number= int(input("Enter second number : "))
third_number= int(input("Enter third number : "))
largest_number=first_number
for i in[first_number,second_number,third_number]:
    if largest_number<i:
        largest_number=i
print("Largest number is:",largest_number)
print()
print()
print()
print()



#Question5:
print("Question5:")
names=str(input("Name:"))
found="No"
for i in["Raman","Adidtya","Rahul","Mohit"]:
    if names==i:
        found="Yes"
print(found)
print()
print()
print()
print()


#Question6
print("Question6:")
side_1= int(input("Length of first side : "))
side_2= int(input("Length of second side : "))                          
side_3= int(input("Length of third side : "))
result="No"
if(side_1+side_2>side_3)&(side_2+side_3>side_1)&(side_3+side_1>side_2):
        result="Yes"
print(result)
       

 
    



