 ##### strings #######

#string is the collection of characters surrounded by the single quotes,double quotes,triple quotes
#the computer does not understand the characters;internally,it stores manipulated character 
# as the combination of the 0's and 1's

str1='hello python' #using single quotes
print(str1) 

str2="helloworld" #using double quotes
print(str2)

str3="""triple quotes are generically used for represent the multiline or docstring """
print(str3) #using triple quotes


#storing string in variables
my_str="sun is shinning"
print(my_str)

#string concatination
str1="sun"
str2="moon"
print(str1 + str2)

#easy way to concatinate
print("sun"+"moon")


#length of string
length=len("surprise")
print(length)

colors=['red','blue','green']
print(len(colors)) 

#string max(); returns the ,maximum alphabetical character from the string
str1="the sky looks beautifull"
print(max(str1))

#string min();returns the minimum alphabetical character from the string
str2="apple"
print(min(str2))

str1="the-sky-looks-beautifull" #returns a symbol which is the minimum character of that string 
str2="theskylooksbeautifull" #returns the "a" which is minimum character of that string
print(min(str1))
print(min(str2))

#equal to
print("sun"=="moon") #false
print("moon"=="moon")#true

#not equal to
print("moon"!="sun") #true
print("moon"!="moon") #false

sorted
str1="natural-disaster"
print(sorted(str1))

#using relational operators
print("peek"=="peek") #true
print("Peek"<"peek")#true
print("Peek">"peek")#false
print("peek"!="peek")#fasle

#using is and is not
str1="Peek"
str2="peek"
str3=str1
print("ID of str1=",hex(id(str1))) #it converts an integer to hexadecimal string
print("ID of str2=",hex(id(str2)))
print("ID of str3=",hex(id(str3)))
print(str1 is str1)
print(str1 is str2)
print(str1 is str3)
str1+="s"
str4="peeks"
print("\nID if changed str1=",hex(id(str1)))
print("ID of str4=",hex(id(str4)))
print(str1 is str4)

#string indexing and splitting
#the indexing opeator selects a single character from a string. 
# the characters are accessed by their position or index value.

str="python"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5]) 
print(str[0:6])
print(str[0:3])
print(str[2:6])
print(str[:4])

#string operators

str1="hello"
str2="world"
print(str1+str2)
print(str1*3)
print(str1[0])
print(str2[1:3])
print('w'in str1)
print('wo' not in str1)
print(r'c://python37')
print("the string str1:%s"%(str1))

#string slicing

#using slice constructor
string1="ASTRING"
s1=slice(3)
s2=slice(1,6,2)
s3=slice(-1,-122,-2)
print("string1 slicing")
print(string1[s1])
print(string1[s2])
print(string1[s3])

#using indexing sequence
string2="ASTRING"
print(string2[:3])
print(string2[1:5:2])
print(string2[-1:-12:-2]) 
print("\nreversing string")
print(string2[::-1])

#joining
ex:1
str=":"
list=['2','3','4']
str2=str.join(list)
print(str2)

ex:2
str="  "
list=['p','y','t','h','o','n']
str2=str.join(list)
print(str2)

ex:3
str="->"
list=["java","python","c"]
str2=str.join(list)
print(str2)

ex:4
dict={'key1':1,'key2':2,'key3':3}
str='&'
str=str.join(dict)
print(str)

#string split()
text="cindrilla is a cute girl"
words=text.split()
print(words)

cars='audi and kia and BMW and volvo and dog'
print(cars.split('and',1))
print(cars.split('and',2))
print(cars.split('and',3))
print(cars.split('and',4))

#strings are immutable
name1="arjun"
name2="t"+name1[1:]
print("name1=",name1,"name2=",name2)

#string methods
var="python" 
print(var.capitalize()) #capitalize the first word
var="pyThOn" 
print(var.casefold()) #convert to casefolded string
print(var.center(20)) #pads string with specified character
var="selection"
print(var.count('e')) #counts the occurence
print(var.encode())
print(var.endswith(var))
print(var.expandtabs())
var="TechBeamers"
str='Beam'
print(var.find(str))
print(var.index(str))
print('python'.isalnum())
print('pythhon'.isalpha())
num=u'2016'
print(num.isdecimal())
v='python'
print(v.islower())
v='PYTHON'
print(v.isupper())
num=u'2016'
print(num.isnumeric())

#string problems : beginner level
#length of string
var="python"
print(len(var))
#convert to uppercase
var="python"
print(var.upper())
#convert to lowercase
var="PYTHON"
print(var.lower())
#reverse string
var="elephant"
rev=var[::-1]
print(rev)
#check palindrome
v="madam"
rev=v[::-1]
if v==rev:
    print("palindrome")
else:
    print("not palindrome")
#count vowels
var="programming"
#vowels="aeiou"
count=0
for i in 'aeiou':
    if i in var:
        count+=1
print(count)
#count consonants
var="programming"
vowels="aeiou"
cons=[]
count=0
for i in var:
    if i not in vowels:
        
        cons.append(i)
        count+=1
print(cons)      
print(count)
#character's frequency
x="banana"
print(x.count('a'))
#replace a word
v="python is a programming language"
print(v.replace("python","java"))
#remove spaces
var="hello world"
print(var.replace(" ",""))

#intermediate level
 #find duplicate characters
v="programming"
dup=[]

for i in v:
     if  v.count(i)>1 and i not in dup:
          dup.append(i)
print(dup)
 #count words in sentence
a="i learned python "
e=(a[0:1],a[2:9],a[10:16]) # an easy way using split: print(a.split(" "))
count=0
for i in e:
   count+=1  
print(count)
#count  the  non repeating characters
v="aabbcdde"
for i in v:
    if v.count(i)==1:
        print(i )
#removes duplicates characters
v="programming"
dup=[]
count=0
for i in v:
    if  i not in dup: #preserves order
    
       dup.append(i)
print("".join(dup)) #convert list into string

#another example
c="banana"
d=[]
for i in c:
    if i not in d:
        d.append(i)
print("".join(d))
#another example
e="mississippi"
d=[]
for i in e:
    if i not in d:
        d.append(i)
print("".join(d))

#checks if two strings are anagrams
a="listen"
b="silent"
print(sorted(a))
print(sorted(b))
if sorted(a)==sorted(b):
        print("anagrams")
else:
      print("not")  

 # find the largest word in a sentence
a="i like programming language"
spl=a.split()
largest=spl[0]
print(spl) 
for i in spl:
    if largest < i:
        largest=i
print(largest)

#count digit,alphabet
a="abc123@"
letters=0
num=0
character=0
for i in a:
   if i.isalpha():
    letters+=1
   elif i.isdigit():
     num+=1
   else: 
     character+=1
print("Letters=",letters)
print("Numbers=",num)
print("Characters=",character)      

#remove all vowels
a="programming"
vowels="aeiou"
d=""
for i in a:
    if  i not in vowels:
        d+=i
print(d)

#capitalize the first letter of each word       
a="hello world"
words=a.split(" ")
result=""
for word in words:
        result+=word.capitalize() +" "
        print(result) 
        

a="hello bro"
r=a.split()
res=""
for i in r:
        res+=i.capitalize() + " "
        print(res) 
                
b="python code"
print(b.title())

#check whether a string only contains digits
s="12345"
print(s.isdigit())   

#string formatting
age=34
print(f"iam rocky i'm {age} years old")

name="jake"
age=23
print(f"hii i'm {name}, i'm {age} years old")

