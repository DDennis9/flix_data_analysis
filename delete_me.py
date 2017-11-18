import pandas as pd

cities = pd.DataFrame.from_csv("cities.csv", sep="\t")
cities = cities[['Stadt', 'Einwohner']]
sum_people = cities['Einwohner'].sum()
cities['share'] = cities['Einwohner']/sum_people
cities = pd.DataFrame(cities.sort_values(by='Einwohner', ascending=True))
cities['share_cumu'] = 0.0
cumu = 0.0
for index, city in cities.iterrows():
    cities.set_value(index, 'share_cumu', cumu + city['share'])
    cumu = cumu + city['share']
    cities = pd.DataFrame(cities.sort_values(by='Einwohner', ascending=False))
print(cities)
cities.to_csv("cities.csv", sep="\t")