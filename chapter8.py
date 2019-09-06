def greet_user():
    print("Hello!")
print(greet_user())

def greet_user(username):
    print("Hello, " + username.title() + "!")

print(greet_user('prasanti'))

def describe_pet(animal_type, pet_name):

    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'mika')

def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()
musician = get_formatted_name('john', 'lee')
print(musician)


def build_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}

    if age :
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("(enter q at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed: ")
for model in completed_models:
    print(model)

def print_models(unfinished, completed):
    while unfinished:
        current_design = unfinished.pop()
        print("Printing model: " + current_design)
        completed.append(current_design)

def show_completed_models(completed):
    print("\nThe following models have been printed: ")
    for model in completed:
        print(model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
        
