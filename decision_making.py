
#if: if statement is used to check a condition and execute a block of code if  the condition is true
#checking greater number
a=10
b=45
if b>a:
 print("b is greater ")

# checking even number
a=4
if a%2==0:
 print(" a is even")

#if-else: checks if the "if" condition and execute if it is true else it execute the "else" block
#checking grater number 
f=34
e=56
if f>e:
 print("f is greater")
else:
 print("e is greater")

#even or odd
a=int(input("enter a number: "))
if a%2==0:
 print("a is even number: ",a)
else:
 print("odd number : ",a)

#voting eligibility
age=int(input("enter your age: "))
if age>=18:
 print("eligible to vote")
else:
 print("not eligible")

#if-elif-else: used when there are multiple conditions to execute

#grading marks
marks=int(input("enter your marks: "))
if marks>=90:
 print("GRADE:A")
elif marks>=70:
 print("GRADE:B")
elif marks>=60:
 print("GRADE:C")
else:
 print("fail")

#nested if :if inside if used to execute multiple conditions
num=int(input("enter a number: "))
if num>0:
 if num%2==0:
    print("positive even number")
 else:
    print("positive odd number")
else:
  print("negative number")


#largest of two numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
if a>b:
 print("a is greater")
elif b>a:
 print("b is greater")
else:
 print("both are equal")

#leap year
year=(int(input("enter the year: ")))
if year%4==0:
 print("leap year")
else:
 print("not leap year")


#password check
password=int(input("enter password: "))
confirm_pass=int(input("enter confirm password: "))
if password==confirm_pass:
 print("correct password")
else:
 print("invalid password")

#ticket price based on age
age=int(input("enter age: "))
if age<=5:
 print("free")
elif age<=18:
 print("100/-")
elif age<=60:
 print("200/-")
else:
 print("120/-")

#biggest number of three
fNumber=int(input("enter first number: "))
sNumber=int(input("enter second number: "))
tNumber=int(input("enter third number: "))
if fNumber>sNumber and fNumber>tNumber:
 print("first number is greater")
elif sNumber>fNumber and sNumber>tNumber:
 print("second number is greater")
elif tNumber>fNumber and tNumber>sNumber:
 print("third number is greater ")
else:
 print("try again")


#using logical operators
#AND operator
age=int(input("enter age: "))
has_id=True
if age>18 and has_id:
  print("allowed")
else:
 print("not allowed")

#OR operator
day=input("enter day: ")
if day=="saturday" or day=="sunday":
 print("weekend")
else:
 print("work day")

#NOT operator
is_raining=False
if not is_raining:
 print("go outside")




