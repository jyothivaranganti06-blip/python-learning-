#dictionary  is a collection of data stored as key-value pair

#creating and accessing dictionary elements
student={"name":"james","age":20,"course":"cse"}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])
print(student.get("name"))  #using get()

#adding items
student={"name":"jay"}
student["age"]=24
print(student)

#updating an item
student={"name":"sana","age":28}
student["age"]=29
print(student)

#removing  items
#pop()
std={"name":"shinchan","age":5}
std.pop("age")
print(std)

#del()
std={"name":"kazhama","age":5}
del std["age"]
print(std)

#dict length
std={"name":"david","age":25,"region":"USA"}
print(len(std))

#loops through dictionary
student={
"name":"juhoon",
"age":18
}
for key in student:
    print(key)

for value in student.values():
   print(value)
for key, value in student.items():
    print(key,value)

#Built-in methods in dictionary 

student={"name":"james","age":20}
print(student.keys()) #return all keyks
print(student.values()) #returns all values
print(student.items()) #return all among with keys and values
print(student.get("name")) #return values safely
print(student.pop("age")) #removes item
print("after removing age:",student)
student.update({"age":20}) #updates dictionary
print("afer updating age:",student)
print(student.copy()) #copy the dictionary
print(student.clear()) #removes all items
keys=["a","b","c","d"]
d=dict.fromkeys(keys,0) #create a new dictionary from the iterable with the values equal to value
print(d)
g={"a":1} 
print("a"in g)
d={"name":"david"}
d.setdefault("age",20) #it is used to set the key to the default value if the key 
#is not declaredd in the dictionary
print(d)

#nested dictionary 
students={"s1":{"name":"james","age":20},
          "s2":{"name":"juhoon","age":18}}
print(students["s1"]["name"])
print(students["s2"]["age"])

#dictionary comprehension 
square={x:x*x for x in range(2,6)}
print(square)

#practice problems

#creating a dict with name,age,course
#basic problems
student={"name":"jay","age":24,"course":"computer science"}
print(student)
#print all keys
print(student.keys())
#print all values
print(student.values())
#add a new key called "city"
student["city"]="australia"
print(student)
#update age
student.update({"age":25})
print(student)
#remove one key using pop()
print(student.pop("city"))
print("after removing city:",student)
#find the length of dictionary
print(len(student))
#check if a key exists
print("age" in student)
#print all key-value pair
print(student.items())
#clear dictionary
print(student.clear())
#intermediate problems
#count frequency of character in a string 
#using if-else method
s="apple"
freq={}
for i in s:
    if i  in freq:
      freq[i]=freq[i]+1 #if "a" in freq it count plus
    else:
       freq[i]=1 #if "a" appears once it counts once
print(freq)

#using get() method
s="apple"
freq={}
for i in s:
   freq[i]=freq.get(i,0)+1
print(freq)

#count frequency of words in a sentence
sen="python is a programming language it is a easy programming language"
s=sen.split(" ")
print(s)
freq={}
for i in s:
   if i in freq:
      freq[i]+=1
   else:
      freq[i]=1
print(freq)

#find the student with highest marks
marks={"A":34, "B":99,"C":98}
highest_student=""
highest_marks=0
for student in marks:
   if marks[student]>highest_marks:
      highest_marks=marks[student]
      highest_student=student
print("highest marks:",highest_marks)
print("student:",highest_student)
#sum all values in a dictionary
val={"a":5,"b":8,"c":3}
v=val.values()
print(v)
total=0
for i in v:
   total+=i
print(total)
#create a dic of numbers and their squares from 1 to 10 
sqr={}
for i in range(1,11):
   sqr[i]=i*i
print(sqr)
#merge two dictionaries
d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5,"f":5}
d3=d1|d2 #union operator
print(d3)
#find keys whose values are greater than 20
d={"a":2,"b":56,"c":45,"d":12,"e":59}
for key in d:
   if d[key]>20:
      print(key)
#reverse a dictionary
d={"a":1,"b":2,"c":3}
reverse={}
for key  in d:
   reverse[d[key]]=key
print(reverse)
#nested dictionary for 3 students
student={"s1":{"a":1,"b":2},
         "s2":{"c":3,"d":4},
         "s3":{"e":6,"f":7}}
print(student)

