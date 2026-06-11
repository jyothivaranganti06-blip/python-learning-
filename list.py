
list=["jyothi","sampath","vishu"] # a simple list
print(list)

items= [1,"bread",2,"mango",36,768,"milk",True]   # a list with heterogeneous data 
print(items)


# accessing list items using an index
names=["pandu","abhi","vibhav"]
print(names[0])
print(names[2])
                  #print(names[6]) throws anindexerror : list index out of range


# a list can contain multiple inner list as items that can be accessed using indexes 
num=[1,2,3,[3,4,5,[7,]],6]
print(num[4])
print(num[3][2])
print(num[3][3])


# updating the list items
# update list using apend or insert 
names=["james","keonho","martin","juhoon"]
names.append("seonhong") # append add an item at the end of the list 
names[0]="namjoon"
names[2]="jungkook"
names.insert(3,"jin")
print(names)

# removing items from the list
# using the remove(),pop() methods,or del  keyword to delete the list items 
twice=["tyuzu","mina","sana","momo","dahyun","jihyo","chaeyoung","nayeon","jeongyeon"]
del twice[2]  # del keyword use the list name"twice",with an index
print("after using del keyword: ",twice)
twice.remove("chaeyoung")  # remove method use the list item"chaeyoung to remove an item
print("after using the remove method: ",twice)
print(twice.pop(1))  # pop method usee the list index
print("after using the pop method: ",twice)

# list operations 


l1=[1,2,3,4]
l2=[5,6,7,8]
#the"+"  symbol concatinate the list 
print(l1+l2)
# the "*" symbol multiple the list 
print(l2*2)
# slice operator"[]"  is return the item at given index 
a=l1[3]
print(a)
# the negative index "-1" counts the position from the right side
c=l2[-1]
print(c)
print(l2[2])
print(l1[-2])
print(l2[-3])

# the range slice operator [fromIndex : untill index ]
li=[8,3,7,4,6,2,9,5]
print(li[:1])
print(li[1:])
print(li[:3])
print(li[1:3])
print(li[3:7])
print(li[-6])
print(li[-6:-2])
print(li[-4:-1])
print(li[-2:])
print(li[:-2])
print(li[-2:]+li[:-2])


# "in" operator return true if the given index is exesting in the list
l=[4,6,9,8,3,3]
print(l)
print(3 in l)
print(10 in l)


# "not in" operator return true if a given index is not exist in the list
k=[3,4,5,6,7]
print(4 not in k)
print(10 not in k)


# LIST METHODS 
lm=[5,6,5,4,3,2,3,1]
lm.append(0)
print(lm)
print(lm.count(3))
lm.extend([9,76,98])
print(lm)
lm.insert(8,10)
print(lm)
print(lm.pop(2))
print(lm)
lm.remove(4)
print(lm)
k=lm.copy()
print(k)
lm.reverse()
print(lm)
lm.sort()
print(lm)
lm.sort(reverse=True)
print(lm)
print(lm.index(0))
lm.clear()
print(lm)


#"CHAT GPT SUNBEANIM"🫡("SAVIOUR")

# create a list
fruit=["apple","mango","banana","strawberry","custered apple","pomogranate","guava"]
print(fruit)

#access elements
print(fruit[0])
print(fruit[6])
#change element
fruit[0]="grapes"
print(fruit)
# adding element
fruit.append("orange") # using append
print(fruit)
print(fruit.insert(2,"papaya")) # using innsert 
print(fruit)
# removing elements
fruit.remove("grapes") # using remove
print(fruit)
fruit.pop(4) # using pop
print(fruit)
# find length
print(len(fruit))
# check elements exists
print("banana" in fruit)
print("banana" not in fruit)
print("grapes" not in fruit)
# sum of list 
m_li=[2,3,4]
s=0
for i in m_li:

  s=s+i
print(s)

l=[8,9,6,1]
# finding largest number
print(max(l))
# finding smallest number
print(min(l))

# even or odd
l=[3,2,5,6,8]
for i in l:
  if i%2==0:
    print("even :",i)
  else:
     print( "odd:",i)


# count of even and odd
s=[3,4,5,69,9]
even=0
odd=0
for i in s:
    if i%2==0:
      even=even+1
      print("count of even: ",even)
    if i%2!=0:
         odd=odd+1
print("count of odd:" , odd)

# reversing the list
s.reverse()
print(s)

# removing the duplicates
num=[2,6,2,4,4,5,6,7,9,8,70]
n_l=[]
for i in num:
   if i not in n_l:
      n_l.append(i)
