import json
import requests

url = "https://aoudiop.pythonanywhere.com/api/GetPizzas"
data = requests.get(url)
#print(data.text)
# deseriliser
pizzas = json.loads(data.text)
# print(pizzas)

for pizzaMondel in pizzas:
    pizza = pizzaMondel['fields']
    print(pizza['nom'])