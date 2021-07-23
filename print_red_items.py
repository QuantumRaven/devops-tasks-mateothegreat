##############
# Fruit loop
##############

# Loops, If Statements, Define Methods

import json

# Open basket.json
with open("./basket.json") as file:
    data = json.load(file)

# Print red items
for item in data["basket"]:
    if item["color"] == "red":
        print(item)
