import random
destinations_list = ['Colorado', 'Florida', 'Arizona', 'New York City', 'Seattle']
restaurants_list =['Steak House', 'Sushi Den', 'Salad Central', 'What did I just eat?', 'Chicken Shack']
mode_of_transport = ['Car', 'Bus', 'Plane', 'Train', 'Teleporter']
entertainment_list = ['Musical', 'Haunted Town Tour', 'Fishing', 'Squirrel Wrangling', 'Scavenger Hunt Tour']

# Random generate answer

def random_trip (list_of_options):
    output = random.choice(list_of_options)
    return (output)

destination = random_trip (destinations_list)
restaurant = random_trip (restaurants_list)
mode = random_trip (mode_of_transport)
entertain = random_trip (entertainment_list)

# day trip message
day_trip = (f'Here is your trip. You have been selected take a {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
print(day_trip)

# does the trip that spit out meet the user's expectations?
def determine_satisfaction(day_trip, mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list):
    trip_satifaction = True
    while trip_satifaction == True:
        user_input = input(f"Is your trip satifactory, Y or N?")
        if user_input == "N":
            mode, destination, restaurant, entertain = change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)
            day_trip = (f'Here is your trip. You have been selected take a {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
            print(day_trip)
        elif user_input == "Y":
            print(f"Congrats! Let's get your trip booked.")
            trip_satifaction = False

# Which option would they change?:
def change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list):
    user_input = input("Which option would you like to change? Destination, Restaurant, Transportation, Entertainment: ")
    print(destination)
    print(destinations_list)
    if user_input == "Destination" or user_input == "destination":
        destinations_list.remove(destination)
        destination = random_trip(destinations_list)
    elif user_input == "Restaurant" or user_input == "restaurant":
        restaurants_list.remove(restaurant)
        restaurant = random_trip(restaurants_list)
    elif user_input == "Transportation" or user_input == "transportation":
        mode_of_transport.remove(mode)
        mode = random_trip(mode_of_transport)
    elif user_input == "Entertainment" or user_input == "entertainment":
        entertainment_list.remove(entertain)
        entertain = random_trip(entertainment_list)
    else:
        print('This is not a valid input.')
        
    return mode,destination, restaurant, entertain

determine_satisfaction(day_trip, mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)
