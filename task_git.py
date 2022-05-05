dict_of_products = {"piekarnia": ["chleb", "bułki", "paczki"], "warzywniak": ["marchew", "seler", "rukola"]}
y = 0
for shop, products in dict_of_products.items():
    print(f"W sklepie {shop.capitalize()} i kupuję tam: {[i.capitalize() for i in products]}")