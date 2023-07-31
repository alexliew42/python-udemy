# name = "Alex"
# new_list = [a for a in name]
# print(new_list)

# # double the numbers in range(1,5)

# doubled_numbers = [n * 2 for n in range(1, 5)]
# print(doubled_numbers)

# names = ['Alex', 'Beth', "Caroline", 'Dave', 'Eleanor', 'Freddie']

# # short_names = [short for short in names if len(short) <= 4]
# # print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]

# print(long_names)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]

print(squared_numbers)