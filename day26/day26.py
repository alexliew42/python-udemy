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
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# # squared_numbers = [num * num for num in numbers]

# # print(squared_numbers)



# result = [number for number in numbers if number % 2 == 0]

# print(result)

# file1 = open('file1.txt', 'r')
# file2 = open('file2.txt', 'r')
# x1 = file1.readlines()
# x2 = file2.readlines()

# file1_list = [int(num.replace("/n", "")) for num in x1]
# file2_list = [int(num.replace("/n", "")) for num in x2]

# result = [number for number in file1_list if number in file2_list]



# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# sentence_list = sentence.split(" ")

# word_dict = {word:len(word) for word in sentence_list}

# print(word_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_dict = {day[0]:(day[1] * (9/5) + 32) for day in weather_c.items()}

print(weather_dict)