import requests
import json

response = requests.get("https://www.federalregister.gov/api/v1/documents?conditions=&format=json&page=1")
todos = json.loads(response.text)


todos == response.json()
print("Key Fields in Response")
for key in todos['results'][0]:
    print(key)

print()

for tot in range(19):
    print()
    print(todos['results'][tot]['title'])
    print(todos['results'][tot]['publication_date'])
    print()
    print(todos['results'][tot]['abstract'])
    print()


