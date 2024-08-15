from os import system
system("cls")

def bigger_price(n, product_list):
    
    sorted_products = sorted(product_list, key=lambda x: x['price'], reverse=True)
    
    
    return sorted_products[:n]


products = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]


result = bigger_price(2, products)
print(result)
