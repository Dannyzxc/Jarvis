import json

data1 = '{ "var1":"harry", "var2":"danny"}'
parsed = json.loads(data1)
print(parsed['var1'])
parsed = json.load

#converted to javascript file

data2 = { "fridge": ["coke", 'ice'], "kitchen": ("onion", "potato", 45), "storeroom": "broom", "isbad": False}
jscomp = json.dumps(data2)
print(jscomp)