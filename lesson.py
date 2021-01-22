
#If the sum of the two magic numbers = 13. Set the second number to 1 and  tripple the first number
#Otherwise, incrament both numbers by 1

magic_number = 7
second_magic_number =  5

if magic_number + second_magic_number == 13: #Conditional Statement
    magic_number = magic_number * 3 # magic_number *= 3
    second_magic_number = 1
else:
    magic_number = magic_number + 1 # magic_number += 1
    second_magic_number = second_magic_number + 1