items = []
while True:
    input_item = int(input('Enter item to be added to list. Enter -1 to exit '))
    if input_item == -1:
        break
    items.append(input_item)
print(f'The items you entered are {items}')
new_list = []
for item in items:
    #print(item*2)
    new_list.append(item*2)
print(f'multiplied list by 2 with new result = {new_list}')
