## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
<b style='color:green; display:block'>ANS</b>
```
Python is used in multiple domains like for web developemnt, operating system, Hardware devices etc.And python is very easy to understand So it is known as general purpose and high-level programming language.
```

Q2. Why is Python called a dynamically typed language?
<b style='color:green; display:block'> Ans : </b>
```
Python don't have any problem even if we don't declare the type of variable. It states the kind of variable in the runtime of the program. Python also take cares of the memory management which is crucial in programming. So, Python is a dynamically typed language
```
Q3. List some pros and cons of Python programming language?
<b style='color:green; display:block'> Ans : </b>
```
Pros:
Beginner-friendly
Flexible and Extensible
Highly Scalable
Portable
Embeddable
Extensive Libraries

Cons:
Issues with design
Slower than compiled languages
High memory consumption
Complex multithreading
```
Q4. In what all domains can we use Python?
<b style='color:green; display:block'> Ans : </b>
```
Python don't have any problem even if we don't declare the type of variable. It states the kind of variable in the runtime of the program. Python also take cares of the memory management which is crucial in programming. So, Python is a dynamically typed language
```
Q5. What are variable and how can we declare them?
<b style='color:green; display:block'> Ans : </b>
```
Variable is the name provided to a memory container which stores data.
```
Q6. How can we take an input from the user in Python?
<b style='color:green; display:block'> Ans : </b>
```
Python has an inbuild function named 'input' which is used to take input in string format as default.
eg:
x = input("enter a number") 
```
Q7. What is the default datatype of the value that has been taken as an input using input() function?
<b style='color:green; display:block'> Ans : </b>
```
String is the default datatype of the value that has been taken as an input using input() function.
```
Q8. What is type casting?
<b style='color:green; display:block'> Ans : </b>
```
Type casting is a process of converting one datatype of variable to another datatype.
```
eg:
```python
int_n = 2
string_n = str(2)
```
Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
<b style='color:green; display:block'> Ans : </b>
```
Yes, we can take more than one input from the user using single input() function. Because input function by default takes in string format. which means we can take input giving space between each word and we will use split function on the input string to get many input.
```
eg:
```python
string_in = input() // "1 2 3 4 5"
int_arr = string_in.split()
```

Q10. What are keywords?
<b style='color:green; display:block'> Ans : </b>
```
Keywords are some predefined and reserved words in python that have special meanings. Keywords are used to define the syntax of the coding. The keyword cannot be used as an identifier, function, and variable name.
```
Q11. Can we use keywords as a variable? Support your answer with reason.
<b style='color:green; display:block'> Ans : </b>
```
No, we can not use keyword as a variable. Because keywords are reserved word and has some specific meaning which can not be overridden by other meaning.
```
Q12. What is indentation? What's the use of indentaion in Python?
<b style='color:green; display:block'> Ans : </b>
```
Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.
```
Q13. How can we throw some output in Python?
 <b style='color:green; display:block'> Ans : </b>
```
There is a "print()" function in python that is used to give output.
```
Q14. What are operators in Python?
<b style='color:green; display:block'> Ans : </b>
```
In python, operators are special symbols that designate that some sort of computation should be performed.
```
Q15. What is difference between / and // operators?
<b style='color:green; display:block'> Ans : </b>
```python
'/' is the division operator. '//' is the floor division operator.
eg:
x = 4 / 3 ## 1.33333333
y = 4 // 3 ## 1
```
Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
<b style='color:green; display:block'> Ans : </b>
```python
print("iNeuroniNeuroniNeuroniNeuron")
```
Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
<b style='color:green; display:block'> Ans : </b>
```python
int_n = int(input("Enter a number"))
if int_n % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")
```
Q18. What are boolean operator?
<b style='color:green; display:block'> Ans : </b>
```
'and' , 'or', 'not' are boolean operator in python.
```
Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
<b style='color:green; display:block'> Ans : </b>
```
1. "1"
2. "0"
3. False
4. "1"
```
Q20. What are conditional statements in Python?
<b style='color:green; display:block'> Ans : </b>
```
There are three conditional statement in python.
i.e if, else and elif.
```
Q21. What is use of 'if', 'elif' and 'else' keywords?
<b style='color:green; display:block'> Ans : </b>
```
- if statement is used with a condition. Execution enters to "if" block when condition is true.

- When condition is false, Execution happens in "else" block.

- When above condition is false, we use another condition using "elif". By which we create nested if-else. 
```
Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
<b style='color:green; display:block'> Ans : </b>
```python
int_age = int(input("Enter your age !"))
if int_age >= 18 :
    print("I can vote.")
else:
    print("I can not vote.")
```
Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
<b style='color:green; display:block'> Ans : </b>
```python
numbers = [12, 75, 150, 180, 145, 525, 50]
add = 0
for num in numbers:
    if num%2 == 0:
        add += num
print("Sum of all the even numbers is : ",add)
```

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
<b style='color:green; display:block'> Ans : </b>
```python
print("Enter 3 numbers !")
int_a = int(input())
int_b = int(input())
int_c = int(input())

if int_a > int_b and int_a > int_c:
    print(int_a, " is the greatest number.")
elif int_b > int_c:
    print(int_b, " is the greatest number.")
else:
    print(int_c, " is the greatest number.")
```

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
<b style='color:green; display:block'> Ans : </b>
```python
numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n%5 == 0 and n <= 150 :
        print(n , end=" ")
    if n > 500:
        break 
```

