# Level 2 Exercises

# 1.- Sum of all numbers from 0 to 100
sum_all = sum(range(101))
print(f'The sum of all numbers is {sum_all}')

# 2.- Sum of even and odd numbers separately
sum_1 = sum(i for i in range(101) if i % 2 == 0)
sum_2 = sum(i for i in range(101) if i % 2 != 0)
print(f'The sum of all evens is {sum_all}.')
print(f'The sum of all odds is {sum_2}.')