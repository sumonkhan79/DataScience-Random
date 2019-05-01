'''def get_data(filename):
    data_tuples = list()
    with open(filename,'r') as f:
        for line in f:
            data_tuples.append(line.strip().split(','))
            #print(data_tuples)
        import datetime
        format_str = "%Y-%m-%d %H:%M:%S"
        data_tuples=[(datetime.datetime.strptime(x[0],format_str).hour,float(x[1])) for x in data_tuples]
        return data_tuples
        #for x in data_tuples:
         #   print(x)

get_data('/Users/sumon/sample_data.csv')
buckets = dict()
#print(buckets)
for x in get_data('/Users/sumon/sample_data.csv'):
    if x[0] in buckets:
        #print(buckets[x[0]][0])
        buckets[x[0]][0] +=1
        buckets[x[0]][1] +=x[1]
    else:
        buckets[x[0]] = [1,x[1]]
print(buckets)
for key, value in buckets.items():
    #print("Hours:", key, "average processing time", value[1]/value[0])'''

def get_average_per_hour(filename):
        def get_data(filename):
            data_tuples = list()
            with open(filename, 'r') as f:
                for line in f:
                    data_tuples.append(line.strip().split(','))
            # print(data_tuples)
            import datetime
            format_str = "%Y-%m-%d %H:%M:%S"
            data_tuples = [(datetime.datetime.strptime(x[0], format_str).hour, float(x[1])) for x in data_tuples]
            return data_tuples
        buckets = dict()
    # print(buckets)
        for x in get_data(filename):
            if x[0] in buckets:
            # print(buckets[x[0]][0])
             buckets[x[0]][0] += 1
             buckets[x[0]][1] += x[1]
            else:
                buckets[x[0]] = [1, x[1]]
        return [(key, value[1]/value[0]) for key, value in buckets.items()]
print(get_average_per_hour('/Users/sumon/sample_data.csv'))
