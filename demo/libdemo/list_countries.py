import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()  # Convert array of JSON objects to list of dict

# Take top 10 countries by population
for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{country['name']:50} {country['population']:10}")
