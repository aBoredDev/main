# Import statements
#   shop contains all the classes required
import shop
#   To run the cls command and clear the output
from os import system
# To decode and encode the JSON
import json
# To facilitate easy access to .shop files
from sys import argv

main = None
# Variable and object definitions
items = None
if len(argv) == 1:
    items = []
    items.append(shop.Item("Demo", 1, 0.5))
    system("cls")
    main = shop.Shop("Demo", items, 0.0)
else:
    file = open(str(argv[1]), 'r')
    file.seek(0)
    jsonitems = json.loads(file.read())['items']
    file.seek(0)
    name = json.loads(file.read())['name']
    file.seek(0)
    profit = json.loads(file.read())['profit']
    system("cls")
    items = []
    for i in jsonitems:
        items.append(shop.Item(i['name'], i['amount'], i['min_cost']))
    main = shop.Shop(name, items, profit)

# Main loop
while True:
    main.loop()
