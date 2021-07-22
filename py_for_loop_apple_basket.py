##############
# Fruit loop
##############
import json

# Open basket.json
with open('./basket.json') as f:
    data = json.load(f)

# Create a loop with basket.json's data that prints the fruit name and its color
for i in data["basket"]:
    print(i)
