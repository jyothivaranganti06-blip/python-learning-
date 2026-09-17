# def hello(): #function definition
#     print("hello python")
# hello() #function calling

# #return statement
# def sum():
#     a=9
#     b=7
#     return a+b
# print("the sum of a ,b :",sum())
# #passing arguments
# def func(name):
#     print("hii",name)
# func("james")

# def sum(a,b):
#     return a+b
# a=int(input("enter a number: "))
# b=int(input("enter another number: "))   
# print("sum: ",sum(a,b))

# def sum(a,b,c):
#     return a+b+c
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# print("sum:",sum(a,b,c))


# def sum():
#     return a+b
# a=8
# b=9
# print(sum())


# #function with return statement 
# def add(a, b):
#     return a+b
# result=add(9,9)
# print(result)

# #grocery bill
# def calculate_total(price,quantity):
#     return price*quantity
# total=calculate_total(50,3)
# print(total)

# #calculate age
# def age(current_year,birth_year):
#     return current_year-birth_year
# current_age=age(2026,2006)
# print(current_age)

# #even or odd
# def num(n):
#     return n%2==0
# number=num(10)
# print("even: ",number)

# #discount calculator
# def calculate_discount(price,discount_percentage):
#     discount_amount=price*discount_percentage/100
#     return price-discount_amount
# final=calculate_discount(1000,20)
# print(final) 

# #ATM withdrawl
# def withdraw(balance,amount):
#     if amount<=balance:
#         return "allow withdrawl"
#     else:
#      return "insufficient balance"
# total=withdraw(5000,1000)
# print(total)

# #ATM remaining balance
# def withdraw(balance,amount):
#     remaining= balance-amount
#     return remaining
# total=withdraw(5000,1000)
# print("remaining balance: ",total)

# #calculate grades
# def calculate_grade(marks):
#     if marks>=90:
#         return "grade A"
#     elif marks>=80:
#         return "grade B"
#     elif marks>=60:
#         return "grade c"
#     elif marks>=50:
#         return "grade D"
#     else:
#         return "fail"
# m=calculate_grade(67)
# print(m)

# #restaurant bill
# def restaurant_bill(price,tax,tip):
#     return price+tax+tip
# total_bill =restaurant_bill(500,50,20)
# print(total_bill)

# #login system 
# def login(username,password):
#     username="admin"
#     password=1234
#     if username and password:
#       return "login successfull"
#     else:
#         return "invalid"
# authentication=login("admin",1234)
# print(authentication) 

# #squaring a number
# def square(num):
#     return num*num
# number=square(9)
# print(number)

# #cab fare 
# def calculate_fare(km):
#     fare=50+(km * 15)
#     return fare
# dist=calculate_fare(5)
# print("total fare: ",dist)

# #salary calculation
# def salary_cal(basic,bonus,deduction):
#     salary=basic+bonus-deduction
#     return salary
# salary=salary_cal(30000,5000,1000)
# print(salary)

# #mobile recharge
# def recharge(balance,amount):
     
#     if amount<=balance:
#         remaining=balance-amount
#         return  "recharge sucessfull" ,remaining
#     else:
#         return "insufficient balance"
    
# total=recharge(500,302)
# print(total)

# #shopping cart 
# def shopping(price,quantity,discount):
#     total=price*quantity
#     dis=total*10/100
#     final_price=total-dis
#     return final_price
# result=shopping(500,3,10)
# print(result)

# #bank transfer
# def transfer(balance,amount):
    
#     if amount>0 and balance>amount:
#         remain=balance-amount
#         return "valid",remain
#     else:
#         return "insufficient"
# result=transfer(5000,2500)
# print(result)

# #students average
# def average(m1,m2,m3,m4):
#     total=m1+m2+m3+m4
#     avg=total/4
#     return avg
# avg=average(30,50,60,90)
# print(avg)

# #electric bill
# def electric_bill(units):
  
#     if units <=100:
#         return units*5 ,"per unit"
#     elif units<=200:
#         return units*7,"per unit"
#     else:
#         return units*10,"per unit"
# u=int(input("enter no.of units: "))
# bills=electric_bill(u)
# print("electric bill:",bills)

