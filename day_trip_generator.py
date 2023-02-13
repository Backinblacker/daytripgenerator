import random
destinations_list = ['Colorado', 'Florida', 'Arizona', 'New York City', 'Seattle']
restaurants_list =['Steak House', 'Sushi Den', 'Salad Central', 'What did I just eat?', 'Chicken Shack']
mode_of_transport = ['Car', 'Bus', 'Plane', 'Train', 'Teleporter']
entertainment_list = ['Musical', 'Haunted Town Tour', 'Fishing', 'Squirrel Wrangling', 'Scavenger Hunt Tour']

# Random generate answer

# def run_day_trip_generator():

def random_trip (list_of_options):
    output = random.choice(list_of_options)
    return (output)

destination = random_trip (destinations_list)
restaurant = random_trip (restaurants_list)
mode = random_trip (mode_of_transport)
entertain = random_trip (entertainment_list)

# day trip message
day_trip = (f'Here is your trip. You have been selected take (a/the) {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
print(day_trip)

def determine_satisfaction(day_trip, mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list):
    trip_satifaction = True
    while trip_satifaction == True:
        user_input = input(f"Is your trip satifactory, Y or N?")
        if user_input == "N":
            change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)
            mode, destination, restaurant, entertain = change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)
            day_trip = (f'Here is your trip. You have been selected take (a/the) {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
            print(day_trip)
        elif user_input == "Y":
            print(f"Congrats! Let's get your trip booked.")
            trip_satifaction = False

# Which option would they change:
def change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list):
    user_input = input("Which option would you like to change? Destination, Restaurant, Transportation, Entertainment")
    if user_input == "Destination" or "destination":
        destinations_list.remove(destination)
        destination = random_trip(destinations_list)
    if user_input == "Restaurant" or "restaurant":
        restaurants_list.remove(restaurant)
        restaurant = random_trip(restaurants_list)
    if user_input == "Transportation" or "transportation":
        mode_of_transport.remove(mode)
        mode = random_trip(mode_of_transport)
    if user_input == "Entertainment" or "entertainment":
        entertainment_list.remove(entertain)
        entertain = random_trip(entertainment_list)
    else:
        print('This is not a valid input.')
        
    return mode,destination, restaurant, entertain
# mode, destination, restaurant, entertain = change_option(mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)
# day_trip = (f'Here is your trip. You have been selected take (a/the) {mode} to {destination}, eat at {restaurant}, and go {entertain}!')
# print(day_trip)
determine_satisfaction(day_trip, mode, destination, restaurant, entertain, destinations_list, restaurants_list, mode_of_transport, entertainment_list)


# Is it the Destination?
# def bad_destination():
#     not_this_one = True
#     while not_this_one == True:
#         user_input = 
        
# def re_select_option(current_trip, options):
    
# run_day_trip_generator()