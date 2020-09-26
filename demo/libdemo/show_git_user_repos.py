import requests

resp = requests.get("https://api.github.com/users/srikanthpragada/repos")
repos = resp.json()  # Convert array of JSON objects to list of dict

for repo in repos:
    createdat = repo['created_at']
    if createdat.startswith("2020"):
        print(repo['name'])
