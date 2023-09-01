def calculate_area(length, width):
    area = length*width
    print(f"Area of rectangle: {area}")

calculate_area(12,4)
#print(area)--- NameError: name 'area' is not defined

def calculate_total(prices):
    total = sum(prices)
    print(f"Total price of items: {total}")

item_prices = [45,12,56]
calculate_total(item_prices)
##print(total)--- NameError: name 'area' is not defined


##--Returning Multiple values from a function
def calculate_rectangle(length, width):
    area = length*width
    perimeter = 2*length+ 2*width
    return area, perimeter
rectangle_area, rectangle_perimeter = calculate_rectangle(12,6)
print(f"Area of rectangle: {rectangle_area}")
print(f"Perimeter of rectangle: {rectangle_perimeter}")


def calculate_power(number):
    square = number**2
    cube = number**3
    return square, cube
Square, Cube = calculate_power(3)
print(f"Square of number: {Square}")
print(f"Cube of number: {Cube}")

def get_user_info(user_ID):
    name = "Faisal"
    email = "faisal@gmail.com"
    age = 30
    return name, email, age

user_name, user_email, user_age = get_user_info(1234)

print(f"User name: {user_name}")
print(f"User email: {user_email}")
print(f"User age: {user_age}")
