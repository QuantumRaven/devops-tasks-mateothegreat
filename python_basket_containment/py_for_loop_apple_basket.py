##############
# Fruit loop
##############

# Loops, If Statements, Define Methods

import json

# Open basket.json
with open("./basket.json") as file:
    data = json.load(file)

# Create a loop with basket.json's data that prints the fruit name
# and its color
for item in data["basket"]:
    print(item)