Q26. What is a string? How can we declare string in Python?
<b style='color:green; display:block'> Ans : </b>

```
A string is any series of characters that are interpreted literally by a script. For Example: "iNeuron".
We can create a string in python by enclosing characters inside a single quote or double-quotes.
```

Q27. How can we access the string using its index?
<b style='color:green; display:block'> Ans : </b>

```
we can access string by referring to its index number inside square brackets [].
For Example : str = "hello" print(str[0]) # h
```

Q28. Write a code to get the desired output of the following

```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

<b style='color:green; display:block'> Ans : </b>
```
python
string = "Big Data iNeuron"
words = string.split(' ')
print(words[2])
```

Q29. Write a code to get the desired output of the following

```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

<b style='color:green; display:block'> Ans : </b>
```
python
def reverse(s) :
    n = len(s) - 1
    str = ""
    for i in range(n, -1, -1):
        str += s[i]
    return str

string = "Big Data iNeuron"
words = string.split(' ')
print(reverse(words[2]))
```

Q30. Resverse the string given in the above question.
<b style='color:green; display:block'> Ans : </b>
```
python
def reverse(s) :
    n = len(s) - 1
    str = ""
    for i in range(n, -1, -1):
        str += s[i]
    return str

string = "Big Data iNeuron"
print(reverse(string))
```

Q31. How can you delete entire string at once?
<b style='color:green; display:block'> Ans : </b>

```
string = "swayam"
del string
```

Q32. What is escape sequence?
<b style='color:green; display:block'> Ans : </b>

```python
An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.

For Example :
print('Who\'s this?') #Who's this?
```

Q33. How can you print the below string?


'iNeuron's Big Data Course'


<b style='color:green; display:block'> Ans : </b>

```python
print('iNeuron\'s Big Data Course')
```

Q34. What is a list in Python?
<b style='color:green; display:block'> Ans : </b>
```
python
Lists are used to store multiple items in a single variable.

For Example :
list = ['ball', 10, 'banana', 'bat', 2.44]

print(list)
```

Q35. How can you create a list in Python?
<b style='color:green; display:block'> Ans : </b>

```
In python we can create a list is created by placing elements inside square brackets [] , separated by commas.
```

Q36. How can we access the elements in a list?
<b style='color:green; display:block'> Ans : </b>

```python
We can access the list items by referring to the index number.

For example :
lst = [1,2,3]
print(lst[2]) # 3
```

Q37. Write a code to access the word "iNeuron" from the given list.

```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
```

<b style='color:green; display:block'> Ans : </b>
```python
print(lst[4][2])
```

Q38. Take a list as an input from the user and find the length of the list.

<b style='color:green; display:block'> Ans : </b>

```python
a = input("Enter list of input separated by space")
lis = a.split(' ')
print(len(lis))
```

Q39. Add the word "Big" in the 3rd index of the given list.

```python
lst = ["Welcome", "to", "Data", "course"]
```

<b style='color:green; display:block'> Ans : </b>

```python
lst = ["Welcome", "to", "Data", "course"]
lst.insert(2, "Big")
print(lst)
```

Q40. What is a tuple? How is it different from list?
<b style='color:green; display:block'> Ans : </b>

```
Python Tuple is a collection of objects separated by commas.
Tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, but list is mutable.
```