print(n_l)

#second largest number
k=[2,34,55,67,22]
max_v=max(k)
k.remove(max_v)
print(max(k))

#merge two list
j=[3,4,5]
k=[5,6,7]
l=[j+k]
print(l)

# find frequency of elements
l=[6,7,88,5,7,88,6,7,4,6,]
check=[]
for i in l:
   if i not in check:
       l.count(i)
       print(i,"->",l.count(i),"times")
   check.append(i)
print(check)


#sort without sort() method
# bubble sorting 
l=[3,6,3,1,4,8,7,6,9]
for i in  range (len(l)):  # go through the list  "this repeats the sorting process multiple times"
   for j in range(len(l)-1):  # this checks adjucent elements "compare index 0 and 1"
      if l[j]>l[j+1]:  # comparison "check if the element is grater then the other element"
         temp=l[j]   # "if number is greater it swaps the number"
         l[j]=l[j+1]
         l[j+1]=temp
         print(l) # prints the bubble sorting process 

# rotating a list
l=[1,2,3,4,5]
print(l[-2:]+l[:-2])# "[-2:] gives the last two digits and [:-2] gives the first numbers until the last 2 elements"

# find common elements
a=[2,3,45,6] 
b=[45,3,7,9]
common=[]
for i in a: # go through the list "all elements in the a"
    if i in b: # checks if the same elements are in the second list"b" 
      common.append(i) # if " if condition" is true , append adds the same elements found in a and b in the common list
print(common) # prints the new common list


# seperate positive and negative numbers 
l=[-4,3,-5,6,-6,7,-8,9,-10,-11,56,76]
positive=[]
negative=[]
for i in l: # travel  through the list 
  if i>=0: # checks the positive and negative 
     positive.append(i) # positive numbers are added to positive list
  else:
       negative.append(i) # negative numbers are added to negative list
print("positive:" ,positive)
print("negative: " ,negative)



# adding the sum of two numbers
nums=[2,3,4,6]
target=8
for i in range(len(nums)):
 for j in range(i+1,len(nums)):
       
  if nums[i]+nums[j]==target:
      print(i,j)
     

#move zeros to end of the list
l=[2,0,3,6,0,8,0,5,0,2]
zero=[]
non_zero=[]
for i in l:
   
     if i ==0:
      zero.append(i)
     else:
        non_zero.append(i)
result=non_zero+zero
print(result)


#finding missing number in a list
l=[1,2,4,5]
total=0
actual=0
for i in range(1,6):
  total=total+i
for j in l:
 actual=actual+j
missing=total-actual
print(j)
print("actual:" ,actual)
print("sum:",total)
print("missing: ",missing)



#seperating the duplicates
l=[2,4,5,5,6,4,3,1,2,1]
check=[]

for i in l:
   if i  in check:
      print(i)
   else:
      check.append(i)
  


l=[1,2,3,4]
p=[]
for i in range(len(l)):
   for j in range( i+1,len(l)):
      if i !=j:
         
         p.append(l[i]*l[j])
print(p)
      

print("count")
#count positive numbers
l=[1,2,-7,4,-5,-8]
count=0
for i in l:
 if i >0:
   
   count=count+1 
print(count)


print("ne")
n=[-9,-8,-6,-4,2,5]
total=0
for i in n:
 if i<0:
   total=total+1
print(total)

p=[100,200,50,300,500]
maximum=p[0]
for i in p:
    if i>maximum:
        maximum=i
print("maximum: ",maximum)


k=[100,23,44,55,6]
min=k[0]
for i in k:
   if i<min:
      min=i
print("minimum: ",min)

#sum of even numbers
j=[1,2,4,8,6,3,]
t=0
for i in j:
   if i%2==0:
      t=t+i
print("sum of even: ",t)

# sum of odd numbers
h=[2,4,3,5,9,13]
o=0
for i in h:
   if i%2!=0:
      o=o+i
print("sum of odd num: ",o)

# product of all elements
d=[1,2,3,4]
product=1
for i in d:
   product=product*i
print("product of elements: ",product)

# avg of all elements in a list
a=[2,3,4,5]
s=0
avg=0
for i in a:
   avg=s=s+i/len(a)
print("average: ",avg)

#greater than 50
g=[23,56,78,90,32]
for i in g:
   if i > 50:
    print("greater than 50: ",i)


#find all even numbers
e=[2,3,7,5,6,8]
for i in e:
   if i%2==0:
      print("even nums: ",i)


