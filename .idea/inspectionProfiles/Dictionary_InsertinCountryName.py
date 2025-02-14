country = {}

for i in range(4):
    name = input("Enter the country name ")
    if name[0].upper() not in country:
        country[name[0].upper()] = [name]

    else:
        country[name[0].upper()].append(name)

print(country)