products={
    "laptop":55000,
    "phone":50009,
    "earbuds":4999,
    "pc":125000
}

expensive_product=None
max_price=0

for product, price in products.items():
    if price>max_price:
        max_price=price
        expensive_product=product

print("most expensive product",expensive_product)
print("price:",max_price)