Q41. How can you create a tuple in Python?
<b style='color:green; display:block'> Ans : </b>

```python
We can create tuple by enclosing all the comma-separated elements inside the parenthesis ().

For Example :
tup = ( 'typle', True, 3.9, 56, [4, 2, 3] )
print( tup )
```

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
<b style='color:green; display:block'> Ans : </b>

```
We can't add/insert or append anything in tuple, because tuple are immutable.

```
Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
<b style='color:green; display:block'> Ans : </b>

```python
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3) # (1,2,3,4,5,6)
```

Q44. Take a tuple as an input and print the count of elements in it.
<b style='color:green; display:block'> Ans : </b>

```
inp = input("enter a tuple")
tpl = tuple(inp)
print(len(tpl))
```

Q45. What are sets in Python?
<b style='color:green; display:block'> Ans : </b>

```
Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.

```
Q46. How can you create a set?
<b style='color:green; display:block'> Ans : </b>
```
python
st = set()
```

Q47. Create a set and add "iNeuron" in your set.
<b style='color:green; display:block'> Ans : </b>

```python
st = set()
st.add('iNeuron')
```

Q48. Try to add multiple values using add() function.
<b style='color:green; display:block'> Ans : </b>
```

add() function on takes one argument. It will throw an error.
```

Q49. How is update() different from add()?
<b style='color:green; display:block'> Ans : </b>

```
add() function is used add only single element.
update() function is used add several element in the set.
```
Q50. What is clear() in sets?
<b style='color:green; display:block'> Ans : </b>
```
clear() method removes all elements in a set.
```

Q51. What is frozen set?
<b style='color:green; display:block'> Ans : </b>

```
Frozen set is a set which is immutable.
```

Q52. How is frozen set different from set?
<b style='color:green; display:block'> Ans : </b>

```
Frozen set are immutable but set are muttable.
```

Q53. What is union() in sets? Explain via code.
<b style='color:green; display:block'> Ans : </b>

```python
union() method returns a set that contains all the elements of both the set.

For Example :
a = {2, 3, 4, 5}

b = {1, 3, 5, 6}

print(a | b)
# {1, 2, 3, 4, 5, 6}
```

Q54. What is intersection() in sets? Explain via code.
<b style='color:green; display:block'> Ans : </b>

```python
intersection() method returns a set that contains common elements of both the set.

For Example :
a = {2, 3, 4, 5}

b = {1, 3, 5, 6}

print(a & b)
# {3, 5}
```

Q55. What is dictionary in Python?
<b style='color:green; display:block'> Ans : </b>

```
Dictionary in Python is a collection of keys values, used to store data values like a map. A dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
```

Q56. How is dictionary different from all other data structures.
<b style='color:green; display:block'> Ans : </b>

```
Dictionary is one of the important Data Structures that is usually used to store data in the key-value format. A dictionary has a set of keys and each key has a single associated value.
```

Q57. How can we delare a dictionary in Python?
<b style='color:green; display:block'> Ans : </b>

```python
dct = {}
```
Q58. What will the output of the following?

```python
var = {}
print(type(var))
```

<b style='color:green; display:block'> Ans : </b>

```python
<class 'dict'>
```

Q59. How can we add an element in a dictionary?
<b style='color:green; display:block'> Ans : </b>

```python
dct = {}
dct[1] = 2
print(dct) # {1: 2}
```


Q60. Create a dictionary and access all the values in that dictionary.

<b style="color:green;">Ans</b>
```python
dic = {
    "name" : "swayam",
    "age" : 21
}
values_list = dic.values()
print(values_list)
```

Q61. Create a nested dictionary and access all the element in the inner dictionary.
<b style="color:green;">Ans</b>
```python
dic = {
    "name" : "Swayam",
    "favourite" : {
        "car" : "audi",
        "web-series" : "Dark"
    }
}

print("Favourite car is" , dic["favourite"]["car"] )
```
Q62. What is the use of get() function?

<b style="color:green;">Ans</b>
```
- "get()" function is used in dictionary to get the values of a key exist in it.
- if there is no such key exist in dictionary, it will return "None" instead of error.
```
Q63. What is the use of items() function?

<b style="color:green;">Ans</b>
```
"items()" function is used in dictionary which return all the items exist in it in the form of list.
```
Q64. What is the use of pop() function?

