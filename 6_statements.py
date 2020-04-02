#indentation important Python Statement
#1
hungry=True
if hungry:
	print('I am hungry')
	snack=True
	orderOnline=True
	if snack:
		print('have snack')
	elif orderOnline:
		print('online ordered')
	else:
		print('No food need to wait')
else:
	print('I am not hungry')
#2for loop
mylist=[1,'two',3.0]
for items_iterator in mylist:
	print(items_iterator)

mynumlist=[1,2,3,4,5,6,7,8,9]
list_sum=0
for nums in mynumlist:
	list_sum=list_sum+nums
print(list_sum)

size=0
for _ in mynumlist:
	size++
print(size)

mytuplelist=[(1,2),(3,4),(5,6),(7,8),(9,0)]
#tuple unpacking
for a,b in mytuplelist:
	print('a=',a)
	print('b=',b)

mydict={'k1':1,'k2':,2'k3':3}
for keys in mydict:
	print(keys)

for values in mydict.values():
	print(values)

for keyvaluepairs in mydict.items():
	print(keyvaluepairs)

#unpacking
for key,value in mydict.items():
	print(key,'->',value)


#3while loop
x=0
#x=10
while x<5:
	print(x,' is less than 5')
	x++
else:
	print(x,' is not less than 5')

#break,continue,pass vs comment
x=[1,2,3,]
for i in x:
	pass
print('end of script')

actor='Akshay'
for letter in actor:
	if letter=='a':
		continue
	print(letter)

for letter in actor:
	if letter=='a':
		break
	print(letter)

#range function
start=0
end=10
increment=2

mylist=[1,2,3,4,5]
for num in range(start,end,increment):
	print(num)
mylist=list(range(start,end,increment))

#enumerate
indexcnt=0
word='abcde'
for letter in word:
	print('at index {} the letter is {} that is same without iterator {}'.format(indexcnt,letter,word[indexcnt]))
	indexcnt++
#or
for letter in enumerate(word):
	print(letter)

for index,letter in enumerate(word):
	print(index,' : ',letter)

#zip function maps tuple item for same index list
mylist_chocolate=['cadbury','kitkat','5star']
mylist_quote=['aaj Kuch Meetha hojaye','kitkat break banta hai','khao khojao']
mylist_price=[100,50,25]
for item in zip(mylist_chocolate,mylist_quote,mylist_price):
	print(item)

#in operator
if('5star' in mylist_chocolate):
	print('Yes')
if('5' in '5star'):
	print('Yes')
mydict={'mykey':'myvalue'}
if('mykey' in mydict ):
	print('yes')
if('myvalue' in mydict.keys() ):
	print('yes')
else:
	print('No')

#min() max()
mynumslist=[10,20,30,40,50,60,0,99]
print(min(mynumslist))
print(max(mynumslist))

#random library
from random import shuffle
mynumslist=[10,20,30,40,50,60,0,99]
shuffle(mynumslist)
print(mynumslist)

from random import radint
start=0
end=100
print(radint(start,end))

#user input(): accept all as string
#type cast int() float() etc...
name=input('enter your name')
print('welcome ',name)

#list comprehensions :advantage{one line code even if same complexity},disadvantage{readability lost}
mystring='hello'
mylist=[]
for letter in mystring:
	mylist.append(letter)
#alternative comprehension
mylist=[ iterator for iterator in mystring ]
mysqlist=[ x**2 for x in range(1,10) if x%2==0 ]
mysq_cube_list=[x**2 if x%2==0 else x**3 for x in range(1,10) ]

celcius=[0,10,,20,34.5]
fahrenheit=[ ( (9/5)*temp+32) for temp in celcius ]

#nested loop in list comprehension

#without comprehe
mylist=[]
for x in [2,3,4]:
	for y in [9,8,7]:
		mylist.append(x*y)
#with compreh
mylist2=[ x*y for x in [2,3,4] for y in [9,8,7] ]

#split() fun
mystring='bulave Tujhe yaar aaj meri gailyan basau tere sang mein alag duniya'
for word in mystring.split():
	if word[0].lower()=='t':
		print(word)

	if len(word)%2==0:
		print(word)

#
"""
>>> for num in range(1,101):
...     if ((num%3==0) or (num%5==0)): 
...             print(num,':')
...             if(num%3==0):
...                     print('Fizz')
...             if(num%5==0):
...                     print('Buzz')
"""
for num in range(1,101):
	if num%3==0 and num%5==0 :
		print('FizzBuzz')
	elif num%3==0:
		print('Fizz')
	elif num%5==0:
		print('Buzz')
	else:
		print(num)
#

listed=[word[0] for word in in mystring.split()]
#


