#  Requirements:
#     * The system should allow to update or add the products to the inventory
#     * Each Product should have 
#         * Id
#         * Name
#         * Model
#         * Cost Price
#         * Selling Price
#         * Number of Items
#     * The System should allow to sell items which means the inventory 
#        should be updated.
#     * The system should show the report of items sold
import os

def read_all_lines(filename):
    with open(filename, 'r') as file_reader:
        return file_reader.readlines()


def parse_file_into_list(filename):
    products = []
    if products_file_exists:
        all_lines = read_all_lines(filename)
        skipped_first_line = False
        for line in all_lines:
            if not skipped_first_line:
                skipped_first_line = True
                continue
            items = line.split(',')
            products.append([
                    int(items[0]),
                    items[1],
                    items[2], 
                    float(items[3]), 
                    float(items[4]), 
                    int(items[5])
                    ]
                )
    return products


def write_content_to_file(products,filename, is_append=True):
    if not is_append:
        os.remove(filename)
    products_file_exists = os.path.exists(filename)
    with open(file= filename, mode= 'a') as products_file_appender:
            if not products_file_exists:
                products_file_appender.writelines(
                    ['id,name,model,cp,sp,quanity\n'])
                products_file_exists = True
            
            for product in products:
                products_file_appender.write(f"{product[0]},{product[1]},{product[2]},{product[3]},{product[4]},{product[5]}\n")


def collect_product_from_input():
    id = int(input('Enter the product id = '))
    name = input('Enter the product name = ')
    model = input('Enter the model = ')
    cp = float(input('Enter the cost price = '))
    sp = float(input('Enter the sell price = '))
    quantity = int(input('Enter the availablie quantity = '))
    product = [id,name,model,cp, sp,quantity]
    return product


products_file = "products.csv"
products_file_exists = os.path.exists(products_file)
products = parse_file_into_list(products_file)

while True:
    menu = """
    Enter the number 
    0 => View Products
    1 => Add Product
    2 => Update Product
    3 => Delete Product
    4 => Sell Items
    5 => Report
    6 => Exit
    """
    choice = input(menu)
    if choice == '0':
        if not products:
            print('No items in inventory')
            continue
        # open the file in the read mode
        for product in products:
            print(product)
    elif choice == '1':
        # to write the files, use a(append) mode
        product = collect_product_from_input()
        products.append(product)
        write_content_to_file([product],products_file)
        
    elif choice == '2' :
        product_id = int(input('Enter the product id to update quantity = '))
        index = -1
        updated_product = []
        for product in products:
            # find product by id
            index += 1
            if product[0] == product_id:
                found = True
                new_quantity = int(input('Enter the quantity to be added = '))
                product[5] += new_quantity
                updated_product = product
                break
        products[index] = updated_product
        write_content_to_file(products,products_file, is_append=False)
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        exit(0)

