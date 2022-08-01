import json

data = '{"var1":"ankit", "var2":56}'
# print(data)
# we can do the same task in this format also but here we call call through index value also

parsed = json.loads(data)
print(parsed['var1'])

# json.loads is used to print int the dictionary form

data2 = {
    "channel_name": "ankitcoder.me",
    "cars": ['bmw', 'audi a8', 'ferrai'],
    "fridge": ('roti', 679),
    "islaam": False
}

jscomp = json.dumps(data2)      # it conveted the whole java script into the python an compatable that is run into the python 
print(jscomp)
