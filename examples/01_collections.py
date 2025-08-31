fruits = ["apple", "banana", "mango"]
print("First fruit:", fruits[0])
fruits.append("orange")
print("All fruits:", fruits)

for i, f in enumerate(fruits, start=1):
    print(i, f)

person = {"name": "Doris", "age": 40}
print("Person name:", person["name"])
person["city"] = "Accra"
print("Person:", person)

lengths = [len(f) for f in fruits]
print("Lengths:", lengths)