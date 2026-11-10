class Supermarket:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.profit = 0
        
    def buy_stock(self, product, quantity):
        product.quantity += quantity
        self.profit -= product.buying_price * quantity
    
    def sell_product(self, product, quantity):
        if product.quantity >= quantity and quantity > 0:
            product.quantity -= quantity
            self.profit += product.selling_price * quantity

    def check_profit(self):
        return self.profit
        
class Department:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
        
    def remove_product(self, product):
        self.products.remove(product)
    

    
class Product:
    def __init__(self, name, buying_price, selling_price, quantity):
        self.name = name
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.quantity = quantity
        
    
    def __str__(self):
        return f"{self.name}: £{self.selling_price}"

        
class Supplier:
    def __init__(self, name):
        self.name = name

    def supply_product(self, supermarket, product, quantity):
        supermarket.buy_stock(product, quantity)
    
    
frozen = Department("Frozen Foods")
fresh = Department("Fresh Fruit and Vegetables")
tinned = Department("Tinned Goods")
pharmacy = Department("Pharmaceuticals")

tesco = Supermarket("Tesco")

tesco.departments.append(frozen)
tesco.departments.append(fresh)
tesco.departments.append(tinned)
tesco.departments.append(pharmacy)


supplier1 = Supplier("Fresh Foods Ltd")

apple = Product("Orange", 1, 2, 0)

fresh.add_product(apple)

supplier1.supply_product(tesco, apple, 10)

print("Stock:", apple.quantity)
print("Profit:", tesco.check_profit())

tesco.sell_product(apple, 4)

print("Stock after selling:", apple.quantity)
print("Profit after selling:", tesco.check_profit())