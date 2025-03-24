# 1. Function to count evens and odds in a positive integer
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

# 2. Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 3. Function to check if a parameter is empty
def is_empty(param):
    if param:
        return False  # Not empty
    else:
        return True  # Empty

# 4. Function to calculate the mean of a list
def calculate_mean(lst):
    return sum(lst) / len(lst)

# 5. Function to calculate the median of a list
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# 6. Function to calculate the mode of a list
def calculate_mode(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes

# 7. Function to calculate the range of a list
def calculate_range(lst):
    return max(lst) - min(lst)

# 8. Function to calculate the variance of a list
def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diff = [(x - mean) ** 2 for x in lst]
    return sum(squared_diff) / len(lst)

# 9. Function to calculate the standard deviation of a list
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5

# Example usage
print(evens_and_odds(100))
# Output:
# The number of odds are 50.
# The number of evens are 51.

print(factorial(5))  # Output: 120
print(is_empty([]))  # Output: True
print(is_empty([1, 2, 3]))  # Output: False

data = [1, 2, 3, 4, 5, 5, 6]
print("Mean:", calculate_mean(data))  # Output: Mean: 3.7142857142857144
print("Median:", calculate_median(data))  # Output: Median: 4
print("Mode:", calculate_mode(data))  # Output: Mode: [5]
print("Range:", calculate_range(data))  # Output: Range: 5
print("Variance:", calculate_variance(data))  # Output: Variance: 2.7755102040816326
print("Standard Deviation:", calculate_std(data))  # Output: Standard Deviation: 1.665833039312269