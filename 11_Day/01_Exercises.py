# 1. Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# 2. Function to calculate the area of a circle
def area_of_circle(r):
    pi = 3.14159  # Approximate value of π
    return pi * r * r

# 3. Function to add all numbers in arguments
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "All arguments must be numbers."
    return total

# 4. Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Function to check the season based on the month
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

# 6. Function to calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# 7. Function to solve a quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"

# 8. Function to print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

# 9. Function to reverse a list using loops
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Function to capitalize each item in a list
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Function to add an item to a list
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Function to remove an item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Function to sum all numbers in a range
def sum_of_numbers(n):
    return sum(range(1, n + 1))

# 14. Function to sum all odd numbers in a range
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

# 15. Function to sum all even numbers in a range
def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

# Example usage
print(add_two_numbers(3, 5))  # Output: 8
print(area_of_circle(5))  # Output: 78.53975
print(add_all_nums(1, 2, 3, 4, 5))  # Output: 15
print(convert_celsius_to_fahrenheit(25))  # Output: 77.0
print(check_season(4))  # Output: Spring
print(calculate_slope(1, 2, 3, 4))  # Output: 1.0
print(solve_quadratic_eqn(1, -3, 2))  # Output: (2.0, 1.0)
print_list([1, 2, 3, 4, 5])  # Output: 1 2 3 4 5 (each on a new line)
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(capitalize_list_items(["apple", "banana", "cherry"]))  # Output: ['Apple', 'Banana', 'Cherry']
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat'))  # Output: ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))  # Output: ['Potato', 'Tomato', 'Milk']
print(sum_of_numbers(5))  # Output: 15
print(sum_of_odds(10))  # Output: 25
print(sum_of_even(10))  # Output: 30