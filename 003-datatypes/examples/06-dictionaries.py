#!/usr/bin/env python3

# dictionaries (dict) are unordered list with key-value pairs.
# the value can be any data type like string, int, float, dict, list etc.
# a dictionaries structure: {"key1": "value1", "key2": 402, "key3": ["Sweden", "Usa"]}

country = {"name": "Sweden", "language": "swedish",
           "capitol_city": "Stockholm", "citizens": 10223500}
# prints the whole dictionary
print(country)

# to get a specific value you call yourdict["key"]
print("Country name:", country["name"])
print("Country language:", country["language"])
print("Country capitol city:", country["capitol_city"])
print("Country citizens count:", country["citizens"])

# you can change a key value.
country["name"] = "Usa"
print("Country dict after name change:", country)

# to get all key names in a dict as an list.
print("Keys:", country.keys())

# to get all key values in a dict as an list.
print("Values:", country.values())

# you can also create a new key value pair in a dictionary
country['eu_member'] = True
print("Dictionary after adding a key with value:", country)
