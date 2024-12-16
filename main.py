# Kaprekar's Constant

def split_number(num):
    numstr = str(num).ljust(4, '0')
    return [int(i) for i in numstr]
    
def max_value(digits):
    digits.sort(reverse = True)
    return int(''.join(map(str,digits)))
    
def min_value(digits):
    digits.sort()
    return int(''.join(map(str,digits)))
    
def diff_value(max_num, min_num, counter):
    diff = max_num - min_num
    print(f"{counter}:\t {max_num} - {min_num} \t = {diff}")
    return diff

numstr = input("Enter a 4 digit number in which at least 1 digit should be different from others: \n")
if len(numstr) != 4:
    print(f"Error: Entered value is not a 4 digit number {numstr}")
    exit()
if numstr.isnumeric() == False:
    print(f"Error: Entered value is not a 4 digit number {numstr}")
    exit()
    
num = int(numstr)
counter = 1
digits = split_number(num)
diff = diff_value(max_value(digits), min_value(digits), counter)
while (diff != 6174):
    counter+=1
    digits = split_number(diff)
    diff = diff_value(max_value(digits), min_value(digits), counter)