# #largest number
# def largest(a,b,c):
#     if a>b and a>c:
#         return "A is largest"
#     elif b>a and b>c:
#         return "B is largest"
#     else:
#         return "C is largest"
# result=largest(2,59,9)
# print(result)

# #temparature converter 
# def celsius_to_fehrenheits(celsius):
#     f=(c*9/5)+32
#     return f
# c=int(input("enter the degree in celsius: "))
# temp=celsius_to_fehrenheits(c)
# print(temp) 

# #simple calculator
# def calculator():
#     a=int(input("enter the number: "))
#     b=int(input("enterr the number: "))
#     operator=(input("enter the operator: "))
#     if operator=='+':
#         return a+b
#     elif operator=="-":
#         return a-b
#     elif operator=="*":
#         return a*b
#     elif operator=="/":
#         return a/b
#     else:
#         return "invalid operator"
# result=calculator()
# print(result)

# #password checker
# def check_password():
#     password=input("enter the password: ")
#     if len(password)>=8:
#         return "strong password"
#     else:
#         return "weak password"
# res=check_password()
# print(res)

# #parking fee
# def parking_fee(hours):
#     if hours<=2:
#         return "20rs per hour"
#     elif hours>2:
#         return hours*30,"rs per hour"
# res=parking_fee(1)
# print(res)

# #BMI calculator
# def calculate_bmi():
#     bmi=weight/(height*height)
#     return bmi
# weight=float(input("enter the weight in KG: "))
# height=float(input("enter the height in cm: "))
# calculate_bmi()

# #ATM mini program
# def atm():
#     balance=int(input("enter the balance: "))
#     choice=int(input("enter the choice:"))
#     if choice==1:
#         amount=int(input("enter the amount:"))
#         if amount<=balance:
#             balance=balance-amount
#             print("withdrawal sucessfull")
#             print("remaining balance:",balance)
#         else:
#             print("insufficient balance")
#     elif choice==2:
#         amount=int(input("enter the amount:"))
#         balance=balance+amount
#         print(" deposit sucesssfull")
#         print("new balance",balance)
#     elif choice==3:
#         print("current balance:",balance) 
#     else:
#         print("invalid choice")

# atm()

# #movie ticket 
# def ticket_price():
#     age=int(input("enter the age: "))
#     if age<5:
#         print("free entry")
#     elif age>5 & age<17:
#         print("100 RS")
#     elif age>17 & age<59:
#         print("200 RS ")
#     elif age>59:
#         print("120 RS")
#     else:
#         print("please enter age")
# ticket_price()

# #positive negative or zero
# def check_num():
#     num=int(input("enter the number: "))
#     if num<0:
#         print("negative")
#     elif num>0:
#         print("positive")
#     else:
#         print("zero")
# check_num()

# #delivery charge
# #def delivery_charge():
# #    amount=int(input("enter the amount:"))
# #    if amount>500:
# #        print("free delivery")
# #    else:
# #        print("50 RS charge")
# #delivery_charge()

# #function returning boolean
# #def is_even(num):
# #    num=int(input("enter the number: "))
# #    return num%2==0
# #re=is_even(num)
# #print(re)

# #password checker
# #def check_password():
# #   password=input("enter the password: ")
# #   a=len(password)
# #   if a<6:
# #     return "weak"
# #   elif a<10:
# #       return "mid"
# #   else:
# #       return "strong"
# #res=check_password()
# #print(res)


# #parameters and arguments
# #positional arguents
# #def student(name,age,course):
# #    print("name:",name)
# #    print("age:",age)
# #    print("course:",course)
# #student("jyothi",20,"computer science")

# #keyword arguments
# #def students(name,age,course):
# #    print(name)
# #    print(age)
# #    print(course)
# #students(name="jytohi",course="computer science",age=20)

# #default parameter
# def greet(name="guest"):
#     print(f"hello,{name}")
# greet()
# #call it by name override the guest
# def greet(name="guest"):
#     print("hello",name)
# greet("jyothi")

# #default tax
# def bill(amount,tax=5):
#     tax_amount=amount*tax/100
#     total=amount+tax_amount
#     print("tax:",tax_amount)
#     print("total bill",total)
# bill(100)

# #mix positional and keyword
# def profile(name,age,city):
#     print(f"my name is {name},age is {age},i live in {city}")
# profile("jyothi",age=20,city="hyderabad")

