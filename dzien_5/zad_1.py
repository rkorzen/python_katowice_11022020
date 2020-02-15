class Product:

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
        self.lang = "pl"

    def __str__(self):
        return "<Product: ({}) {}: {}>".format(
            self.id,
            self.name,
            self.price
        )


    def print_info(self):
        if self.lang == "pl":
            print(f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price}")
        elif self.lang == "en":
            print(f"Product \"{self.name}\", id: {self.id}, price: {self.price}")

product = Product(1, "Woda", 10.99)
product.lang = "en"
assert product.id == 1
product.print_info()

