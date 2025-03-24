# 1. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 2. Function to check if all items in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Function to check if all items in a list are of the same data type
def all_same_type(lst):
    if not lst:
        return True  # Empty list is considered as having the same type
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

# 4. Function to check if a variable name is a valid Python variable
def is_valid_variable(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

#----------------------------------------
from countries_data import count

#------------------------------------------

# 5. Function to find the most spoken languages in the world
def most_spoken_languages(countries_data, top_n=10):
    language_count = {}
    for country in countries_data:
        for language in country["languages"]:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

# 6. Function to find the most populated count in the world
def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    return [(country["name"], country["population"]) for country in sorted_countries[:top_n]]

# Example usage
print(is_prime(29))  # Output: True
print(is_prime(15))  # Output: False

print(all_unique([1, 2, 3, 4, 5]))  # Output: True
print(all_unique([1, 2, 2, 3, 4]))  # Output: False

print(all_same_type([1, 2, 3, 4]))  # Output: True
print(all_same_type([1, 2, "three", 4]))  # Output: False

print(is_valid_variable("valid_var"))  # Output: True
print(is_valid_variable("2invalid_var"))  # Output: False

# Most spoken languages
print("Most spoken languages:")
print(most_spoken_languages(count, top_n=10))

# Most populated count
print("Most populated count:")
print(most_populated_countries(count, top_n=10))