# 1 #/// Positional and keyword arguments ///#
def add_to_cart(item, quantity):
    print(f"Added {quantity} {item} to the cart.")

add_to_cart("Apples", "4kg")


# 2 #///Default arguments///#
def greet_user(name = "there"):
    print(f"Hello {name}! Welcome to our website.")
    
greet_user()
greet_user("Faisal")

# 3 #///Variable-Length arguments///#
def calculate_average(*args):
    total = sum(args)
    average = total / len(args)
    return average

print(calculate_average(4,8,6,2))