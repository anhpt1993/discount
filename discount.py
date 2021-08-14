# discount price
def again(answer):
    if answer == "YES" or answer == "Y":
        return True

def discount(price):
    if price >= 150:
        print("You get an discount of 50$")
        print("Your total price is {} USD".format(price-50))
    elif price >= 100:
        print("You get an discount of 25$")
        print("Your total price is {} USD".format(price - 25))
    elif price >= 75:
        print("You get an discount of 15$")
        print("Your total price is {} USD".format(price - 15))
    else:
        print("The minimum bill is 75$ to get a discount")
        print("You have to buy more {} USD".format(75-price))
        answer = input("Do you want to buy more? (Yes/No): ").upper()
        if again(answer):
            print("See you later!!!")
            pass
        else:
            print("Your total price is {} USD".format(price))
while True:
    try:
        price = float(input("Enter you bill please: "))
        if price > 0:
            break
        else:
            print("You have to buy something first. See yaa!!")
            print()
    except ValueError:
        print("Give me an positive number. Thanks!!!")
        print()
discount(price)
