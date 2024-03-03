class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, shares):
        self.shares -= shares

    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'


class MyStock(Stock):
    def __int__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        return self.sell(self.shares)

    def cost(self):
        # return 1.25*self.shares*self.price
        return super().cost() * self.factor
