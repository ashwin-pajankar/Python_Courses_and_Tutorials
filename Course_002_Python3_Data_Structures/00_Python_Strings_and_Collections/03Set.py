set1 = {"Apple", "Amazon", "Microsoft"}
print(set1)

#print(set1[0])

if "Apple" in set1:
    print("SUCCESS!")

set1.add("Yahoo!")
print(set1)

set1.update(["Google", "Adobe"])
print(set1)

print(len(set1))

set1.remove("Apple")
print(set1)

set1.clear()
print(set1)

del set1
print(set1)