langs = ['Python', 'Java', 'TypeScript']
vers = [3.8, 14, 3.5]

# for l in langs:
#     print(l)

for idx, value in enumerate(langs):
    print(idx + 1, value)

for idx, value in enumerate(langs):
    print(value, vers[idx])

for name,ver in zip(langs,vers):
    print(f"{name:15} {ver:5}")