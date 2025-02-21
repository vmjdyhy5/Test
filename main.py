import re
import random

def find_pattern_occurrences(text):
    # Define the regex pattern
    # ^b: starts with 'b'
    # [a-zA-Z]*: matches any number of letters (both lowercase and uppercase)
    # Bob$: ends with 'Bob'
    pattern = r'\bb[a-zA-Z]*Bob\b'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Return the number of matches
    return len(matches)

# Example usage
text = "bHelloBob bWorldBob bBob bSomethingBob bAnotherBob"
print(find_pattern_occurrences(text))  # Output: 5

# Create a list
my_list = [1, 2, 3]

# Modify an element
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Add an element
my_list.append(4)
print(my_list)  # Output: [10, 2, 3, 4]

# Remove an element
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4]

# Create a string
my_string = "hello"

# Attempt to modify a character (this will cause an error)
# my_string[0] = 'H'  # Uncommenting this line will raise a TypeError

# Instead, create a new string
new_string = 'H' + my_string[1:]
print(new_string)  # Output: "Hello"

# The original string remains unchanged
print(my_string)  # Output: "hello"

def is_valid_url(url):
    # Check if the URL starts with a valid scheme
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    
    # Find the position of '://'
    scheme_end = url.find("://")
    
    # Extract the domain part
    domain = url[scheme_end + 3:]
    
    # Check if there's at least one dot in the domain
    if '.' not in domain:
        return False
    
    # Check if the domain has at least one character before and after the dot
    dot_position = domain.find('.')
    if dot_position == 0 or dot_position == len(domain) - 1:
        return False
    
    # If all checks pass, return True
    return True

# Example usage
print(is_valid_url("http://example.com"))  # Output: True
print(is_valid_url("https://example.com/path"))  # Output: True
print(is_valid_url("ftp://example.com"))  # Output: False
print(is_valid_url("http://example"))  # Output: False
print(is_valid_url("example.com"))  # Output: False

def days_since_birth(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))
    
    # Get the current year
    current_year = 2025  # Assuming the current year is 202 for this example
    
    # Calculate the number of full years between the birth year and the current year
    full_years = current_year - year - 1  # Exclude the birth year and the current year
    
    # Calculate the total number of days (ignoring leap years)
    total_days = full_years * 365
    
    return total_days

# Example usage
birthday = "10-06-2004"
print(days_since_birth(birthday))  # Output: 7300

print((3+10**2/2) or 70.0)  # Output: 53.0


import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
 
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c//3)
print(d)

a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Iterate over the list and modify it based on the conditions
for index in range(len(random_numbers)):
    if random_numbers[index] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[index] = random.randint(20, 30)
    else:
        # Replace numbers less than or equal to 50 with "XX"
        random_numbers[index] = "XX"

# Print the modified list
print(random_numbers)




