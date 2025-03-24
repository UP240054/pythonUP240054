#LEVEL 3
#1. Countries 
from countries import countries
def contains_land(country):
    return 'land' in country

land_countries = list(filter(contains_land, countries))
print(land_countries)


#2. Reverse the fruit list using a loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruit list:", reversed_fruits)




#3------------------------------------------------------------
# Import the data from countries-data.py
from countries_data import coun 

# Now you can use the `countries_data` list in your code
print(f"Number of countries: { len (coun)}")

# 2. Total number of languages in the data
all_languages = set()
for country in coun:
    all_languages.update(country['languages'])
print(f"Total number of languages: {len(all_languages)}")

# 3. Ten most spoken languages
from collections import defaultdict

language_count = defaultdict(int)
for country in coun:
    for language in country['languages']:
        language_count[language] += 1

sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
top_10_languages = sorted_languages[:10]
print("Top 10 most spoken languages:")
for language, count in top_10_languages:
    print(f"{language}: {count}")

# 4. Ten most populated countries
sorted_countries = sorted(coun, key=lambda x: x['population'], reverse=True)
top_10_populated_countries = sorted_countries[:10]
print("Top 10 most populated countries:")
for country in top_10_populated_countries:
    print(f"{country['name']}: {country['population']}")