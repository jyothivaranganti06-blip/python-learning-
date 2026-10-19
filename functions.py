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
calculate_bmi()

#ATM mini program
def atm():
    balance=int(input("enter the balance: "))
    choice=int(input("enter the choice:"))
    if choice==1:
        amount=int(input("enter the amount:"))
        if amount<=balance:
            balance=balance-amount
            print("withdrawal sucessfull")
            print("remaining balance:",balance)
        else:
            print("insufficient balance")
    elif choice==2:
        amount=int(input("enter the amount:"))
        balance=balance+amount
        print(" deposit sucesssfull")
        print("new balance",balance)
    elif choice==3:
        print("current balance:",balance) 
    else:
        print("invalid choice")

atm()

#movie ticket 
def ticket_price():
    age=int(input("enter the age: "))
    if age<5:
        print("free entry")
    elif age>5 & age<17:
        print("100 RS")
    elif age>17 & age<59:
        print("200 RS ")
    elif age>59:
        print("120 RS")
    else:
        print("please enter age")
ticket_price()

#positive negative or zero
def check_num():
    num=int(input("enter the number: "))
    if num<0:
        print("negative")
    elif num>0:
        print("positive")
    else:
        print("zero")
check_num()

#delivery charge
#def delivery_charge():
#    amount=int(input("enter the amount:"))
#    if amount>500:
#        print("free delivery")
#    else:
#        print("50 RS charge")
#delivery_charge()

#function returning boolean
#def is_even(num):
#    num=int(input("enter the number: "))
#    return num%2==0
#re=is_even(num)
#print(re)

#password checker
#def check_password():
#   password=input("enter the password: ")
#   a=len(password)
#   if a<6:
#     return "weak"
#   elif a<10:
#       return "mid"
#   else:
#       return "strong"
#res=check_password()
#print(res)


#parameters and arguments
#positional arguents
#def student(name,age,course):
#    print("name:",name)
#    print("age:",age)
#    print("course:",course)
#student("jyothi",20,"computer science")

#keyword arguments
#def students(name,age,course):
#    print(name)
#    print(age)
#    print(course)
#students(name="jytohi",course="computer science",age=20)

#default parameter
def greet(name="guest"):
    print(f"hello,{name}")
greet()
#call it by name override the guest
def greet(name="guest"):
    print("hello",name)
greet("jyothi")

#default tax
def bill(amount,tax=5):
    tax_amount=amount*tax/100
    total=amount+tax_amount
    print("tax:",tax_amount)
    print("total bill",total)
bill(100)

#mix positional and keyword
def profile(name,age,city):
    print(f"my name is {name},age is {age},i live in {city}")
profile("jyothi",age=20,city="hyderabad")

# #scope variables
#local variable
def test():
     x=20
     print(x)
test()
# global variable
x=10
def test():
    print(x)
test()
#local and global
y="hello"
def greet():
     x="hii"
     print("this is inner function",x)
greet()
print("this is outside function",y)

#local vs global
x=10
def test():
     x=67
     print(x)
test()
print(x)

#global keyword
counter=90
def increment():
     global counter
     counter+=1
increment()
print(counter)

#functions  with list
#sum of list 
def list_sum(numbers):
     return sum(numbers)
my_list=[4,5,6]
result=list_sum(my_list)
print("total sum: ",result)

#manual way(using for loop)
def list_sum(numbers):
     total=0
     for num in numbers:
          total+=num
     return total
my_list=[5,5,2]
res=list_sum(my_list)
print(res)

#taking user input
def list_sum(number):
     total=0
     for i in number:
          total+=i
     return total
count=int(input("enter the count of numbers: "))
em_list=[]
for _ in range(count):
   num=int(input("enter the  numbers: "))
   em_list.append(num)
res=list_sum(em_list)
print(res)

#find maximum
def find_max(numbers):
     largest=0
     for i in numbers:
          if i>largest:
               
               largest=i
     return largest