#swap fisrt and last elements
s=[1,2,3,4,5]
a=s[0],s[-1]=s[-1],s[0]
for i in s:
 print(i)

# remove all occurence of elements
l=[1,2,2,3,2,4]
o=[]
target=2
for i in l:
    if i!=target:
      o.append(i)
print("occurence:",o)

# another wayn of removing occurences but it repeatedly shows target value
l=[1,2,2,3,2,4]
target=2
for i in l:
    if i==target:
     l.remove(target)
print("occurence:",l)


# checking palindrome
p=[1,2,3,2,1]
l2=p[::-1]
if p==l2:
    print("palindrome: ")
else:
   print("no")


#checkinng the unique elements
q=[1,2,2,3,4,4,5]
unique=[]
for i in q:
   if q.count(i)==1:
       unique.append(i)
print( "unique: ",unique)


#splitting the list into 2 equal parts
l=[2,3,4,5,6]
mid=len(l)//2
m=len(l)/2
print(mid)
print(m)
print(len(l))
print(l[:mid])
print(l[mid:])



#adding the sum of target value
s=[2,3,4,5,6]
t=11
for i in s:
   for j in range( i+1,len(s)):
      if s[i]+s[j]==t:
        print(s[i],s[j])


#converting negative numbers into positive numbers
w=[-23,5,-500,-100]
for i in w:
   if i<0:
      print(i*-1)


#removing empty string
s=["jyo","","vish","sam","","pinky"]
e=[]
for i in s:
   if i!="":
      e.append(i)
print(e)



#printing all elements from the nested llist
o=[[12,23,34],[35,56,78,],[90]]
print(o)
print(o[:])


r=[[23,12,32],[45,34,5],[47,89,79]]
print([sum(i)for i in r ])


# printing all nested list elements  using the nested loops
v=[[3,2],[9,6]]
for i in v:
   for j in i:
      print(j)


#printing the sum of all elements using nested loops
d=[[23,4,5],[67,89,90]]
total=0
for i in d:
   for j in i:
      total=total+j
print(total)


#printing the largest number from the nested list
f=[[23,34,56],[90,89,67]]
l=f[0][0]
for i in f:
   for h in i:
      if h>l:
         l=h
print("largest: ",l)


#counting the elements in nested list
t=[[23,34,56],[90,89,67]]
count=0
for i in t:
   for j in i:
    count=count+1
print("count:",count)



# matrix addition

t=[3,4,5]
y=[6,7,8]
b=[]
for i in range(len(t)):
    b.append(t[i]+y[i])
print("matrix of the list:",b)

# LIST COMPREHENSSION 
# list comprehenssion is a short and concise way to create lists in python
# cretaing a list of squares in list comprehenssion
squares=[i**2 for i in range(1,6)]
print(squares) 

#converinng string to the uppercase
words=["apple","papaya","mango"]
result=[word.upper() for word in words]
print(result)   

#using if condition 
numbers=[6,8,9,4]
result=[num  for num in numbers if num%2==0  ]
print(result)


#checking numbers greater then 10
q=[23,5,6,77,89,98,1]
res=[val for val in q if val>10]
print( "greater then 10:",res)

#creating a list from a range
f=[i for i in range(11)]
print("numbers:",f)

#using nested loops
c=[(x,y) for x in range(3) for y in range(3)]
print("nested loops:",c)

#flatting a list of lists
r=[[1,2,3],[4,5,6],[7,8,9]]
res=[val for row  in r for val in row ]
print(res)

#list comprehension with string 
word="strawberry"
vowel="aeiou"
res=[char for char in word if char in vowel]
print(res)

#nested list comprehension 
h=[[i*j for i in range(1,6)]for j in range(2,5)]
print(h)


num_l=[y for y in range(100) if y%2==0 if y%5==0]
print("numbers that are divisible by  2 and 5:",num_l) 


#dictionary from two list using zip()
states=["telanagana","andra pradesh"]
capitals=["hydarabad","amaravathi"]
d={states:capitals for states,capitals in zip(states,capitals)}
print(d)


#checking a length of a list is even or not
fruits=["banana","mango","strawberry"]
word_len={word:len(fruits) for word in fruits if len(word)%2==0}
print(word_len)


#?????????????????
matrix=[[1,2,3],[4,5,6],[7,8,9]]
filtered=[row[1] for row in matrix if row[1]%2==0]
print(filtered)

matrix=[[1,2],
        [3,4],
        [5,6]]
