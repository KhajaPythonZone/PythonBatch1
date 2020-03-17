import os

for root, dirs, files in os.walk(r'C:\temps\test'):
    for name in files:
        print(os.path.join(root, name))

    for name in dirs:
        print(os.path.join(root, name))