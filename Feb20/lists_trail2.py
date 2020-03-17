items = [1,2,4543,0,-1]
smallest = items[0] # 1
largest = items[0] # 1
for item in items:
    if item < smallest:
        smallest = item
    if item > largest:
        largest = item
print(f"smallest item in {items} is {smallest}")
print(f"smallest item in {items} is {largest}")