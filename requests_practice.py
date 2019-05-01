import requests
print("import of the requests module is successful")
url = 'https://jsonplaceholder.typicode.com/photos'
print(url)
response = requests.get(url)
#print(response.json())
for obj in response:
    print(obj)
jsonPayload = {'albumID':1, 'title':'test', 'url':'nothingreally.com', 'thumbnailUrl': 'nothing.com'}
print(jsonPayload)
response= requests.delete(url, json=jsonPayload)
response.json()
print(response)
url='https://jsonplaceholder.typicode.com/photos/100'
response=requests.put(url,jsonPayload)
print(response)
response=requests.delete(url)
print(response)
response.json()