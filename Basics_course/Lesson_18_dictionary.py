# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russai": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

capitals.get("USA")

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")




# capitals.update({"Germany": "Berlin"}) - can insert a new 
# capitals.update({"USA:": "Detroit"}) - or update an already existing one
# capitals.pop("China") - remove a key value pair
# capitals.popitem() - remove the latest one
# capitals.clear() - clears the dictionary
# capitals.keys() - get all of the keys but not the values
# capitals.values() - get only the values
# capitals.items() - returns a dictionary object that resembles a 2d list tuple

print(capitals)