<b style="color:green;">Ans</b>
```
"pop()" function is used in list to remove the last element.
```
Q65. What is the use of popitems() function?

<b style="color:green;">Ans</b>
```
"popitems()" is used in dictionary to delete the last item inserted in it.
```
Q66. What is the use of keys() function?

<b style="color:green;">Ans</b>
```
"keys()" function is used in dictionary to return all the keys exist in the dictionary in the form of list.
```
Q67. What is the use of values() function?

<b style="color:green;">Ans</b>
```
"values()" function is used in a dictionary to return all the values exist in the dictionary in the form of list.
```
```python
dic={
    "name" : "swwayam"
}
print(dic.values())
```
Q68. What are loops in Python?

<b style="color:green;">Ans</b>
```
It allows programmers to modify the flow of the program so that rather than writing the same code, again and again.
- It is also used to iterate a sequence.
```
Q69. How many type of loop are there in Python?

<b style="color:green;">Ans</b>
```
There are 2 types of loop in python, 
- for loop
- while loop
```
Q70. What is the difference between for and while loops?

<b style="color:green;">Ans</b>
```
- In "for" loop we give any certain range or list in ordered to traverse it.
- where  in "while" loop we loop until our condition is satisfied. 
```
Q71. What is the use of continue statement?

<b style="color:green;">Ans</b>
```
while looping when we want to go to next iteration without executing below statement, we use continue.
```
```python
for i in range(1,10):
    if i == 5:
        continue
```
Q72. What is the use of break statement?

<b style="color:green;">Ans</b>
```
when we want to stop the loop or get out of the loop, we use break statement.
```
```python
for i in range(1,10):
    if i == 5:
        break
```
Q73. What is the use of pass statement?

<b style="color:green;">Ans</b>
```
When we don't have any statement to execute in a block we use "pass".
```
```python
check = True
if check:
    pass
else:
    print("hii")
```
Q74. What is the use of range() function?

<b style="color:green;">Ans</b>
```
range() is used in "for" loop to define the number of iteration or two specific number whithin which it will loop with a certain time period.
```
```python
for i in range(1,5,1):
    print(i)

#it will run for 4 times from 1 to 5(exclusive 5) with step 1.
```
Q75. How can you loop over a dictionary?

<b style="color:green;">Ans</b>
```
There is an attribute of dictionary known as "items()" which give you a list of all the items. Using that list you can loop on it.
```
```python
for item in dic.items():
    print(item)
```

### Coding problems
Q76. Write a Python program to find the factorial of a given number.

<b style="color:green;">Ans</b>
```python
n = int(input("Enter a number \n"))
fac = 1
for i in range(1,n+1):
    fac *= i

print(f"Factorial of {n} is {fac}")

```
Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

<b style="color:green;">Ans</b>
```python
inputs = input("enter P R T").split(" ")
P = int(inputs[0])
R = int(inputs[1])
T = int(inputs[2])

SI = (P*R*T)/100
print(f"Simple Interest is {SI}")
```
Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

<b style="color:green;">Ans</b>
```
inputs = input("enter p , r ,t").split(" ")
p = int(inputs[0])
r = int(inputs[1])
t = int(inputs[2])
A = p*(pow(1 + (r/100),t))
print("A is ",A)
```
Q79. Write a Python program to check if a number is prime or not.

<b style="color:green;">Ans</b>
```python
n = int(input("Enter a Number"))
check = False
for i in range(2,n//2+1,1):
     
     if n%i == 0:
         check = True
         break

if check :
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
    
```
Q80. Write a Python program to check Armstrong Number.

<b style="color:green;">Ans</b>
```python
n = input("Enter a Number\n")
#let 123 = 1pow(3)+2(pow3)+3pow(3)
leng = len(n)
n = int(n)
sum = 0;
num = n;
while(n>0):
    rem = n%10
    sum += pow(rem,leng)
    n //= 10;
print(sum)

if(num == sum):
    print(num,' is Armstrong')
else:
    print(num,' is not a Armstrong')
```
Q81. Write a Python program to find the n-th Fibonacci Number.

<b style="color:green;">Ans</b>
```python
first = 0
second = 1
n = 7  #nth number
print(first,second,end=" ")
i = 2
while i<n:
    res = first + second
    print(res, end=" ")
    first = second
    second = res 
    i += 1
```

