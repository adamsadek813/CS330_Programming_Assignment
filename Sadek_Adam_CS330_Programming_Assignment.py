import re

main_key = '66457'
unlock = '1'
lock = '4'
status = 'Locked.'

def LockPad(status):
    while True:
        raw_input = input("Input: ")
        input_str = re.sub('\D', '', raw_input)
        if len(input_str) >= 6:
            for element in range(5, len(input_str)):
                if input_str[element-5] == main_key[0] and input_str[element-4] == main_key[1] and input_str[element-3] == main_key[2] and input_str[element-2] == main_key[3] and input_str[element-1] == main_key[4] and input_str[element] == unlock:
                    status = 'Unlocked.'
                if input_str[element-5] == main_key[0] and input_str[element-4] == main_key[1] and input_str[element-3] == main_key[2] and input_str[element-2] == main_key[3] and input_str[element-1] == main_key[4] and input_str[element] == lock:
                    status = 'Locked.'
                print(status)
        else:
            print(status)

if __name__ == "__main__":
  LockPad(status)