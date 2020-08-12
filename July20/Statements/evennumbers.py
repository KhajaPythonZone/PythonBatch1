index = int(input("Enter the starting number :"))
end = int(input("Enter the ending number :"))
while index <= end:
    if index%2 == 0:
        print(index)
    index = index + 1