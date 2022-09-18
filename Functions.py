"""
def display_message():
    print("we'll learn Functions in this chapter!")
display_message()
"""
"""
def favourite_book(title):
    print(f"One of my favourite book is {title}")
favourite_book("Dune")
"""
"""
def make_tshirt(size):
    print(f"Tshirt's size is {size}")
make_tshirt("Large")
make_tshirt(size = "Large")
"""
"""
def make_tshirt(size,message):
    print(f"Tshirt's size is {size}")
    if size == "Large":
        print(f"{message}")
make_tshirt("Large", message= "Large Tshirt message")
make_tshirt(size = "Medium", message= "Medium Tshirt Message")
"""
"""
def describe_city(name,country = "Turkey"):
    print(f"{name} is in {country}")
describe_city("Berkay")
describe_city(name= "Berkay", country= "Turkey")
describe_city("Halil", "Germany")
"""