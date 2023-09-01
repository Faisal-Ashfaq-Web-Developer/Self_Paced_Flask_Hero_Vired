products = {
    1: {'name': 'iPhone', 'category': 'Electronics', 'price': '$1,000.00'},
    2: {'name': 'Tv', 'category': 'Electronics', 'price':'$2,000.00'},
    3: {'name': 'Book', 'category': 'Books', 'price':'$30.00'},
    4: {'name': 'Cake', 'category': 'Food', 'price':'$50.00'},
    5: {'name': 'Pizza', 'category': 'Food', 'price':'$100.00'},
}

def product_search(**kwargs):
    matching_products = []
    for product_id, attributes in products.items():
        if all(attributes.get(key) == value for key, value in kwargs.items()):
            return matching_products

results = product_search()
