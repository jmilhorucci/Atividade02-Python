import requests
import json
r =requests.get('https://restcountries.eu/rest/v2/lang/it')
#print(r.text)
js = json.loads(r.text)
#print(len(js[0]["topLevelDomain"]))

class Country:
  def __init__(self, name, callingCodes, capital, population, area):

    self.name = name
    self.callingCodes = callingCodes
    self.capital = capital
    self.population = population
    self.area = area

  def __str__(self):
    return f"A(name:{self.name}, callingCodes:{self.callingCodes}, capital:{self.capital}, population:{self.population}, area:{self.area})"

CountryA = Country (
  name = (js[1]["name"]),
  callingCodes = (js[1]["callingCodes"]),
  capital = (js[1]["capital"]),
  population = int(js[1]["population"]),
  area = float(js[1]["population"])
)

print(CountryA)

#Etapa 1 - Modelar uma classe com 5 atributos simples(Integer,String,Float,Boolean) - OK 
