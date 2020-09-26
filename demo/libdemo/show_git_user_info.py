
import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
details = resp.json()  # Convert JSON to dict

print("Full name  : ", details['name'])
print("Company    : ", details['company'])
print("Joined On  : ", details['created_at'])