# # #scope variables
# #local variable
# def test():
#      x=20
#      print(x)
# test()
# # global variable
# x=10
# def test():
#     print(x)
# test()
# #local and global
# y="hello"
# def greet():
#      x="hii"
#      print("this is inner function",x)
# greet()
# print("this is outside function",y)

# #local vs global
# x=10
# def test():
#      x=67
#      print(x)
# test()
# print(x)

# #global keyword
# counter=90
# def increment():
#      global counter
#      counter+=1
# increment()
# print(counter)

# #functions  with list
# #sum of list 
# def list_sum(numbers):
#      return sum(numbers)
# my_list=[4,5,6]
# result=list_sum(my_list)
# print("total sum: ",result)

# #manual way(using for loop)
# def list_sum(numbers):
#      total=0
#      for num in numbers:
#           total+=num
#      return total
# my_list=[5,5,2]
# res=list_sum(my_list)
# print(res)

# #taking user input
# def list_sum(number):
#      total=0
#      for i in number:
#           total+=i
#      return total
# count=int(input("enter the count of numbers: "))
# em_list=[]
# for _ in range(count):
#    num=int(input("enter the  numbers: "))
#    em_list.append(num)
# res=list_sum(em_list)
# print(res)

# #find maximum
# def find_max(numbers):
#      largest=0
#      for i in numbers:
#           if i>largest:
               
#                largest=i
#      return largest
# count=int(input("enter the no.of count:"))
# num_list=[]
# for _ in range(count):
#      num=int(input("enter the numbers:"))
#      num_list.append(num)
# res=find_max(num_list)
# print(res)

# #count even numbers
# def count_even(num):
#      count=0
#      for i in num:
#           if i%2==0:
#            count+=1
#      return count
# count=int(input("enter the no.of count: "))
# even_list=[]
# for _  in range(count):
#      num=int(input("enter the numbers:"))
#      even_list.append(num)
# res=count_even(even_list)
# print(res)

# #reverse a list
# def reverse_list(numbers):
#      return numbers[::-1]
# count=int(input("enter the no.of count:"))
# rev_list=[]
# for _ in range(count):
#      num=int(input("enter the numbers:"))
#      rev_list.append(num)
# res=reverse_list(rev_list)
# print(res)

# #remove duplicates
# def remove_duplicates(numbers):
#       unique_list=[]
#       for i in numbers:
#            if i not in unique_list:
#                 unique_list.append(i)
#       return unique_list
# count=int(input("enter the no.of count:"))
# dup_list=[]
# for _ in range(count):
#      num=int(input("enter the numbers:"))
#      dup_list.append(num)
# res=remove_duplicates(dup_list)
# print(res)

# #find second largest
# def second_large(numbers):
#      for i in numbers:
#           largest=max(numbers)
#           numbers.remove(largest)
#           second_largest=max(numbers)
#           return second_largest
# count=int(input("enter the no.of count:"))
# s_list=[]
# for _ in range(count):
#      num=int(input("enter the numbers:"))
#      s_list.append(num)
# res=second_large(s_list)
# print(res)

#function with strings

#count vowels


# def count_vowel(text):
#     vowel=["a","e","i","o","u"]
#     count=0
#     for i in text:
#         if i in vowel:
#             count+=1
#     return count
# txt=input("enter the word:")
# res=count_vowel(txt)
# print(res)

# #count consonanta
# def count_consonant(text):
#     vowels=["a","e","i","o","u"]
#     count=0
#     for i in text:
#         if i not in vowels:
#             count+=1
#     return count
# txt=input("enter the word: ")
# res=count_consonant(txt)
# print(res)

# #reverse string
# def reverse_string(text):
#     return text[::-1]
# txt=input("enter the word: ")
# res=reverse_string(txt)
# print(res)


#palindrome checker
# def palindrome(text):
#     p=text[::-1]
#     if text  in p:
#         return "palindrome"
#     else:
#         return "not palindrome"
# txt=input("enter the word: ")
# res=palindrome(txt)
# print(res)

# #count words
# def count_word(sentence):
#     sen=sentence.split(" ")
#     count=0
#     for i in sen:     #we can simply use len(sen)
#       count+=1  
#     return count
# txt=input('enter the word: ')
# res=count_word(txt)
# print(res)

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
    