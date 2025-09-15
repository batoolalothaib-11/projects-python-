basket = []
prices = []

print("***** Welcome to iShop calculator *****")
items = int(input("\nHow many items are there in your basket today? "))
if items > 0:    
    print("\nLet's get to couting them ....")
    for i in range (1, items + 1):
        name = input(f"\nPlease tell me the name of the item number {i} : ")
        basket.append(name)
        price = float(input(f"\nWhat is the price of {name} : \n$"))
        prices.append(price)
else:
    print("Seems like you are not in the mood for shopping today.")
    exit()
    
see_basket = input("\nWould you like to see your entire basket items? ").lower()
if see_basket == "yes":
    print(basket)

cost = input("Would you like to see how much it'll cost? ").lower()
if cost == "yes":
    print("\nBuying these items will cost:")
    print(sum(prices))
else:
    input("Press Enter to exit.")
