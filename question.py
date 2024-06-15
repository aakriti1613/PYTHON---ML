#****ques.1*****
a=input("first no.: ")
b=input("second no.: ")
sum=int(a)+int(b)
print(sum)

#****ques.2*****
number=int(input("enter no.: "))
if (number % 2==0):
    print(f'{number} is an even number')
else:
     print(f'{number} is an odd number')   

#****ques.3*****
def fact(num):
   if num==1 or num==0:
     return 1
   elif num<0:
     return 0
   else:
      factnum= num * fact(num-1)
      return factnum
   
factorial=fact(number)
print(factorial)

#****ques.4,8*****
name=input("enter name: ")
greet="Hello, Good morning "
print(greet+name)  #**ques.8 concatenation***

#****ques.5,6,7,9,10,16 & 17*****
str=input("enter a string: ")
f = open('myfile.txt','w')
f.write(str)
f.close()
f = open('myfile.txt','r')   #**ques 6 read text file***
text=f.read()
print(text)
print(len(text))   #**ques. 7 str length***
print(str.find('hello'))  #****ques.9*****
print(str.upper())  #***ques. 10***
print(str.title()) #**ques.17***
print(str.count('a')) #**ques.16**

#****ques.11*****
def fibonacci(n):
    if(n==1 or n==2):
        return 1
    else:
        fibo=fibonacci(n-1)+fibonacci(n-2)
        return fibo
    
count = 1
while count <= number:
 print(fibonacci(count), end=" ")
 count+=1
	
#****ques.12*****
def sum_of_digits(n):
   sum=0
   rem=0
   if(n==0 or n<0):
      return 0
   while(n!=0):
      rem=n%10
      sum=sum+rem
      n=int(n/10)
   return sum   
sum=sum_of_digits(432)
print(f'sum of the digits:{sum}')
      
#***ques. 13***
birth_year=int(input("enter your birth year: "))
age=2024-birth_year
print(age)

#***ques.14***
lines = []

while True:
    user_input = input()
    if user_input == '':
      break
    else:
      lines.append(user_input)
print(lines)

#***ques.15***
import csv
with open('myfile.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

#**ques.18***
ana1,ana2=input("enter first string: ").split()
count=0
if(len(ana1)==len(ana2)):
  for i in ana1:
   for j in ana2:
      if(i==j):
        count+=1
      else:
        continue 
if(len(ana1)==count): print("anagram")       
else:
  print("not an anagram")

#***ques.19***
import string
str3="Hello world, Akriti this side...!!"
str3=str3.translate(str.maketrans('', '', string.punctuation))
print(str3)

#**ques.20,21 & 22***
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
i=0
sum=0
for i in range(len(x)):
   sum=sum+x[i]
print(f'sum of numbers in list:{sum}') 
print(x.count(7)) #**ques.21**
print(max(x)) #***ques.22**
print(min(x))

#**ques.23***
value,convert_to=input("enter the value and convert to(c-celcuius, f-fahrenheit): ").split()
value=int(value)
match (convert_to):
 case 'c':
   print((value-32)/1.8)
 case 'f':
   print((value * 1.8) + 32)

#***ques.24***
x,y,z=input("enter numbers and (a-add,s-subtract,m-multiply,d-division): ").split()
x,y=int(x),int(y)
match (z):
 case 'a':
   print(x+y)
 case 's':
   print(x-y)
 case 'm':
   print(x*y)
 case 'd':
   print(x / y)

#**ques.25**
import shutil 
shutil.copyfile('myfile.txt','secfile.txt')

#***ques.26***
str2="hello akriti...!!!"
print(str2.endswith("!!!"))
print(str2.startswith("hell"))

#****ques.27*****
str1="Python ML internship"
print(list(str1))