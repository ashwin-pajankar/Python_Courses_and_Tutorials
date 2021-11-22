dict1 = {"brand": "Intel",
         "model": "8008",
         "year": 1972}

print(dict1)

print(dict1["brand"])

print(dict1.get("model"))

dict1["brand"] = "AMD"

dict1["model"] = "Ryzen"

dict1["year"] = 2017

print(dict1)

for x in dict1:
    print(x)

for x in dict1:
    print(dict1[x])

for x in dict1.values():
    print(x)

for x, y in dict1.items():
    print(x, y)

print(len(dict1))

dict1["color"] = "Red"

for x, y in dict1.items():
    print(x, y)

del dict1["model"]

for x, y in dict1.items():
    print(x, y)

dict1.clear()
print('------')
for x, y in dict1.items():
    print(x, y)

del dict1
