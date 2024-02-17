# 1) Write  a program to display elements from a given list present at odd index positions
# Given	 list: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("1.............................")

my_list = [10,20,30,40,50,60,70,80,90,100]
for i in range(1,10,2):
    print(my_list[i])


# 2)Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become
# 2 + 22 + 222 + 2222 + 22222 = 24690
print("2.............................")

n = 5
sum = 0
for i in range(1,n+1):
    num = eval('2'*i)
    sum+=num
print(sum)



# 3)	Write a function program that returns
# a.	String
# b.	Accepts different values as parameters and returns a list
# c.	returns a dictionary
# d.	returns a tuple
print("3.............................")

# a. Returning a string:

def return_string():
    return "Hello, I am a string!"

print(return_string())


# b. Accepting different values as parameters and returning a list:

def return_list(*args):
    return list(args)

print(return_list(1, 2, 3, 4, 5))


# c. Returning a dictionary:

def return_dictionary():
    return {"name": "John", "age": 25}

print(return_dictionary())


# d. Returning a tuple:
def return_tuple():
    return (1, 2, 3, 4, 5)
print(return_tuple())

# 4.Create a simple horoscope program that asks the user for their star sign and outputs a fun horoscope
# for them. Bear in mind that your program should display an error message if the user types in their sign
# wrong.
print("4.............................")

horoscopes = {
    "aries": "Today, you will have a burst of energy and accomplish great things!",
    "taurus": "You might encounter some unexpected challenges today, but stay strong!",
    "gemini": "Your communication skills will be on point today. Have some fun conversations!",
    # Add more horoscopes for other star signs
}

user_sign = input("What is your star sign? ").lower()

if user_sign in horoscopes:
    print(horoscopes[user_sign])
else:
    print("Oops! That's not a valid star sign. Please try again.")





# 5Write a program to check how many times the character is occurring in the sequence.
print("5.............................")

count = 0
string = "be-practiclee"
char = "e"
for i in string:
    if i == char :
        count += 1
print(count)


# 6) Write a program to check Palindrome numbers in a given list
print("6.............................")

list1 = [1,2,1]
rev = list(reversed(list1))
if list1 == rev :
    print(f"{list1} is palindrom")
else:
    print(f"{list1} is not palindrom")

# 7.	Write a program to print Arithmetic Progression Series
print("7.............................")

def arthmetic(a,d,n):
    current_term = a
    for i in range (1,n+1):
        print(current_term,end=' ')
        current_term = current_term + d
a = 0
d = 5
n = 10
arthmetic(a,d,n)

# 8.Write a Python program to print butterfly pattern
print("8.............................")

r = 5
for i in range(1,r+1):
    print("*"*i,end="")
    print(" "*(r-i)*2,end="")
    print("*"*i)
for i in range(r,0,-1):
    print("*" * i, end="")
    print(" " * (r - i) * 2, end="")
    print("*" * i)

# 10.	Write a program to remove the last character from the given string using loop
print("10.............................")

str = "Be-Practical"
str1 = str[ : -1]
print(str1)
