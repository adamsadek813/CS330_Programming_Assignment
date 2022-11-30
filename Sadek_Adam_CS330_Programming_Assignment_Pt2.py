import time
from random import randint

unlock = '664571'

def generator():
    return str(randint(0,9))
print("Generating data. This should take about one minute...")
time_taken = 0
list_of_times = []
list_of_numbers = []
total_count = 0
for x in range(20):
    rand_num = ''
    counter = 0
    found = False
    start = time.time()
    while found == False:
        if(len(rand_num) >= len(unlock)):
            if rand_num[len(rand_num)-1] == unlock[5] and rand_num[len(rand_num)-2] == unlock[4] and rand_num[len(rand_num)-3] == unlock[3] and rand_num[len(rand_num)-4] == unlock[2] and rand_num[len(rand_num)-5] == unlock[1] and rand_num[len(rand_num)-6] == unlock[0]:
                found = True
            else:
                rand_num = rand_num + generator()
                counter = counter + 1
        else:
            rand_num = rand_num + generator()
            counter = counter + 1
    end = time.time()
    list_of_times.append(end-start)
    list_of_numbers.append(counter)
    time_taken = time_taken + (end - start)
    total_count = total_count + counter
average_time = time_taken / 20
average_counter = total_count / 20
max_time =  max(list_of_times,key=lambda x:float(x))
min_time = min(list_of_times,key=lambda x:float(x))
max_numbers_needed = max(list_of_numbers,key=lambda x:float(x))
min_numbers_needed = min(list_of_numbers,key=lambda x:float(x))
print("Times to find access code (sec):")
print("     Average: " , average_time)
print("     Minimum: ", min_time)
print("     Maximum: ", max_time)
print("Symbols needed to find access code:")
print("     Average: " , average_counter)
print("     Minimum: ", min_numbers_needed)
print("     Maximum: ", max_numbers_needed)

    

