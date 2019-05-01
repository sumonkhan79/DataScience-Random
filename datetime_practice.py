import datetime
dt1=datetime.date(1979,10,11)
dt2=datetime.date(2011,5,1)
#print(max(dt1,dt2))
diff = dt2 - dt1
#print(diff)

century_start = datetime.datetime(2000,1,1,0,0,0)
today = datetime.datetime.now()
days_in_century = today - century_start
#print("We are", days_in_century, " minutes  in the current century")

def add_to_time(time_object, time_delta):
    import datetime
    temp_datetime_object = datetime.datetime(500,1,1,time_object.hour, time_object.minute, time_object.second)
    #print(temp_datetime_object)
    return (temp_datetime_object+time_delta).time()

# String convert to datetime object in Python
date = '01-APR-13'
date_obj = datetime.datetime.strptime(date,'%d-%b-%y')
#print(date_obj)

# Datetime object conversion to Python
now = datetime.datetime.now()
#print(now)
string_now = datetime.datetime.strftime(now, '%m/%d/%y %h:%m:%s')
#print(string_now)
#print(str(now))
#print(dir(datetime))

nas_dob = datetime.date(1979,3,1)
print(nas_dob)
shawpna_dob = datetime.date(1980,11,19)
launch_date = datetime.date(1979,1,1)
launch_time = datetime.time(11,11,11)
launch_datetime = datetime.datetime(1980,1,1,11,11,11)
print(launch_date)
print(launch_time)
print(launch_datetime)
now = datetime.datetime.now()
print(now)
td = shawpna_dob + datetime.timedelta(days=100)
diff = launch_date - shawpna_dob
print(diff)