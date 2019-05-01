import requests
url = 'https://jsonplaceholder.typicode.com/photos'
#print(url)
response = requests.get(url)
#print(response.json())
my_json= response.json()
#print(my_json)
'''url_list = []
for x in my_json:
    url_list.append(x['url'])
print(len(url_list))
#print(my_json['url'])
#mylist = [1,2,3,4,4,7,7,9,9]
#print(set(mylist))"""
if len(url_list) != len(set(url_list)):
    print("We have duplicates")
    print(len(set(url_list)))
else:
    print("we have no duplicates")'''
#print(my_json)
from collections import defaultdict
temp_ids = []
dup_dict = []
dup_url = []
for number, row  in enumerate(my_json):
    id = row['url']
    if id not in temp_ids:
        temp_ids.append(id)
    else:
        dup_dict.append(url)
print(dup_dict)
