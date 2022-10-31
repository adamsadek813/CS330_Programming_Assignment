import re

unlock = '024451'
lock = '024454'

status = 'Locked.'
while True:
    raw_input = input("Input: ")
    input_str = re.sub('\D', '', raw_input)
    if len(input_str) >= 6:
        for element in range(5, len(input_str)):
            if input_str[element-5] == unlock[0] and input_str[element-4] == unlock[1] and input_str[element-3] == unlock[2] and input_str[element-2] == unlock[3] and input_str[element-1] == unlock[4] and input_str[element] == unlock[5]:
                status = 'Unlocked.'
            if input_str[element-5] == lock[0] and input_str[element-4] == lock[1] and input_str[element-3] == lock[2] and input_str[element-2] == lock[3] and input_str[element-1] == lock[4] and input_str[element] == lock[5]:
                status = 'Locked.'
        print(status)
    else:
        print(status)

    

