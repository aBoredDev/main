from os import system

input_string = input("Input: ")
input_list = list(input_string)
output_string = ""
upper = False

for i in input_list:
    if(i != ' '):
        if(upper == True):
            output_string += i.lower()
            upper = False
        else:
            output_string += i.upper()
            upper = True
    else:
        output_string += i

print("Output: %s" % output_string)
system("cmd")