count=int(input("enter the no.of count:"))
num_list=[]
for _ in range(count):
     num=int(input("enter the numbers:"))
     num_list.append(num)
res=find_max(num_list)
print(res)

#count even numbers
def count_even(num):
     count=0
     for i in num:
          if i%2==0:
           count+=1
     return count
count=int(input("enter the no.of count: "))
even_list=[]
for _  in range(count):
     num=int(input("enter the numbers:"))
     even_list.append(num)
res=count_even(even_list)
print(res)

#reverse a list
def reverse_list(numbers):
     return numbers[::-1]
count=int(input("enter the no.of count:"))
rev_list=[]
for _ in range(count):
     num=int(input("enter the numbers:"))
     rev_list.append(num)
res=reverse_list(rev_list)
print(res)

#remove duplicates
def remove_duplicates(numbers):
      unique_list=[]
      for i in numbers:
           if i not in unique_list:
                unique_list.append(i)
      return unique_list
count=int(input("enter the no.of count:"))
dup_list=[]
for _ in range(count):
     num=int(input("enter the numbers:"))
     dup_list.append(num)
res=remove_duplicates(dup_list)
print(res)

#find second largest
def second_large(numbers):
     for i in numbers:
          largest=max(numbers)
          numbers.remove(largest)
          second_largest=max(numbers)
          return second_largest
count=int(input("enter the no.of count:"))
s_list=[]
for _ in range(count):
     num=int(input("enter the numbers:"))
     s_list.append(num)
res=second_large(s_list)
print(res)

#function with strings

#count vowels


def count_vowel(text):
    vowel=["a","e","i","o","u"]
    count=0
    for i in text:
        if i in vowel:
            count+=1
    return count
txt=input("enter the word:")
res=count_vowel(txt)
print(res)

#count consonanta
def count_consonant(text):
    vowels=["a","e","i","o","u"]
    count=0
    for i in text:
        if i not in vowels:
            count+=1
    return count
txt=input("enter the word: ")
res=count_consonant(txt)
print(res)

#reverse string
def reverse_string(text):
    return text[::-1]
txt=input("enter the word: ")
res=reverse_string(txt)
print(res)


#palindrome checker
def palindrome(text):
    p=text[::-1]
    if text  in p:
        return "palindrome"
    else:
        return "not palindrome"
txt=input("enter the word: ")
res=palindrome(txt)
print(res)

#count words
def count_word(sentence):
    sen=sentence.split(" ")
    count=0
    for i in sen:     #we can simply use len(sen)
      count+=1  
    return count
txt=input('enter the word: ')
res=count_word(txt)
print(res)

#character frequency
def char_freq(word):
     freq={}
     for i in word:
          if i in freq:
               freq[i]+=1
          else:
               freq[i]=1
     return freq
txt=input("enter the word: ")
res=char_freq(txt)
print(res)

#*args
#add all number of numbers
def add_all(*numbers):
    return sum(numbers)
res=add_all(1,2,3,4)
es=add_all(10,20,30)
print(add_all(2,4,6,8,10))
print(res)
print(es)

#average of numbers
def avg(*args):
    average=sum(args)/len(args)
    return average
res=avg(10,20,30)
print(res)

#find largest number using *args
def largest(*num):
    if not num:
        return None
    largest=num[0]
    for i in num:
     if i >largest:
        largest=i
    return largest
res=largest(5,4,7,9,50)
print(res)

#**kwargs
def student_details(**details):
   return details
print(student_details(name="jyothi",age=20,course="bsc(honours)"))

#employee details
def employee_details(**details):
   return details
print(employee_details(name="james",salary=30000,department="IT"))

#functions calling functions
def calculate_total(prices):
   return sum(prices)
#count=int(input("enter the no.of counts: "))
#amount=[]
#for  i in range(count):
  # num=int(input("enter the prices: "))
 #  amount.append(num)
#res=calculate_total(amount)
#print(res)

