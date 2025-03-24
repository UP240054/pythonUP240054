# LEVEL 1 

# 1.- Iterate 0 to 10 using for loop
for i in range(11):
    print(i)

# 2.- Iterate 0 to 10 using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# 3.- Iterate 10 to 0 using for loop
for i in range(10, -1, -1):
    print(i)

# 4.- Iterate 10 to 0 using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# 5.- Print triangle pattern
for i in range(1, 8):
    print('#' * i)

# 6.- Print nested loop pattern
for i in range(8):
    for j in range(8):
        print('# ', end='')
    print()

# 7.- Print multiplication pattern
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 8.- Iterate through a list and print items
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tech_list:
    print(tech)

# 9.- Print even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i)

# 10.- Print odd numbers from 0 to 100
for i in range(1, 101, 2):
    print(i)