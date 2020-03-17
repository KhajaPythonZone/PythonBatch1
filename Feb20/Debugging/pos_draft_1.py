#  Requirements:
#     * The system should allow to update or add the products to the inventory
#     * Each Product should have 
#         * Id
#         * Name
#         * Model
#         * Cost Price
#         * Selling Price
#         * Number of Items
#     * The System should allow to sell items which means the inventory should be updated.
#     * The system should show the report of items sold

products = []
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
        if len(products) == 0:
            print('No items in inventory')
            continue
        print("id, name, model, cost price, selling price, available")
        for product in products:
            print(f'{product[0]}, {product[1]}, {product[2]}, {product[3]}, {product[4]}, {product[5]}')
    elif choice == '1':
        id = int(input('Enter the product id = '))
        name = input('Enter the product name = ')
        model = input('Enter the model = ')
        cp = float(input('Enter the cost price = '))
        sp = float(input('Enter the sell price = '))
        quanity = int(input('Enter the availablie quantity = '))
        product = [id,name,model,cp, sp,quanity]
        products.append(product)
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


    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        exit(0)

    




