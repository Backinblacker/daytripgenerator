import random
destinations_list = ['Colorado', 'Florida', 'Arizona', 'New York', 'Seattle']
restaurants_list =['Steak House', 'Sushi Den', 'Salad Central', 'What did I just eat?', 'Chicken Shack']
mode_of_transport = ['Car', 'Bus', 'Plane', 'Train', 'Teleporter']
entertainment_list = ['Musical', 'Haunted Town Tour', 'Gone Fishing', 'Squirrel Wrangling', 'Scavenger Hunt Tour']

# Random generate answer

# def run_day_trip_generator():
# def print_full_trip(list_of_options):

def generate_random_dest():
    random_dest = random.choice(destinations_list)
    print('Destination: ' + random_dest)
    return random_dest
generate_random_dest()

def generate_random_rest():
    random_rest = random.choice(restaurants_list)
    print('Restaurant: ' + random_rest)
    return random_rest
generate_random_rest()

def generate_random_mode():
    random_mode = random.choice(mode_of_transport)
    print('Mode of Transportation: ' + random_mode)
    return random_mode
generate_random_mode()

def generate_random_entertain():
    random_entertain = random.choice(entertainment_list)
    print('Entertainment: ' + random_entertain)
    return random_entertain
generate_random_entertain()


# def determine_satisfaction():
#     trip_satifaction = True
#     current_trip = generate_random_item()
#     while trip_satifaction == True:
#         user_input = input(f"Is {current_trip} satifactory, Y or N?")
#         if user_input == "N":
#             print(f"Let's try this again.")
#         elif user_input == "Y":
#             print(f"Congrats! Let's get your {current_trip} booked.")
#             trip_satifaction = False
# determine_satisfaction()

# Which option would they change:
# def change_option():
#     user_input = ("Which option would you like to change? Destination, Restaurant, Transportation, Entertainment")
#     if user_input == "Destination" or "destination":
#     if user_input == "Restaurant" or "restaurant":
#     if user_input == "Transportation" or "transportation":
#     if user_input == "Entertainment" or "entertainment":
# Is it the Destination?
# def bad_destination():
#     not_this_one = True
#     while not_this_one == True:
#         user_input = 
        
# def re_select_option(current_trip, options):
    
# run_day_trip_generator()