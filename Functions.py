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
"""
def get_formatted_name(firstname,lastname):
    fullname = f"{firstname} {lastname}"
    return fullname.title()

musician = get_formatted_name('jimmy','hendrix')
print(musician)
"""
"""
def build_person(first_name, last_name, age=None):
    #Return a dictionary of information about a person.
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
"""
"""
def get_formatted_name(firstname,lastname):
    fullname = f"{firstname} {lastname}"
    return fullname.title()
"""
"""
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == "q":
        break
    l_name = input("Last Name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}")
"""    
"""
def city_country(city_name,country_name):
    fullname = f"{country_name}, {city_name}"
    print(fullname)
city_country("istanbul", "TR")
"""
"""
def make_album(artist_name, album_title):
    album = {"artist_name":artist_name,"album_title":album_title}
    return f"{album['album_title']} made by {album['artist_name']}"
artist_song = make_album("haluk","song")
print(artist_song)
"""
"""
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
usernames = ['berkay','oguzhan','ilayda']
greet_users(usernames)
"""
"""
unprinted_design = ['design-1','design-2','design-3']
completed_models = []

while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
"""
"""
def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_design = ['design-1','design-2','design-3']
completed_models = []
print_models(unprinted_design, completed_models)
show_completed_models(completed_models)
"""
"""
full = ["hello","hi","bye"]
empty = [] 
def show_messages(msgs):
    while full:
        current = full.pop()
        empty.append(current)
print(full)
print(empty)

show_messages(full)
print(full)
print(empty)
"""

"""
def make_pizza(*toppings):
    print(toppings)
#make_pizza("mushrooms")
make_pizza("mushrooms","cheese","pepperoni")
"""
"""
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)
make_pizza("mushrooms","cheese","pepperoni")
"""
"""
def make_pizza(size,*args):
    print(f"{size}-inch pizza will be ready with followings: ")
    for topping in args:
        print(topping)
make_pizza("12","mushrooms","cheese","pepperoni")
"""
"""
def build_profie(first,last,**user_info):
    user_info["first_name"] = first
    user_info["last_name"]  = last
    return user_info
abc = build_profie("albert","einstein", location = "princeton", field = "physics")
print(abc)
"""
"""
#8-12 Sandwiches
def make_sandwiches(*toppings):
    print(f"sandwich will be ready with followings:")
    for i in toppings:
        print(f"-{i}")
make_sandwiches("chicken")
make_sandwiches("chicken","meat")
"""
"""
#8-13 User Profile
def build_profile(first,last,**user_info):
    user_info["firstname"] = first
    user_info["lastname"]  = last
    return user_info
ID = build_profile("berkay","akar", location = "istanbul", age = "\t26")
for key,value in ID.items():
    print(f"{key}\t{value}")
"""
"""
#8-14 Cars
def make_car(manufacturer,model,**car_info):
    car_info["manufacturername"] = manufacturer
    car_info["modelname"]        = model
    return car_info
car = make_car("honda","civic",color = "red", package = "excellent")
print(car)
"""

