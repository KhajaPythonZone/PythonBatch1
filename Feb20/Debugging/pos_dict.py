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
# structure of dictionary will be
# {
#   '<code>' :  {
#        'name': '<product name>',
#        'quantity': <product quantity> 
#   }  
# }

# example:
#  products = {
#      'dell': { 'name': 'dell', 'cp': 30000, 'sp': 34000, 'quantity': 20, 'model': 'latitude'},
#      'hp': { 'name': 'hp', 'cp': 30000, 'sp': 34000, 'quantity': 20, 'model': 'elitebook'},
# }

products = {}

def ask_user_input(purpose):
    # This function asks for user input with custom message and returns the values
    user_input = input(f"Enter the {purpose} = ")
    return user_input

def does_product_exists(code):
    # returns whether the code exists or not
    return code in products.keys()



while True:
    choice = input(menu)
    if choice == '0':
        for code, product in products.items():
            print(f"{code} = {product}")
    elif choice == '1':
        code = input('Enter the product code name = ')
        if code in products:
            print(f'{code} already exists')
            continue
        product = {}
        product['name'] = ask_user_input('product name')
        product['model'] = ask_user_input('model')
        product['cp'] = float(ask_user_input('cost price'))
        product['sp'] = float(ask_user_input('selling price'))
        product['quantity'] = int(ask_user_input('available quantity'))
        products[code] = product
    elif choice == '2':
        code = ask_user_input('product code name')
        if code not in products.keys():
            print('Invalid code entered. Please check the code')
            continue
        quantity = int(ask_user_input('quantity to be added'))
        new_quantity = quantity + products[code]['quantity']
        products[code]['quantity'] = new_quantity
        print(f'quantity updated and new quantity is {new_quantity}')
    elif choice == '3':
        code = ask_user_input('product code name')
        if code not in products.keys():
            print('Invalid code entered. Please check the code')
            continue
        return_product = products.pop(code)
        print(f"{return_product} has been deleted")
    else:

        exit(0)


