
#break statement immediately stops the loop and moves execution to the first statement after the loop
for i in range(1,6):
    if i==4:
        break
    print(i) 

for i in range(1,11):
    if i==7:
        break
    print(i)

#stops when "o" appears
s="python"
for i in s:
    if i=='o':
        break
    print(i)

n=[23,45,24,67,-89,45,69]
for i in n:
    if i==-89:
        break
    print(i)

#first number divisible by 7 from 1 to 50
for i in range(1,51):
    if i%7==0:
        print(i)
        break 


for i in range(1,101):
    print(i)
    if i%13==0:
     break
#first even number and greater than 25
for  i in range(1,51):
    if i%2==0 and i>25:
        print(i)
        break

#finding a value and stops
l=["paper","pen","pepper","pencil"]
for i in l:
    if i=="pepper":
        break

    print(i)
print("found")

  
  #multiplication table of 5 and stops when result exceeds 30
n=5
for i in range(1,11):
    if i*n==30:
        break
    print(n,"x",i,"=",n*i)  


#continue statement skips the current iteration and moves to the next iteration of the loop
for i in range(1,11):
    if i==5: #skips 5
        continue
    print(i)

#print 1 to 20 and skip even numbers
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

#print 1 to 15 skips multiple of 3
for i in range(1,16):
    if i %3==0:
        continue
    print(i)


#skip t
d="python"
for i in d:
    if i=="t":
        continue
    print(i)

#skips negative number
n=[23,45,24,67,-89,45,69]
for i in n:
    if i==-89:
        continue
    print(i)

#counting odd numbers from 1 to 20
count=0
for i in range(1,21):
    if i%2==0:
        count+=1
        continue
print(count)

#print numbers from 1 to 30, skip num divisible by 2 and 3
for i in range(1,31):
    if i%2==0 and i%3==0:
        continue
    print(i)

#from list print only grater than 50
l=[56,78,90,89,34,22,33]
for i in l:
    if i<=50:
        continue
    print(i)

s="window"
vowels="aeiou"
for i in s:
    if i==vowels:
        continue
    print(i)