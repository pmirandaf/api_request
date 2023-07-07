
#Consumindo API do Github

import requests

username = input('Qual seu nome? ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()  


if response.status_code == 200:
    # print(data)
    print(f'ID: {data["id"]}')
    print(f'Nome Completo: {data["name"]}')
    print(f'Location: {data["location"]}')
else:
        print('Error')


#teste2
# print('Github Users')