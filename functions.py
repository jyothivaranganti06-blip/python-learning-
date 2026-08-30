def hello(): #function definition
    print("hello python")
hello() #function calling

#return statement
def sum():
    a=9
    b=7
    return a+b
print("the sum of a ,b :",sum())
#passing arguments
def func(name):
    print("hii",name)
func("james")

def sum(a,b):
    return a+b
a=int(input("enter a number: "))
b=int(input("enter another number: "))   
print("sum: ",sum(a,b))

def sum(a,b,c):
    return a+b+c
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
print("sum:",sum(a,b,c))


def sum():
    return a+b
a=8
b=9
print(sum())


#function with return statement 
def add(a, b):
    return a+b
result=add(9,9)
print(result)

#grocery bill
def calculate_total(price,quantity):
    return price*quantity
total=calculate_total(50,3)
print(total)

#calculate age
def age(current_year,birth_year):
    return current_year-birth_year
current_age=age(2026,2006)
print(current_age)

#even or odd
def num(n):
    return n%2==0
number=num(10)
print("even: ",number)

#discount calculator
def calculate_discount(price,discount_percentage):
    discount_amount=price*discount_percentage/100
    return price-discount_amount
final=calculate_discount(1000,20)
print(final) 

#ATM withdrawl
def withdraw(balance,amount):
    if amount<=balance:
        return "allow withdrawl"
    else:
     return "insufficient balance"
total=withdraw(5000,1000)
print(total)

#ATM remaining balance
def withdraw(balance,amount):
    remaining= balance-amount
    return remaining
total=withdraw(5000,1000)
print("remaining balance: ",total)

#calculate grades
def calculate_grade(marks):
    if marks>=90:
        return "grade A"
    elif marks>=80:
        return "grade B"
    elif marks>=60:
        return "grade c"
    elif marks>=50:
        return "grade D"
    else:
        return "fail"
m=calculate_grade(67)
print(m)

#restaurant bill
def restaurant_bill(price,tax,tip):
    return price+tax+tip
total_bill =restaurant_bill(500,50,20)
print(total_bill)

#login system 
def login(username,password):
    username="admin"
    password=1234
    if username and password:
      return "login successfull"
    else:
        return "invalid"
authentication=login("admin",1234)
print(authentication) 

#squaring a number
def square(num):
    return num*num
number=square(9)
print(number)

#cab fare 
def calculate_fare(km):
    fare=50+(km * 15)
    return fare
dist=calculate_fare(5)
print("total fare: ",dist)

#salary calculation
def salary_cal(basic,bonus,deduction):
    salary=basic+bonus-deduction
    return salary
salary=salary_cal(30000,5000,1000)
print(salary)

#mobile recharge
def recharge(balance,amount):
     
    if amount<=balance:
        remaining=balance-amount
        return  "recharge sucessfull" ,remaining
    else:
        return "insufficient balance"
    
total=recharge(500,302)
print(total)

#shopping cart 
def shopping(price,quantity,discount):
    total=price*quantity
    dis=total*10/100
    final_price=total-dis
    return final_price
result=shopping(500,3,10)
print(result)

#bank transfer
def transfer(balance,amount):
    
    if amount>0 and balance>amount:
        remain=balance-amount
        return "valid",remain
    else:
        return "insufficient"
result=transfer(5000,2500)
print(result)

#students average
def average(m1,m2,m3,m4):
    total=m1+m2+m3+m4
    avg=total/4
    return avg
avg=average(30,50,60,90)
print(avg)

#electric bill
def electric_bill(units):
  
    if units <=100:
        return units*5 ,"per unit"
    elif units<=200:
        return units*7,"per unit"
    else:
        return units*10,"per unit"
u=int(input("enter no.of units: "))
bills=electric_bill(u)
print("electric bill:",bills)

#largest number
def largest(a,b,c):
    if a>b and a>c:
        return "A is largest"
    elif b>a and b>c:
        return "B is largest"
    else:
        return "C is largest"
result=largest(2,59,9)
print(result)

#temparature converter 
def celsius_to_fehrenheits(celsius):
    f=(c*9/5)+32
    return f
c=int(input("enter the degree in celsius: "))
temp=celsius_to_fehrenheits(c)
print(temp) 

#simple calculator
def calculator():
    a=int(input("enter the number: "))
    b=int(input("enterr the number: "))
    operator=(input("enter the operator: "))
    if operator=='+':
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else:
        return "invalid operator"
result=calculator()
print(result)

#password checker
def check_password():
    password=input("enter the password: ")
    if len(password)>=8:
        return "strong password"
    else:
        return "weak password"
res=check_password()
print(res)

#parking fee
def parking_fee(hours):
    if hours<=2:
        return "20rs per hour"
    elif hours>2:
        return hours*30,"rs per hour"
res=parking_fee(1)
print(res)

#BMI calculator
def calculate_bmi():
    bmi=weight/(height*height)
    return bmi
weight=float(input("enter the weight in KG: "))
height=float(input("enter the height in cm: "))
res=calculate_bmi()
print(res)
