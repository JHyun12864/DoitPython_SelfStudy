import json

with open('./json_test/myinfo.json', encoding='UTF-8') as f:
    data = json.load(f)


print(type(data))