def calculate_discount(prices,discount_percentage):
   discount_amount=prices*discount_percentage/100
   return discount_amount
#res=calculate_discount(3500,10)
#print(res)

def calculate_tax(amount,tax):
   total=amount*tax/100
   return total
#res=calculate_tax(3150,10)
#print(res)
def final_bill(prices,discount_percentage,tax_percentage):
   total=calculate_total(prices)
   discount=calculate_discount(total,discount_percentage)
   amount=total-discount
   tax=calculate_tax(amount,tax_percentage)
   final_amount=amount+tax
   return final_amount
prices=[1000,2000,500]
res=final_bill(prices,10,10)
print("final bill: ",res)

#student result system 
def calculate_total_marks(marks):
   return sum(marks)

def calclulate_avg(marks):
   return sum(marks)/len(marks)

def calculate_grade(grade):
   if grade>90:
      return "A"
   elif grade>80:
      return "B"
   elif grade>70:
      return "C"
   elif grade>50:
      return "D"
   else:
      return "Fail"
def display_result(marks):

   total=calculate_total_marks(marks)
   avg=calclulate_avg(marks)
   g=calculate_grade(avg)

   print("total",total)
   print("average",avg)
   print("grade",g)
s_marks=[40,50,34,56,89]
res=display_result(s_marks)
print(res)

#ATM system
def check_pin():
   origin_pin=input("enter the pin: ")
   confirm_pin=input("enter the confirm pin: ")
   if origin_pin==confirm_pin:
      return "correct pin"
   else:
      return "incorrect pin"

def withdraw(balance):
   amount=int(input("enter the amount"))
   if amount>balance:
      print("insuffient balance")
   else:
       new_balance=balance-amount
       print("withdrawal successful remaining balance:",new_balance)
       

def deposit(balance):
   amount=int(input("enter the deposit amount: "))
   new_amount=balance+amount
   print("amount after deposit: ",new_amount)

def atm():
    current_balance=5000
    status=check_pin()
    print(status)

    if status=="correct pin":
       current_balance=withdraw(current_balance)
       depo=deposit(current_balance)
atm()


#recursion
#count down
def countdown(n):
     if n==0:
        return 
     print(n)
     countdown(n-1)
countdown(5)

#factorial 
def factorial(n):
   if n==1:
      return 1
   return n*factorial(n-1)
print("factorial:",factorial(5))
print("problem solved")

#sum of numbers
def add_numbers(n):
    if n==1:
     return 1
    return n+add_numbers(n-1)
print(add_numbers(5))

def fibbinacci(n):
   if n==0:
    return 0
   if n==1:
     return 1
   return fibbinacci(n-1)+fibbinacci(n-2)
print(fibbinacci(7))

#lambda function
#square
square= lambda n: n*n
result=square(5)
print(result)

#even
even=lambda n:n%2==0
print(even(6))

#odd
odd=lambda n:n%2!=0
print(odd(7))

#even/odd
even_odd=lambda n:"even" if n%2==0 else "odd"
print(even_odd(8))

#add two numbers
add= lambda a,b:a+b
print(add(6,7))

#sort using lambda
students=[("Adithya",50),("Banu",80),("Chinnu",70)]
students.sort(key=lambda student:student[1])
print("students sorted by marks:")
print(students)


#higher order apply operation
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def apply_operation(a,b,operation):
    return operation(a,b)
print(apply_operation(5,10,add))
print(apply_operation(4,5,multiply))

#custom filter
def is_even(n):
    return n%2==0
def filter_numbers(numbers,condition):
    result=[]
    for number in numbers:
        if condition(number):
            result.append(number)
    return result
numbers=[1,2,3,4,5,6,7,8,9,10]
print(filter_numbers(numbers,is_even))

#calculator
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def apply_calculation(a,b,operation):
    return operation(a,b)
print(apply_calculation(5,2,add))
print(apply_calculation(9,2,substract))
print(apply_calculation(6,7,multiply))

