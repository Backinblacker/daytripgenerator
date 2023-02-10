import random
destinations_list = ['Colorado', 'Florida', 'Arizona', 'New York', 'Seattle']
restaurants_list =['Steak House', 'Sushi Den', 'Salad Central', 'What did I just eat?', 'Chicken Shack']
mode_of_transport = ['Car', 'Bus', 'Plane', 'Train', 'Teleporter']
entertainment_list = ['Musical', 'Haunted Town Tour', 'Gone Fishing', 'Squirrel Wrangling', 'Scavenger Hunt Tour']

# Random generate answer

# def run_day_trip_generator():
# def print_full_trip(list_of_options):
#def generate_random_item(list_of_items):
def generate_random_item():
    random_dest = random.choice(destinations_list)
    print(random_dest)

    random_rest = random.choice(restaurants_list)
    print(random_rest)

    random_mode = random.choice(mode_of_transport)
    print(random_mode)

    random_entertain = random.choice(entertainment_list)
    print(random_entertain)
    return
generate_random_item()
# def degermins_satisfaction(current_trip, trip_options):
# def re_select_option(current_trip, options):
    
# run_day_trip_generator()