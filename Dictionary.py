colors = ["red", "blue", "green", "orange", "yellow"]
names = ["name1", "name2", "name3", "name4", "name5"]
# creating a dictionary
sample1 = {
    "name1": "red",
    "name2": "blue",
    "name3": "green",
    "name4": "orange",
    "name5": "yellow"
}

# accessing values of a dictionary
print(sample1)
print(sample1['name1'])

# getting the list of keys
print(sample1.keys())

# values of the dictionary
print(sample1.values())

for key in sample1.keys():
    print(key,sample1[key])

# Check if a key exists in a dictionary or not

if "name17" in sample1:
    print(sample1["name2"])
else:
    print("This key does not exist!")

# Adding a key and value pair
sample1["name17"] = "purple"
print(sample1)

# Delete a key and value pair
del(sample1["name2"])
print(sample1)

# Changing the value of a dictionary
sample1["name1"] = "yellow and green"
print(sample1)



# store a list as a value in a dictionary
sample1["Marks"] = [10,29,43]
print(sample1)

# Accessing a value of list from the dictionary
print(sample1["Marks"][1])

# Creating a nested dictionary
classroom = {
    "tom":{
        "name":"tom",
        "age":23,
        "marks":[90,45,32,99]
    },
    "bobby":{
        "name":"bobby",
        "age":22,
        "marks":[89,53,99,103] 
    }
}

print(classroom.keys())
print(classroom.values())

for key in classroom:
    print(key,classroom[key])

print(classroom["tom"]["age"])