#final function projects
#complete ATM 
def check_pin(pin):
    c_pin= int(input("enter the pin: "))
    if pin==c_pin:
        print(" login sucessfull")
        return True
    else:
        print("invalid pin")
        return False

    
def check_balance(balance):
        return balance

def withdraw(amount,balance):
    if amount<balance:
        new_balance=balance-amount
        print(new_balance)
    else:
        print("insuffiecient balance")

def deposit(amount,balance):
    new_balance=amount+balance
    return new_balance

def change_pin():
    new_password=int(input("enter the new password: "))
    confirm_pass=int(input("enter the confirm password: "))
    if confirm_pass==new_password:
        print("password changed sucessfully")
        return new_password
    else:
        print("incorrect password")
        return None
pin=1234
balance=5000
login=check_pin(pin)
if login:
    print("1.check Balance\n""2.withdraw\n""3.deposit\n""4.change pin\n""Exist\n")
    choice=int(input("enter the choice:"))
    if choice==1:
        result=check_balance(balance)
        print("Balance",result)
    elif choice==2:
        amount=int(input("ente the amount:"))
        balance=withdraw(amount,balance)
        print("new balance after withdraw:",balance)
    elif choice==3:
        amount=int(input("enter the deposit amount:"))
        balace=deposit(amount,balance)
        print("amount after deposit",balance)
    elif choice==4:
        new_pin=change_pin()
        if new_pin is not None:
            pin=new_pin
        elif choice==5:
            print("Thank you")
        else:
            print("invalid choice")

#shopping cart
def add_items(products):
    item=input("enter the item: ")
    price=float(input("enter the price: "))
    products.append([item,price])
    return products

def remove_items(products):
    item=input("enter the item to remove: ")

    for product in products:
        if product[0]==item:
            products.remove(product)
            print("item removed")
            return products
        else:
            print("item not found")
            return products

def calculate_total(products):
    total=0
    for product in products:
        total=total+product[1]
    return total

def apply_discount(total):
    discount=total*0.10
    final_amount=total-discount
    return final_amount

def calculate_tax(amount):
    tax=amount*0.05
    final_amount=amount+tax
    return final_amount

def generate_bill(products,total,discount_amount,tax_amount,final_amount):
    print("\n--------BILL----------")
    for product in products:
        print(product[0],"RS",product[1])

    print("------------------")
    print("Total",total)
    print("Discount",discount_amount)
    print("Tax",tax_amount)
    print("Final amount",final_amount)

products=[]
products=add_items(products)
products=add_items(products)
products=add_items(products)

print("\n your cart")
print(products)

remove=input("\n do you want to remove an item yes/no: ")
if remove=="yes":
    products=remove_items(products)
total=calculate_total(products)
discounted_amount=apply_discount(total)
discount_amount=total-discounted_amount
final_amount=calculate_tax(discounted_amount)
tax_amount=final_amount-discounted_amount

generate_bill(products,total,discount_amount,tax_amount,final_amount)

#student management
def add_student(students):
    person=input("enter your name: ")
    mark1=int(input("enter the subject 1 marks: "))
    mark2=int(input("enter the subject 2 marks: "))
    mark3=int(input("enter the subject 3 marks: "))
    students.append([person,mark1,mark2,mark3])
    return students

def total_marks(students):
    total=0
    for student in students:
        total=total + student[1]+student[2]+student[3]
    return total

def total_avg(total,students):
    average=total/3
    return average

def grade(marks):
    if marks>=90:
        return "grade A"
    elif marks>=70:
        return "grade B "
    elif marks>=50:
        return "grade C"
    else:
        return "fail"
    
def display_student(students,total_marks,average,grade):
    for student in students:
        print("\n--------student report-------")
        print("name: ",student[0])
        print("subject1: ",student[1])
        print("subject2: ",student[2])
        print("subject3: ",student[3])

    print("Total marks: ",total_marks)
    print("Average: ",average)
    print("Grade: ",grade)

students=[]

students=add_student(students)
student=students[0]