#count vowels in a string using a dictionary
s="union"
freq={}
for i in s:
    if i in  "aeiou":
       if   i in freq:
        freq[i]=freq[i]+1
       else :
         freq[i]=1
print(freq)

s="bEautIful"
txt=s.lower()
vowels={}
for i in txt:
    if i in "aeiou":
       vowels[i]=vowels.get(i,0)+1
print(vowels)

#advanced problems
#find duplicates in a dictionary
d={1:"a",2:"a",3:"e",4:"t",5:"t"}
seen=[]
dup=[]
for i in d.values():
   if i in seen: # it checks if a value is in seen list 
     if i not  in dup:#again if a value is already in seen list it goes to the dup list
        dup.append(i) #adds every value at the last
   else:
        seen.append(i)    
print(dup)

#sort a dictionary values
d={"d":2,"s":1,"a":3}
srt=[]
s=(sorted(d.values()))
srt.append(s)
print(srt)

#sort dict by keys
d={"a":1,"c":4,"b":3,"d":2}
srt=[]
srt.append(sorted(d.keys()))
print(srt)

#find the key with the second highest value
d={"a":34,"b":54,"c":23}
srt=sorted(d.values())
large=max(srt)
r=srt.remove((large))
print("second maximum value:", max(srt))
for key in d:
      if d[key]== (max(srt)):
         print( "second maximum key:",key)


#another method
d={"a":34,"b":54,"c":23}
values=list(d.values())
values.sort()
second_highest=values[-2]
for key in d:
    if d[key]==second_highest:
       print("second highest key:",key)
       print("second highest value:",second_highest)
#remove duplicate values get with key_value pair 
d={"a":90,"b":30,"c":90}
seen=[]
new_dict={}
for key in d:
   if d[key]  not in seen:
      seen.append(d[key])
      new_dict[key]=d[key]
print(new_dict)
#create a nested dictionary of students and marks
students={"alice":{"maths":90,"science":89},
          "david":{"maths":87,"science":90}}
print(students["alice"]["science"])
print(students["david"]["science"])

#calculate the average marks of all students
marks={"a":34,"b":56,"c":58,"d":90}
average=(sum(marks.values()))/len(marks)
print("average marks of all students:",average)

#find the students who scored greater than the average score
marks={"a":34,"b":56,"c":58,"d":90}
average=(sum(marks.values()))/len(marks)
print("average marks of all students:",average)
for key in marks:
   if marks[key] > average:
      print(key)
#convert two list into one dictionary
keys=["a","b","c","d"]
values=[1,2,3,4,5]
a=zip(keys,values) #combines elements from multiple iterables (like lists or tuples)element-wise into a single iterator of tuples
print(dict(a))

#invert a dict while handling duplicates
d={"a":90,"b":34,"c":90,"d":90,"e":45}
new={}
for key in d:
   value=d[key]
   if value not in new:
      new[value]=[]
   new[value].append(key)
print(new)

#Bonus challenges
#count the frequuency of every word in the paragraph
text="'python is a programming language , the programming language is easy to understand and to write'"
text=text.split()
print(text)
freq={}
for word in text:
    if word in freq:
       freq[word]=freq[word]+1
    else:
       freq[word]=1
print(freq)

#group names by their first letter
d=["alice","paro","ayush","aditya","kaira","krishna"]
g_name={}
for name in d:
   first=name[0]
   if first  not in g_name:
      g_name[first]=[]
   g_name[first].append(name)   
print(g_name)
#first non-repeating character
s="programming"
count={}
#count frequency
for i in s:
   if i not  in count:
      count[i]=1
   else:
      count[i]+=1
#find first non-repeating character
for i in s:
   if s.count(i) == 1:
       print("non-repeating characters",i)
       break
   
#dictionary comprehension
#squaring
square={i : i*i for i in range(1,6)}
print(square)

num=[2,3,1,4]
a={ i for i in num if i%2==0 }
print(a)

a={i for i in range(1,6) if i%2==0 }
print("even:",a)   

d={i for i in range(1,21) if i>5 and i%4==0}
print(d)

#popitem()
d={1:"rahul",2:"raghu",3:"david"}
print(d.popitem())
print(d)
#sorting  
print(sorted(d.keys()))
print(sorted(d.values()))
print(sorted(d.items()))