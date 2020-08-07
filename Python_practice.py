print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
len(counties)
print (counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
print (counties_tuple[1])
counties_dict = {"Arapahoe": 422829, "Denver" : 463353, "jefferson": 43238}
print (counties_dict)
items = counties_dict.items()
print (items)
keys = counties_dict.keys()
print (keys)
print (counties_dict["Arapahoe"])
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voter":422829})
voting_data.append({"county":"Denver", "registered_voters":463365})
voting_data.append({"county":"Jefferson", "regisered_voters":432438})
print  (voting_data)





