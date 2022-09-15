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
