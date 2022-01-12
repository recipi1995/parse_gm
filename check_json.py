import json

file = open(f'moscow.json','r', encoding='utf8')
data = json.load(file)

print(len(data))

file = open(f'moscow_updated.json','r', encoding='utf8')
data = json.load(file)

print(len(data))
