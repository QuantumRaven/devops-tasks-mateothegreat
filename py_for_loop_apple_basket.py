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
# for item in data["basket"]:
#     print(item)

# Print a specific color, yellow
# for item in data["basket"]:
#     if i["color"] == "yellow":
#         print(i["color"])

# Print red items
# for item in data["basket"]:
#     if item["color"] == "red":
#         print(item)

# Python addition function with arguments
def add(a, b):
    return a + b


print(add(9, 100))

# Python subtraction function with args
def sub(c, d):
    return c - d


print(sub(100, 9))

# Python division function
def div(e, f):
    return e / f


print(div(10, 5))

# Python return value as argument - Addition
print(add(sub(109, 10), 200))

# Python return value as argument - Subtraction
print(sub(add(100, 100), 50))


# Add quantity for total
total = 0
for item in data["basket"]:
    print(item["quantity"])
    total += item["quantity"]
print(total)

print()

# Function to print basket total
# def = define method
def bastot():
    print(total)
bastot()
