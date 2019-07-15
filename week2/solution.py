
class Item:
    def __init__(self, count, measure, name, price):
        self.quantity = count
        self.measure = measure
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.quantity:5} {self.measure:<6}{self.name:<10} @ ${self.price:.1f}...${self.quantity * self.price:.1f}"

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __format__(self, f):
        if len(self.items) == 0:
            return ''

        sorted_items = sorted([i for i in self.items], key=lambda x: x.name)
        if f == "short":
            return ', '.join([i.name for i in sorted_items])

        if f == "long":
            s = "\n\t".join([str(i) for i in sorted_items])
            return f"\t{s}"

        return f"unknown format code {f}"