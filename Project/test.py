sum_num = int(input("Enter the calculation result where x is 1: "))
base = sum_num + 1
result = int(input(f"Enter the calculation result where x is {base}: "))
remainder_dict = dict()
output = ""
power = 0

while result >= base:
    remainder = result % base
    result = int((result - remainder)/base)
    remainder_dict[f"{power}"] = remainder
    power += 1
else:
    remainder_dict[f"{power}"] = result


for key in remainder_dict:
    if key == "0":
        if remainder_dict[key] != 0:
            output += f" {remainder_dict[key]} "
    elif key == "1":
        if remainder_dict[key] == 1:
            output = f" x +" + output
        elif remainder_dict[key] != 0:
            output = f" {remainder_dict[key]}x +" + output
    else:
        if remainder_dict[key] == 1:
            output = f" x^{key} +" + output
        elif remainder_dict[key] != 0:
            output = f" {remainder_dict[key]}x^{key} +" + output

print(output[:-1])
