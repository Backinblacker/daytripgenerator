import random
destinations_list = ['Colorado', 'Florida', 'Arizona', 'New York City', 'Seattle']
restaurants_list =['Steak House', 'Sushi Den', 'Salad Central', 'What did I just eat?', 'Chicken Shack']
mode_of_transport = ['Car', 'Bus', 'Plane', 'Train', 'Teleporter']
entertainment_list = ['Musical', 'Haunted Town Tour', 'Fishing Tour', 'Squirrel Wrangling', 'Scavenger Hunt Tour']

# Random generate answer

def random_trip (list_of_options):
    output = random.choice(list_of_options)
    return (output)

def starting_choices (trip_elements):
    trip_elements[0] = random_trip (destinations_list)
    print("Destination:  ", trip_elements[0])
    trip_elements[1] = random_trip (restaurants_list)
    print("Restaurant:  ", trip_elements[1])
    trip_elements[2] = random_trip (mode_of_transport)
    print("Mode of Transport:  ", trip_elements[2])
    trip_elements[3] = random_trip (entertainment_list)
    print("Entertainment:  ", trip_elements[3])
    return trip_elements

# day trip message
# day_trip = (f'Here is your trip. You have been selected take a {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
# print(day_trip)

# does the trip that spit out meet the user's expectations?
def determine_satisfaction():
    trip_satifaction = True
    trip_elements = ['', '', '', '']
    starting_choices(trip_elements)
    while trip_satifaction == True:
        user_input = input(f"Is your trip satifactory, Y or N? ")
        if user_input == "N" or user_input == "n":
            day_trip = change_option(trip_elements)
            #print(day_trip)
        elif user_input == "Y" or user_input == "y":
            print(f"Congrats! Now let's get your trip booked.")
            trip_satifaction = False

# Which option would they change?:
def change_option(trip_elements):
    user_input = input("Which option would you like to change? Destination, Restaurant, Transportation, Entertainment: ")
    if user_input == "Destination" or user_input == "destination":
        destinations_list.remove(trip_elements[0])
        trip_elements[0] = random_trip(destinations_list)
    elif user_input == "Restaurant" or user_input == "restaurant":
        restaurants_list.remove(trip_elements[1])
        trip_elements[1] = random_trip(restaurants_list)
    elif user_input == "Transportation" or user_input == "transportation":
        mode_of_transport.remove(trip_elements[2])
        trip_elements[2] = random_trip(mode_of_transport)
    elif user_input == "Entertainment" or user_input == "entertainment":
        entertainment_list.remove(entertainment_list[3])
        trip_elements[3] = random_trip(entertainment_list)
    else:
        print('This is not a valid input.')
    
    print("Destination:  ", trip_elements[0])
    print("Restaurant:  ", trip_elements[1])
    print("Mode of Transport:  ", trip_elements[2])
    print("Entertainment:  ", trip_elements[3])
    return trip_elements

determine_satisfaction()
