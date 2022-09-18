"""
user_0 = {
    'username' : 'berkay', 
    'lastname' : 'akar'
    }

for key,value in user_0.items():
    print(f"Key : {key}")
    print(f"Value : {value}")
"""

"""
fav_language = {
    'jen'   : 'python'  , 
    'sarah' : 'c'       ,
    'edward': 'ruby'    ,
    'phill' : 'python' 
    }
for name,language in fav_language.items() :
    print(f"{name.title()}'s favourite language is {language.title()}.")
"""

"""
fav_language = {
    'jen'   : 'python'  , 
    'sarah' : 'c'       ,
    'edward': 'ruby'    ,
    'phill' : 'python' 
    }
for name in fav_language.keys() :
    print(f"{name.title()} is in the list.")

for language in fav_language.values() :
    print(f"{language.title()} is one of the favourite language in the list.")
"""

"""
fav_language = {
    'jen'   : 'python'  , 
    'sarah' : 'c'       ,
    'edward': 'ruby'    ,
    'phill' : 'python' 
    }
friends = ['phill','sarah']
for name in fav_language.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = fav_language[name]
        print(f"\t{name.title()}, I see you love {language.title()}.")
"""
"""
fav_language = {
    'jen'   : 'python'  , 
    'sarah' : 'c'       ,
    'edward': 'ruby'    ,
    'phill' : 'python' 
    }
for name in sorted(fav_language.keys()): 
    #alfabetik olarak sıralanır
    print(f"{name}")
"""
"""
fav_language = {
    'jen'   : 'python'  , 
    'sarah' : 'c'       ,
    'edward': 'ruby'    ,
    'phill' : 'python' 
    }
for language in set(fav_language.values()):
    #tekrarlayanlar silinir
    print(f"{language}")
"""
"""
cars_and_speeds = {
    'honda'    :    '80'    ,
    'toyota'   :    '90'    ,
    'mercedes' :    '100'   ,
    'ferrari'  :    '110'
}
for car,speed in cars_and_speeds.items():
    print(f"{car} has {speed}")

for car_name in cars_and_speeds.keys():
    print(f"{car_name}")

for speed_value in cars_and_speeds.values():
    print(f"{speed_value}")

"""
"""
#Nesting --> iç içe geçirme; dictionaryleri bir liste olarak toplama

alien_0 = {'color':'green'  ,'points':'5'}
alien_1 = {'color':'yellow' ,'points':'10'}
alien_2 = {'color':'red'    ,'points':'15'}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
"""
"""
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:5]:
    print(alien)
print(f"Total numer of aliens : {len(aliens)}")
"""
"""
#List in a dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
"""
"""
favourite_languages = {
    'jen' : ['python','ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby','go'],
    'phil' : ['python','haskell']
}

for name,languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
"""
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last'  : 'einstein',
        'location' : 'princeton'
    },
    'mcurie' : {
        'first' : 'marie',
        'last'  : 'curie',
        'location' : 'paris'
    }
}
for username,user_info in users.items():
    print(f"\nUsername : {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull name : {fullname.title()}")
    print(f"\tLocation : {location.title()}")
"""

"""
responses = {}

#set a flag to indicate that polling is active
polling_active = True


while polling_active :
    #prompt for te person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would like to climb ? ")
    #store the response in dictionary
    responses[name] = response
    #Find out if anyone else is going to take the poll
    repeat = input("Would like to let another person respond? (yes/no) ")
    if repeat == "no" :
        polling_active = False
print("\n--Poll Results--")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")
print(responses)
"""
"""
sandwich_orders = ["vegan","chicken","meat"]
finished_sandwiches = []
i = 0
while i < len(sandwich_orders):
    print(f"I made your {sandwich_orders[i].title()} sandwich")
    finished_sandwiches.append(sandwich_orders[i])
    i += 1
print("\tAll Sandwiches have been made")
"""
"""
sandwich_orders = ["vegan", "pastrami", "chicken","pastrami","meat","pastrami"]
finished_sandwiches = []
if "pastrami" in sandwich_orders:
    print("deli has run out of pastrami")
    p = 0
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
        p += 1
    print(f"{p} pastrami sandwiches have been removed due to deli run out of pastrami")
i = 0
while i < len(sandwich_orders):
    print(f"I made your {sandwich_orders[i].title()} sandwich")
    finished_sandwiches.append(sandwich_orders[i])
    i += 1
print("\tAll Sandwiches have been made")
"""

flag = True
visitor_list = {}
while flag:
    name  = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    visitor_list[name] = place
    repeat = input("is there anyone else? (yes/no)")
    if repeat == "no":
        flag = False
print("\n--Thank you for your participating--")
for name, place in visitor_list.items() :  
    print(f"{name} would like to visit {place}")
