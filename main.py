import shop_functions

# while True:
#     shop_functions.print_products(shop_functions.products, shop_functions.itemsCount)
#     user_input = shop_functions.read_input()
#
#     if user_input == 0:
#         shop_functions.print_shopping_cart(shop_functions.shopping_cart)
#         print("thanks for purchase")
#     else:
#         if shop_functions.is_input_valid(user_input):
#             #buying_product = shop_functions.products[user_input]
#             shop_functions.shopping_cart.append(user_input)
user_buying = 1

while True:

    #shop_functions.print_shopping_cart(shop_functions.shopping_cart)
    #shop_functions.print_products(shop_functions.products, shop_functions.itemsQuantity)
    shop_functions.user_shopping(shop_functions.shopping_cart, shop_functions.products, shop_functions.itemsQuantity,
                                 shop_functions.itemsCount)




