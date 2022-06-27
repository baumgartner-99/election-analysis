#ensure the python interpreter is active

print("Hello World")

#create a list of counties
counties = ["Arapahoe", "Denver", "Jefferson"]
counties

#practice indexing
counties[0]
print(counties[2])
print(counties[-1])
len(counties)

#add to list
counties.append("El Paso")
counties

#remove from list
counties.remove("El Paso")

#or

counties.append("El Paso")
counties.pop(3)

#insert at specific spot
counties.insert(0, "El Paso")

#create a dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

#retrieve keys
counties_dict.keys()

#retrieve values
counties_dict.values()

#list of dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#skill drill
voting_data.insert(1, {"county": "El Paso", "registered_voters": 461149})
voting_data.pop(0)
voting_data.pop(1)
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

#if statements
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#membership operators
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

#logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for loops
counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

i = len(counties)
for i in range(len(counties)):
    print(counties[i])

#for loops in counties dictionary
counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

for county in counties_dict.keys():
    print(county, end=" ")
    print("county has")
for voters in counties_dict.values():
    print(voters, end=" ")
    print("registered voters.")

#skill drill print in full sentence for each county
for county, voters in counties_dict.items():
    print(county, end= " ")
    print("county has", end= " ")
    print(voters, end =" ")
    print("registered voters.")

#another option:
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#using f strings:
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#get the values from a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#skill drill formatting floating-point decimals
counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")