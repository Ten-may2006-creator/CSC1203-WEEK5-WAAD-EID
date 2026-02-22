##Q1##   
import math

radius = float(input("Enter the radius of the circle: "))

def calculate_area(r):
    return math.pi * r ** 2

calculate_circumference = lambda r: 2 * math.pi * r

area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"Area: {round(area, 2):.2f}")
print(f"Circumference: {round(circumference, 2):.2f}")
###########################################
## Q2 ##
import re

text = input("Enter a string: ")

numbers = re.findall(r'\d+', text)
numbers = list(map(int, numbers))

def sum_numbers(nums):
    return sum(nums)

double_value = lambda x: x * 2

total = sum_numbers(numbers)
doubled = double_value(total)

print("Numbers found:", numbers)
print("Sum:", total)
print("Doubled value:", doubled)
#######################################
## Q3 ##
import math

user_input = input("Enter numbers separated by commas: ")
numbers = list(map(float, user_input.split(',')))

square = lambda x: x ** 2

squares = list(map(square, numbers))

def max_square(nums):
    return max(nums)

maximum_square = max_square(squares)
sum_of_squares = sum(squares)
sqrt_of_sum = math.sqrt(sum_of_squares)

print("Original numbers:", numbers)
print("Squares:", squares)
print("Maximum square:", maximum_square)
print("Square root of sum of squares:", sqrt_of_sum)
##################################################
##Q4##
import re
import math

# Read password
password = input("Enter a password: ")

# Regex checks
has_upper = re.search(r'[A-Z]', password)
has_lower = re.search(r'[a-z]', password)
has_number = re.search(r'\d', password)

if has_upper and has_lower and has_number:
    strength = "Strong"
else:
    strength = "Weak"

# Read scores
scores_input = input("Enter 5 scores separated by spaces: ")
scores = list(map(float, scores_input.split()))

# Function to calculate average
def calculate_average(scores):
    return sum(scores) / len(scores)

# Lambda to calculate average
average_lambda = lambda s: sum(s) / len(s)

average = average_lambda(scores)
rounded_average = math.ceil(average)

print("Password strength:", strength)
print("Rounded average score:", rounded_average)
#############################################
##Q5##
import re
import math

# Function to count total vowels
def count_vowels(text):
    return len(re.findall(r'[aeiouAEIOU]', text))

# Read paragraph
paragraph = input("Enter a paragraph: ")

# Find words starting with vowel
vowel_words = re.findall(r'\b[aeiouAEIOU]\w*', paragraph)

# Lambda to calculate length of each vowel word
word_length = lambda word: len(word)

lengths = list(map(word_length, vowel_words))

# Calculate average vowel word length
if lengths:
    average_length = round(sum(lengths) / len(lengths), 2)
else:
    average_length = 0

total_vowels = count_vowels(paragraph)

print("Words starting with vowels:", vowel_words)
print("Total vowels in paragraph:", total_vowels)
print("Average vowel-word length:", average_length)
####################### 