transpose=[]
for j in range(len(matrix[0])):
       new_row=[]
       for i in range(len(matrix)):
          new_row.append(matrix[i][j])
       transpose.append(new_row) 
   
print("transpose",transpose)

#square using list comprehension
r=[i**2 for i in range(1,6) ] #we can use i*i to get the square
print(r)

f=[i**3 for i in range(1,4)]
print(f)

#even numbers using list comprehension
g=[45,76,65,98]
res=[i for i in g if i%2==0]
print(res)

#length of string
i=[2,3,4,5]
res=[len(i)]
print(res)



#indexing  and slicing the list 
l=[4,3,2,5,6,8,9,5,7]
print(l[2:6])
print(l[-5:-2])
print(l[0:6:2])

#write python program to add two matrices 
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[2,3,4],[5,6,7],[8,9,7]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)): # len(x)=3
     for j in range(len(x[0])):# len(x[0])=1
        result[i][j]= x[i][j] +y[i][j]
for r in result:
   print(r) 


#converting negative number to positive using abs built-in function
f=[-23,-45,-67,-90]
res=[abs(i) for i in f] #abs function  returns the absolute value of specific number, effectively reemoving its negative sign 
print(res)


#length of every word in  a list using list comprihension and len() keyword
s=["python","java","oracle","json"]
res=[len(i) for i in s]
print(res)


#ascening order without using sort method
w=[2,5,6,78,5]
for i in range(len(w)):#i=>w[0]--->i=0-->5
  for j in range( i+1, len(w)):#i+1 so j=i+1 ----> j=1---.j=2 checks 5>2
     if w[i] > w[j]:
         w[i],w[j]=w[j],w[i]
print(w)

#descending order wothout using sort
r=[23,45,76,9,1,22]
for i in range(len(r)): #length of list is shows in an index manner
   for j in range(i+1,len(r)): #to check the next value put i+1 so, j index becomes 1 then i=0 ,j=1
      if r[i]<r[j]: 
         r[i],r[j]=r[j],r[i]
print(r)


#sorting the words(alphabetic)
a="apple"
b="banana"
print(sorted(a))
print(sorted(b))
res="".join(sorted(a))
print(res)#gives the string instead of list 
print(sorted(a,reverse=True))#gives descending order in list form 
print("".join (sorted(a,reverse=True)))#gives descending order in string form



#sorting words with their length
r=["sugar","salt","pepper","chilli"]
for i in range(len(r)):
   for j in range(i+1,len(r)):
      if len(r[i])>len(r[j]): #compare the words length to know the highest length
         r[i],r[j]=r[j],r[i]
print(r)



#linear search 
g=[34,67,90,23,68]
target=g[1]
s=[]
for i in range(len(g)):
   if g[i]==target:
      s.append(i)
print(s)

#binary search 
b=[23,4,5,6,7]
low=0
high=4
mid=low+high
mid=int(mid/2)
print("index:",mid)
print("value",b[mid])

#count occurrences
j=[2,6,6,7,6,6,6]
target=6
count=0
for i  in j:
   if i==target:
      count=count+1
print( "count of target:",count)

#sum of two
u=[3,4,5,6,7,9]

target=11
for i in range(len(u)):
   for j in range(i):
    if u[i]+u[j]==target:
       
     print(u[i],u[j])


#longest word
f=["soure","sweet","salty","bitter"]
longest=f[0]
for i in f:
    if len(i)>len(longest):
       longest=i
       print(len(longest))

#removing dup
d=[3,4,5,4,3,2,3,4]
new=[]
for i in  d:
   if i not in new:
      new.append(i)
print(new)      

#second largest
o=[34,5,57,67]
max_va=max(o)
o.remove((max_va))
print(max(o))

#rotating a list by right
f=[5,4,3,2,1]
print(f[-1:]+f[:-1])

#rotating a list by left
f=[5,4,3,2,1]
print(f[1:]+f[:1])

#merge sorted list
f=[9,3,4]
g=[5,8,2]
merge=f+g
print(sorted(merge))

#zip()
name=["a","b","c"]
marks=[2,3,4]
for name,marks in zip(name,marks):
   print(name,marks)

#all()
print(all([True,1,"hello"]))
print(all([False,0,"hello"]))
print(all([]))

#any()
print(any([False,True,False]))
print(any([False,False,False]))
print(any([]))


#list to tuple
my_list=[1,2,3,"apple"]
my_tuple=tuple(my_list)
print(my_tuple)

#list to set
d=[4,5,6,"banana"]
s=set(d)
print(s)






    
     
  

    




  





