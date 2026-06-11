#loops help us to repeat the code multiple times

#for loop : used when we know how many times to repeat

for i in range(5):
   print("hello world")

#for loop to print 1 to 10
for i in range(1,11):
    print(i)

a=5
for i in range(a):
    print(i)

# for  loop to check even number
for i in range(1,11):
    if i%2==0:
        print("even: ",i)

#another way to print even number
for i in range(2,11,2):
    print(i)

#for loop to print odd number
for i in range(1,11):
    if i%2!=0:
        print("odd: ",i)
#another way to print odd  number
for i in range(1,11,2):
    print(i)

#reverse numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

# sum of even numbers from 1 to 50

total=0
for i in range(1,51):
    if i%2==0:
      total=total+i
print(total)

#sum of numbers from 1 to 20
total=0
for i in range(1,21):
    total=total+i
print(total) 
#count even and odd numbers
#even_count=0
#odd_count=0
#for i in range(1,11):
 #a=int(input("enter a number: "))
 #if a%2==0:
  #  even_count+=1
 #else:
 #      odd_count+=1      
#print("even:",even_count)
#print("odd:",odd_count)


#product of a number
prod=1
for i in range(1,6):
    prod=prod*i
print(prod)

#factorial of a number
a=int(input("enter a number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

#printing a table
a=int(input("enter a number: "))
for i in range(1,11):
    print(a,"x",i,"=",i*a)

#print all multiple 0f 3 between 1 to 50
n=3
for i in range(1,51):
    if i%3==0:
        print(i)

#square of numbers from 1 to 10
for i in range(1,11):
    print(i*i)

#sum of nummbers from  1 to n
n=int(input("enter a number: "))
total=0
for i in range(1,n+1):
    total+=i
print(total)


#nested for loop
#prime numbers between 1 to 50
for num in range(2,51):
   count=0
   for i in range(1,num+1):
        if num%i==0:
            count+=1
   if count==2:
        print(num)


#sum of factorials
for num in range(1,6):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
print(fact)

#pattern numbers
for i in range(1,6):
    for  j in range(1,i+1):
        print(i,end="")
    print()

#print pattern 
for i in range(1,6):
    print("*"*i)



#while loop
#while loop is used when we don't know how many times, we repeat until condition becomes false
#while loop to print 1 to 5

i=1
while i<=5:
    print(i)
    i+=1

#while to check even numbers upto 20
i=2
while i<=20:
    print(i)
    i+=2

#check odd numbers to upto 20
i=1
while i<=20:
    print(i)
    i+=2

# printing a table using while loop 
i=1
num=int(input("enter a number: "))
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

# sum of a number 
total=0
i=1
while i<=5:
    
    total=total+i
    i=i+1
print(total)

#sum of even number
i=2
total=0
while i<=20:
    total+=i
    i=i+2
print(total)




#reverse numbers from 10 to 1
i=10
while i>=1:
    print(i)
    i
    i-=1

#reversing a number
n=3456
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed num: ",rev)

#palindrome 
n=12321
rev=0
original=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed",rev)
if original==rev:
    print("palindrome")
else:
    print("not palindrome ")

#count digits in a number
n=234545
cout=0
while n>0:
    digit=n%10
    count+=1
    n=n//10
print(count)

#multiple of digits in a number
n=56
product=1
while n>0:
    digit=n%10
    n=n//10
    product*=digit
print(product)

#largest digit in a number
n=9675
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print(largest)

