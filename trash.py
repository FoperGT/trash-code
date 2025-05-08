items = [
    {'name': 'apple', 'price': 2, 'quantity': 5},
    {'name': 'banana', 'price': 1, 'quantity': 10},
    {'name': 'apple', 'price': 2, 'quantity': 3},
    {'name': 'orange', 'price': 3, 'quantity': 2},
    {'name': 'banana', 'price': 1, 'quantity': 4},
    {'name': 'kiwi', 'price': 5, 'quantity': 1}
]

total = 0
total_items = 0
names = []
max_price = 0
max_items = []

for i in range(0, len(items)):
    total = total + items[i]['price'] * items[i]['quantity']
    total_items = total_items + items[i]['quantity']
    if not items[i]['name'] in names:
        names.append(items[i]['name'])
    if items[i]['price'] > max_price:
        max_price = items[i]['price']
        max_items = [items[i]['name']]
    elif items[i]['price'] == max_price:
        if not items[i]['name'] in max_items:
            max_items.append(items[i]['name'])

avg = 0
if total_items != 0:
    avg = total / total_items

print("Total cost is " + str(total))
print("Average item price: " + str(avg))
print("Unique items: " + str(names))
print("Most expensive items: " + str(max_items))
