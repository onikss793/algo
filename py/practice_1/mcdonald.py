import sys


def get_cheapest_price(num):
    cheapest_price = 10000

    for n in range(num):
        price = int(sys.stdin.readline().rstrip())

        if price < cheapest_price:
            cheapest_price = price

    return cheapest_price


def discount(price):
    standard = 50

    return price - standard


def main():
    burger = get_cheapest_price(3)
    drink = get_cheapest_price(2)

    result = discount(burger + drink)

    print(result)


main()

# 800
# 700
# 900
# 198
# 330