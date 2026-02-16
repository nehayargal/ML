import json
import requests
with open("./dpla_config_secret.json") as key_file:
    key = json.load(key_file)
url = 'https://api.dp.la/v2/items'

params = {'api_key': key['api_key'], 'q': 'Artificial Intelligence and Machine Learning', 'page_size': 500}
r = requests.get(url, params=params)
print(type(r))
r.url
print(r.status_code)
data = r.content
if r.status_code == 200:
    jsonObj = json.loads(r.content)
print(jsonObj)
with open('API_Data.json', 'w') as f:
    json.dump(jsonObj, f, indent=3)

f = open('DPLA.csv', "w")
header = "Title, Publisher, Description, Date\n"
f.write(header)

for item in jsonObj["docs"]:
    if item == "docs":
        print("item"+item["docs"])
    title = item["sourceResource"]["title"]
    if "publisher" in item["sourceResource"].keys():
        publisher = item["sourceResource"]["publisher"]
    else:
        ""
    description = item["sourceResource"]["description"]
    date = item["ingestDate"]
    f.write(title[0].replace(",", " ") + "," + publisher[0].replace(",", " ") + "," + description[0].replace(",", " ")\
            + "," + date + "\n")
