

# Day Trip Generator! by Harrison Latta

import random
from tkinter.messagebox import YES

destinations = ['Corpus Christi', 'Houston', 'San Antonio', 'El Paso', 'Dallas']
restaurants = ['McDonalds', 'Olive Garden', 'Texas Roadhouse', 'Chilis', 'Burger King']
transportation_methods = ['walking', 'taking an Uber', 'driving']
entertainments = ['going to the movie theater', 'sightseeing', 'exploring a museum', 'going for a swim']


final_list = []

def places_to_go(cities):
    place = random.choice(cities)
    return place

def welcome_message():
    first_name = input('Hey there, please enter your first name. ')
    last_name = input('Now please enter your last name. ')
    full_name = first_name + ' ' + last_name
    final_list.append(full_name)
    print(f"Hello {full_name}, let's get started on your random day trip!")

def dest_picker():
    random_dest_result = places_to_go(destinations)
    city_select = input(f'For the destination, how does {random_dest_result} sound? (Yes or No) ')
    while city_select != 'Yes':
            random_dest_result = places_to_go(destinations)
            city_select = input(f'Okay then, how does {random_dest_result} sound? (Yes or No) ')
    if city_select == 'Yes':
        final_list.append(random_dest_result)
        print('Okay, on to the next step.')

def restaurant_picker():
    random_rest_result = places_to_go(restaurants)
    food_select = input(f'As far as eating goes, how does {random_rest_result} sound? (Yes or No) ')
    while food_select != 'Yes':
            random_rest_result = places_to_go(restaurants)
            food_select = input(f'Okay then, how does {random_rest_result} sound? (Yes or No) ')
    if food_select == 'Yes':
        final_list.append(random_rest_result)
        print('Okay, on to the next step.')

def transport_picker():
    random_transport_result = places_to_go(transportation_methods)
    ride_select = input(f'For getting around, how does {random_transport_result} sound? (Yes or No) ')
    while ride_select != 'Yes':
            random_transport_result = places_to_go(transportation_methods)
            ride_select = input(f'Okay then, how does {random_transport_result} sound? (Yes or No) ')
    if ride_select == 'Yes':
        final_list.append(random_transport_result)
        print('Okay, on to the next step.')

def entertain_picker():
    random_entertain_result = places_to_go(entertainments)
    ent_select = input(f'Now for fun, how does {random_entertain_result} sound? (Yes or No) ')
    while ent_select != 'Yes':
            random_entertain_result = places_to_go(entertainments)
            ent_select = input(f'Okay then, how does {random_entertain_result} sound? (Yes or No) ')
    if ent_select == 'Yes':
        final_list.append(random_entertain_result)
        print("Okay, looks like we're all done!")

def confirmation():
    last_call = input('Are you satisfied with your selections? (Yes or No)')
    while last_call != 'Yes' or 'yes':
        final_list.pop()
        final_list.pop()
        final_list.pop()
        final_list.pop()
        dest_picker()
        restaurant_picker()
        transport_picker()
        entertain_picker()
        if last_call == 'Yes' or 'yes':
            break


def wrap_up():
    print(f"Okay {final_list[0]}, you're going to {final_list[1]}.")
    print(f"You'll be going to eat at {final_list[2]} and you'll be {final_list[3]} to get around!")
    print(f"As far as entertainment goes, you'll be {final_list[4]}!")
    print('Have fun and enjoy your trip! :)')





welcome_message()
dest_picker()
restaurant_picker()
transport_picker()
entertain_picker()
confirmation()
wrap_up()