Q82. Write a Python program to interchange the first and last element in a list.

<b style="color:green;">Ans</b>
```python
lis = [1,2,3,4,5]
first_element = lis[0]
lis[0] = lis[len(lis)-1]
lis[len(lis)-1] = first_element
print(lis)
```
Q83. Write a Python program to swap two elements in a list.

<b style="color:green;">Ans</b>
```python
lis = [1,2,3,4,5]

##swaped indexes
i , j =1,4     

temp = lis[i]
lis[i] = lis[j]
lis[j] = temp

print(lis)
```
Q84. Write a Python program to find N largest element from a list.

<b style="color:green;">Ans</b>
```python
lis = [2,5,1,6,12,7,3]
N = 3

lis.sort()
print(N,"largest element from a list is : ", lis[len(lis)-N])
```
Q85. Write a Python program to find cumulative sum of a list.

<b style="color:green;">Ans</b>
```python
lis = [10,20,30,40,50]
sum = 0
new_list = []
for n in lis:
    sum += n
    new_list.append(sum)

print(new_list)
```

Q86. Write a Python program to check if a string is palindrome or not.

<b style="color:green;">Ans</b>
```python
string = "ababa"
rev_string = ""
for i in range(len(string)-1,-1,-1):
    rev_string += string[i]
    
if string == rev_string:
    print("string is palindrome.")
else:
    print("string is not palindrome")
```
Q87. Write a Python program to remove i'th element from a string.

<b style="color:green;">Ans</b>
```python
string = "emberassment"
i = 3 ## 'e'
s = string[0:3] + string[4:]
print(s)
```
Q88. Write a Python program to check if a substring is present in a given string.

<b style="color:green;">Ans</b>
```python
string = "hey there, i am swayam prakash sahoo."
sub_string = "swayam"
lis = string.split()

if sub_string in lis:
    print("substring is present in string")
else:
    print("substring is not present in string")
```
Q89. Write a Python program to find words which are greater than given length k.

<b style="color:green;">Ans</b>
```python
words = ["swayam" , "bimal", "rock" , "audi", "speaker" , "cat" , "aeroplane"]
k = 5

for word in words :
    if len(word) > 5:
        print(word, end=" ")
```

Q90. Write a Python program to extract unquire dictionary values.

<b style="color:green;">Ans</b>
```python
d = {
    "name" : "swayam",
    "age" : 21,
    "nick_name" : "swayam",
    "language" : "python"
}
s = set(d.values())
print(s)
```

Q91. Write a Python program to merge two dictionary.

<b style="color:green;">Ans</b>
```python
d1 = {
    "name" : "swayam",
    "age" : 21
}

d2 = {
    "language" : "python",
    "leetcode" : 450
}

d1.update(d2)
print(d1)
```
Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```
<b style="color:green;">Ans</b>
```
lis = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dic = {}
for t in lis:
    dic[t[0]] = t[1]

print(dic)
```

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```
<b style="color:green;">Ans</b>
```python
lis = [9, 5, 6]
ans = [(x,pow(x,3)) for x in lis]
print(ans)
```

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```
<b style="color:green;">Ans</b>
```python
tp1 = (7,2)
tp2 = (7,8)

lis = [(x,y) for x in tp1 for y in tp2]
lis2 = [(x,y) for x in tp2 for y in tp1]
lis.extend(lis2)
print(lis)
```

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```
<b style="color:green;">Ans</b>
```python
def myfun(tp):
    return tp[1]

l = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
l.sort(key = myfun)
print(l)
```
Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
<b style="color:green;">Ans</b>
```python
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```
<b style="color:green;">Ans</b>
```python
for i in range(4,-1,-1):
    for j in range(5):
        if j >= i:
            print("* ",end="")
        else:
            print(" ",end="")
    print()
```

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```
<b style="color:green;">Ans</b>
```python
for i in range(4,-1,-1):
    for j in range(5):
        if j >= i:
            print("* ",end="")
        else:
            print(" ",end="")
    print()
```
Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```
<b style="color:green;">Ans</b>
```python
for i in range(1,6):
    for j in range(1,i+1):
        print(j , end=" ")
    print()
```
Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```
<b style="color:green;">Ans</b>
```python
ch = 'A'
for i in range(5):
    for j in range(i+1):
        print(ch,end=" ")
    ch  = chr(ord(ch)+1)
    print()
```
