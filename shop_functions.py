import random

products = {
    "apple": 5,
    "peach": 5,
    "mandarin": 5,
    "mango": 8,
    "pineapple": 8,
    "dragonfruit": 10,
}

shopping_cart = []


def num_of_items(products):
    itemsNumber = len(products)
    return itemsNumber


def products_generator(itemsCount):
    itemsNumber = []
    for i in range(itemsCount):
        itemsNumber.append(random.randint(1, 10))
    return itemsNumber


itemsCount = num_of_items(products)
itemsQuantity = products_generator(itemsCount)


def print_products(products, itemsCount):
    counter = 0
    print("{:10} {:<11} {:<10} {:<6}".format("number", "name", "price", "product quantity"))
    for item in products:
        if itemsQuantity[counter] != 0:
            print("{:<10} {:<11} {:<10} {:<6}".format(counter + 1, item, str(products[item]) + " $ ", itemsQuantity[counter]))
        else:
            print(counter + 1, ". " + "\t " + str(products[item]) + "\t   ", str(products[item]) + " $" + "\t   ",
                  "not available")
        counter += 1


def countingUserItems(shopping_cart):
    countingItems = {}

    for item in shopping_cart:
        countingItems[item] = shopping_cart.count(item)

    return countingItems


def total_price(shopping_cart):
    listOfPrices = []

    for item in shopping_cart:
        listOfPrices.append(products.get(item))

    finalPrice = sum(listOfPrices)
    return finalPrice




def print_shopping_cart(shopping_cart):
    print("shopping cart:")
    for item in shopping_cart:
        print(item + str(products[item]), "$")

    print("total price:" + str(total_price(shopping_cart)) + "$")


def read_input():
    try:
        num = int(input("Write a number of product u wish tu buy, if u want to end your shopping write 0 \n"))
        return num
    except ValueError:
        print("inser a valid number")
        return read_input()


def user_shopping(shopping_cart, products, itemsQuantity, itemsCount):
    wrong_input = 1
    print_products(products, itemsCount)
    #shopping_cart_items = countingUserItems(shopping_cart)
    #print_shopping_cart(shopping_cart_items)

    while wrong_input == 1:
        #print_shopping_cart(shopping_cart)
        #print_products(products, itemsCount)
        products_counter = 0

        while True:
            try:
                user_input = int(input("Write a number of product u wish tu buy, if u want to end your shopping write 0 \n"))
            except ValueError:
                print("inser a valid number")
                continue
            break

        if user_input == 0:
            print_shopping_cart(shopping_cart)
            print("thanks for purchase")
            break
        elif 1 <= user_input <= itemsCount:

            for item in products:
                if products_counter == user_input - 1:
                    if itemsQuantity[products_counter] != 0:
                        itemsQuantity[products_counter] -= 1
                        shopping_cart.append(item)
                        wrong_input = 0
                        break
                    else:
                        print("Product is no longer available, choose something else")
                        break
                else:
                    products_counter += 1
        else:
            print("enter a valid number")
    return shopping_cart
