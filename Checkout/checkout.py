class Checkout:
    class Discount:
        def __init__(self, nbrOfItems, price):
            self.nbrOfItems = nbrOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            total += self.calculateItemDiscountedTotal(item, cnt, discount)
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        if cnt >= discount.nbrOfItems:
            nbrOfDiscounts = cnt//discount.nbrOfItems
            total += nbrOfDiscounts * discount.price
            remaining = cnt % discount.nbrOfItems
            total += remaining * self.prices[item]
        else:
            total += self.prices[item] * cnt
        return total

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount
