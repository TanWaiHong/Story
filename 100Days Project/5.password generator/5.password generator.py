import random

# print(random.sample(range(10), 10))


def ran_letter(a, b):
    for x in range(b):
        y = random.randint(0, len(letters) - 1)
        a.append(letters[y])
    return


def ran_number(a, b):
    for x in range(b):
        y = random.randint(0, len(numbers) - 1)
        a.append(numbers[y])
    return


def ran_symbol(a, b):
    for x in range(b):
        y = random.randint(0, len(symbols) - 1)
        a.append(symbols[y])
    return


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = list()

password = ""

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

count_sum = letters_count + symbols_count + numbers_count

ran_letter(password_list, letters_count)
ran_number(password_list, numbers_count)
ran_symbol(password_list, symbols_count)

sample_list = random.sample(range(count_sum), count_sum)

for num in sample_list:
    password += password_list[num]

print(password)
