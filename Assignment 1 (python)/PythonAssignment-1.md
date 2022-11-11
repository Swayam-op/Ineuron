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