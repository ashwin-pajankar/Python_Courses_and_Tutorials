list1 = ["Apple", "Google", "Yahoo!"]

print(list1)

print(list1[0])

list1[2] = "Microsoft"

print(list1)

for x in list1:
    print(x)

if "Apple" in list1:
    print("SUCCESS!")

print(len(list1))

list1.append("Amazon")
print(list1)

list1.remove("Amazon")
print(list1)

del list1[1]
print(list1)

list1.clear()
print(list1)