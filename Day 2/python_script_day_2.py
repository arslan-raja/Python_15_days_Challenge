# %% [markdown]
# <h1>Day # 02</h1>
# 
# <h3>Aim:</h3>
# <ul>
#     <li>Understand variables and different daya types in Python.</li>
# </ul>

# %%
#function to get dtype int from user...

def get_input(data_type, input_label, error_label):
    while True:
        try:
            return data_type(input(input_label))
        except ValueError:
            print(error_label)

# %% [markdown]
# <h2>Example Questions</h2>

# %% [markdown]
# <h3>Q1. Create variables for storing a person's name, age and average test score.</h3>

# %%
name = input("Enter your name: ")
age = get_input(int, "Enter your age: ", "Enter a valid age...")

math = get_input(int, "Enter your Math numbers: ", "Enter a valid score...")
english = get_input(int, "Enter your English numbers: ", "Enter a valid score...")
science = get_input(int, "Enter your science numbers: ", "Enter a valid score...")

avg = (math + english + science)/3
print(f"Hello {name}, your average score is {avg} and your age is {age}.")

# %% [markdown]
# <h3>Q2. Concatenate two strings and print the result.</h3>

# %%
a = input("Enter first string: ")
b = input("Enter second string: ")

concatenate = a + b
print("Concatenated string: ", concatenate)

# %% [markdown]
# <h3>Q3. Create a list of fruits and access elements using indexing.</h3>

# %%
fruits = ["Apple", "Orange", "Banana", "Grapes"]

print("First index: ", fruits[0])
print("Third index: ", fruits[2])
print("Last index: ", fruits[-1])

# %% [markdown]
# <h2>Practice Questions...</h2>

# %% [markdown]
# <h3>Q1. Given a list of numbers, find the sum and average.</h3>

# %%
listt = []
sum = 0

while True:
    number = get_input(int, "Enter a number: ", "Enter a valid number...")
    if number == -1:
        break
    
    listt.append(number)

for i in listt:
    sum += i

avg = sum/len(listt)

print("Given list: ", listt)
print("Sum of the given list: ", sum)
print("Average of the given list: ", avg)

# %% [markdown]
# <h3>Q2. Create a program that takes a temperature in Celsius and converts it to Kelvin.</h3>

# %%
c = get_input(int, "Enter the temperature in Celsius: ", "Enter a valid temperature")

k = c + 273.15
print(f"{c}°C is equal {k} K.")

# %% [markdown]
# <h3>Q3. Implement a program that checks if a given string is a palindrome .</h3>

# %%
user = input("Enter a string: ").lower()
reversed = user[::-1]

print("String is Palindrome") if user == reversed else print("String is not Palindrome")

# %% [markdown]
# <h3>Q4. Create a function to reverse a string.</h3>

# %%
def reverse_string(str):
    return str[::-1]

a = input("Enter a string: ")
reversed_str = reverse_string(a)
print("Original input: ", a)
print("Reversed input: ", reversed_str)


# %% [markdown]
# <h3>Q5. Giver a list of names, concatenate them into a single string separated by spaces.</h3>

# %%
name_list = ["Arslan", "Saad", "Umar", "Hamza", "Fahad", "Husnain"]
name_string = ""
for i in name_list:
    name_string += i + " "

print("Name list: ", name_list)
print("Name string: ", name_string)

# %% [markdown]
# <h3>Q6. Write a python program to check if a given string is a pangram.</h3>
# <p>(contains all letters of the alphabet)</p>

# %%
alphabet = ['a','b','c','d','e','f', 'g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','v','w','x','y','z']

pangram_input = input("Enter a string to check pangram: ").lower()

for char in pangram_input:
    if char in alphabet:
        alphabet.remove(char)

print("Input String: ", pangram_input)

if len(alphabet) == 0:
    print("Input string is pangram")

else:
    print("Input string is not pangram")

# %% [markdown]
# <h3>Q7. Calculate the area and circumference of a circle given its radius.</h3>

# %%
import math         # to use PI

radius = get_input(float, "Enter the radius of the circle(cm): ", "Enter a valid radius...")

area = math.pi * radius**2
circumference = 2 * math.pi * radius

print(f"Radius of the circle            : {radius} cm")
print(f"Area of that circle             : {area} cm^2")
print(f"Circumference of that circle    : {circumference} cm")

# %% [markdown]
# <h3>Q8. Implement a program that converts a given number of minutes into hours and minutes.</h3>

# %%
time = get_input(int, "Enter time in minutes: ", "Enter a valid number...")
hours = time // 60
minutes = time - (hours * 60)

print(f"Time in minutes     : {time} minutes")
print(f"Time in hours       : {hours}h", end=' ')

if minutes != 0:
    print(f"and {minutes}m")

# %% [markdown]
# <h3>Q9. Create a function to count the number of vowels in a given string.</h3>

# %%
def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in str.lower():
        if char in vowels:
            count += 1

    return count


q9_input = input("Enter a string to count vowels: ")
vowels_count = count_vowels(q9_input)

print(f"Input String: {q9_input}")
print(f"No of vowels: {vowels_count}")

# %% [markdown]
# <h3>Q10. Write a program to check if a number if prime.</h3>

# %%
q10_input = get_input(int, "Enter a number: ", "Enter a valid number...")
prime = True

for i in range(2, q10_input):
    if q10_input % i == 0:
        prime = False
        break

if prime:
    print(f"{q10_input} is a prime number")

else:
    print(f"{q10_input} is not a prime number")

# %% [markdown]
# ------------------------------------------------------------------------------------------------------------------
# 


