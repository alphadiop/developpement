import json
import requests
import pandas as pd
url = "https://alphadiop.pythonanywhere.com/api/GetPizzas"
data = requests.get(url)
print(data.text)
# deseriliser
pizzas = json.loads(data.text)
dico_pizza = [pizzaMondel['fields'] for pizzaMondel in pizzas]
dataframe = pd.DataFrame.from_dict(dico_pizza)
print('\n')

# for pizzaMondel in pizzas:
#     pizza = pizzaMondel['fields']
#     print(pizza['nom']+ " : " +str(pizza['prix']))

print(dataframe)