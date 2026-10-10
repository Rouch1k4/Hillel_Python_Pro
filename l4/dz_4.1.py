
class Shop:
    def __init__(self):
        self.products = []
        self.customers = []

    def load_product(self, filename):
        with open(filename, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                product = Product(parts[0], parts[1], int(parts[2]), int(parts[3]))
                self.products.append(product)

    def load_customer(self, filename):
        with open(filename, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                customer = Customer(parts[0], parts[1])
                self.customers.append(customer)

class Product:
    def __init__(self, name, category, price, quantity_storage) :
        self.name = name
        self.category = category
        self.price = price
        self.quantity_storage = quantity_storage

    def change_price (self, new_price) :
        self.price = new_price

    def change_quantity_storage(self, new_quantity_storage) :
        self.quantity_storage = new_quantity_storage


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.list_order = []


    def add_new_order(self, new_order) :
        self.list_order.append(new_order)


class Order:
    def __init__(self) :
        self.product = []
        self.total_price = 0

    def add_product(self, product) :
        self.product.append(product)

    def calcul_total(self):
        total = 0
        for product in self.product:
            total += product.price
        self.total_price = total


shop = Shop()
shop.load_product("products.txt")
shop.load_customer("customers.txt")

print(len(shop.products), len(shop.customers))
print(shop.products[0].name)
print(shop.customers[0].email)


order = Order()
order.add_product(shop.products[0])
order.add_product(shop.products[1])
order.calcul_total()
shop.customers[0].add_new_order(order)

print(order.total_price)
print(len(shop.customers[0].list_order))