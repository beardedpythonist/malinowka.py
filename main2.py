import requests

response = requests.options('http://google.com')
zapros = requests.request(url='http://onliner.by', method="GET")


print(response.headers)


for key, val in response.headers.items():
     print(f' ключ:  {key}, значение: {val}')