print("\n your details")
print(students)
total=total_marks(students)
average=total_avg(total,students)
g=grade(average)
display_student(students,total,average,g)

#hospital billing
def patient_details():
    name=input("enter the patient name: ")
    return name

def consultation_fee():
    amount=int(input("enter the consultation fee: "))
    return amount

def medicine_bill():
    price=int(input("enter the medicine bill: "))
    return price

def room_price():
    day=500
    days=int(input("how many days ; per day RS 500: "))
    room_charge=day*days
    return room_charge

def total_bill(patient,consultation,medicine,room):
    
    print("\n------patient Report---------")
    print("patien Name: ",patient)
    print("consultation fee: ",consultation)
    print("medicine bill: ",medicine)
    print("room charge: ",room)
    total=consultation+medicine+room
    print("total bill: ",total)

patient=patient_details()
consultation=consultation_fee()
medicine=medicine_bill()
room=room_price()
total_bill(patient,consultation,medicine,room)


#restaurant management
def show_menu():
    print("\n--------MENU------ ")
    print("1.BURGER 100 RS")
    print("2.PIZZA 180 RS")
    print("3.MATCHA 100 RS")
def take_order():
    orders=[]
    while True:
        choice=int(input("\n choose item (0 to finish): "))
        if choice==0:
            break
        quantity=int(input("enter quantity: "))
        if choice==1:
            orders.append([100,quantity])
        elif choice==2:
            orders.append([180,quantity])
        elif choice==3:
            orders.append([100,quantity])
        else:
            print("invalid choice")

    return orders

def calculate_bill(orders):
    subtotal=0
    for order in orders:
        price=order[0]
        quantity=order[1]
        subtotal=subtotal+(price*quantity)
    return subtotal

def apply_discount(subtotal):
    discount=subtotal*10/100
    return discount

def generate_bill(subtotal,discount):
    final_bill=subtotal-discount

    print("\n----bill-------")
    print("subtotal RS:",subtotal)
    print("discount RS:",discount)
    print("final bill RS:",final_bill)

def main():
    show_menu()
    orders=take_order()
    subtotal=calculate_bill(orders)
    discount=apply_discount(subtotal)
    generate_bill(subtotal,discount)
    
main()

#personal expense tracker

expenses=[]
def add_expense():
    category=input("enter the category: ")
    amount=int(input("enter the expense amount: "))

    expense={"category": category,"amount": amount}
    expenses.append(expense)
    print("expenses added sucessfully")

def remove_expense():
    if len(expenses)==0:
        print("no expenses to remove")
        return 
    for i in range(len(expenses)):
        print(i+1, expenses[i] ["category"],"RS",expenses[i] ["amount"])
        choice=int(input("enter the expense number to remove:"))
        if choice>=1 and choice<=len(expenses):
            removed=expenses.pop(choice-1)
            print(removed["category"],"expense removed")
        else:
            print("invalid choice")

def total_expenses():
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    print("total expense: RS",total)

def highest_expense():
    if len(expenses)==0:
        print("No expense available")
        return 
    highest=expenses[0]
    for expense in expenses:
        if expense["amount"]>highest["amount"]:
            highest=expense
    print("highest expense:",highest["category"],"RS",highest["amount"])

def average_expense():
    if len(expenses)==0:
        print("no expense available")
        return
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    average=total/len(expenses)
    print("average expense : RS",format(average,".2f"))


while True :
    print("\n ----personal expenses tracker------")
    print("1. Add expenses")
    print("2. Remove expenses")
    print("3.show Total")
    print("4. show highest")
    print("5. show average")
    print("6.exist")

    choice=int(input("enter your choice: "))
    if choice==1:
        add_expense()
    elif choice==2:
        remove_expense()
    elif choice==3:
        total_expenses()
    elif choice==4:
        highest_expense()
    elif choice==5:
        average_expense()
    elif choice==6:
        print("thankyou")
        break
    else:
        print("invalid choice")