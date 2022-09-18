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
"""
