import csv
date_string_list=[]
hour_string_list = []
time_taken_list = []
with open('/Users/sumon/sample_data.csv', 'r') as f:
    for x in f:
        #print(x)
        date_string = (x[0:11])
        #print(date_string)
        date_string_list.append(date_string)
        hour_string = (x[11:19])
        #print(hour_string)
        hour_string_list.append(hour_string)
        time_taken = (x[20:]).rstrip('\n')
        #print(time_taken)
        time_taken_list.append(time_taken)
print(date_string_list)
print(hour_string_list)
print(time_taken_list)