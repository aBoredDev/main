from os import system

input_string = str(input(""))
output_string = ""
input_list = list(input_string)

for i in range(len(input_list)):
    if (i % 2) != 0:
        output_string += input_list[i].upper()
    else:
        output_string += input_list[i].lower()

print(output_string)

system("cmd")
