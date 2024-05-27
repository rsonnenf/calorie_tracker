import zmq, json

goals = {1: "Lose Weight",
         2: "Gain Weight",
         3: "Maintain Weight"
         }

activity_levels = {1: "sedentary",
                   2: "lightly active",
                   3: "moderately active",
                   4: "active",
                   5: "very active"
                   }



foods = {
    1: {
        "category": "fruits",
        "items": {
            "apple": {"serving_size": "1 medium", "calories": 95},
            "avocado": {"serving_size": "1/5 medium", "calories": 50},
            "banana": {"serving_size": "1 medium", "calories": 105},
            "cherries": {"serving_size": "1 cup", "calories": 97},
            "grapefruit": {"serving_size": "1/2 fruit", "calories": 52},
            "kiwi": {"serving_size": "1 medium", "calories": 42},
            "mango": {"serving_size": "1 cup, pieces", "calories": 99},
            "peach": {"serving_size": "1 medium", "calories": 59},
            "pineapple": {"serving_size": "1 cup, chunks", "calories": 82},
            "strawberries": {"serving_size": "1 cup, halves", "calories": 49}
        }
    },
    2: {
        "category": "vegetables",
        "items": {
            "bell peppers": {"serving_size": "1 cup, sliced", "calories": 18},
            "broccoli": {"serving_size": "1 cup, chopped", "calories": 31},
            "carrots": {"serving_size": "1 cup, chopped", "calories": 52},
            "cauliflower": {"serving_size": "1 cup", "calories": 25},
            "celery": {"serving_size": "1 cup, diced", "calories": 14},
            "green beans": {"serving_size": "1 cup", "calories": 34},
            "lettuce": {"serving_size": "1 cup, shredded", "calories": 5},
            "onions": {"serving_size": "1 cup, chopped", "calories": 64},
            "spinach": {"serving_size": "1 cup", "calories": 7},
            "tomatoes": {"serving_size": "1 cup, chopped or sliced", "calories": 32}
        }
    },
    3: {
        "category": "grains",
        "items": {
            "barley": {"serving_size": "1 cup, cooked", "calories": 193},
            "bread": {"serving_size": "1 slice", "calories": 79},
            "buckwheat": {"serving_size": "1 cup, cooked", "calories": 155},
            "corn": {"serving_size": "1 cup", "calories": 132},
            "millet": {"serving_size": "1 cup, cooked", "calories": 207},
            "oatmeal": {"serving_size": "1 cup, cooked", "calories": 158},
            "pasta": {"serving_size": "1 cup, cooked", "calories": 221},
            "quinoa": {"serving_size": "1 cup, cooked", "calories": 222},
            "rice": {"serving_size": "1 cup, cooked", "calories": 206},
            "rye": {"serving_size": "1 slice", "calories": 83}
        }
    },
    4: {
        "category": "protein",
        "items": {
            "almonds": {"serving_size": "1 oz", "calories": 164},
            "black beans": {"serving_size": "1 cup, cooked", "calories": 227},
            "chicken breast": {"serving_size": "3 oz", "calories": 140},
            "chicken thigh": {"serving_size": "3 oz", "calories": 209},
            "eggs": {"serving_size": "1 large", "calories": 72},
            "lentils": {"serving_size": "1 cup, cooked", "calories": 230},
            "pork chop": {"serving_size": "3 oz", "calories": 197},
            "salmon": {"serving_size": "3 oz", "calories": 177},
            "tofu": {"serving_size": "1/2 cup", "calories": 94},
            "turkey": {"serving_size": "3 oz", "calories": 125}
        }
    }
}

# Data compiled from "Metabolic Equivalents for Weight Loss: What Are They & How to Calculate Them",
# https://blog.nasm.org/metabolic-equivalents-for-weight-loss#:~:text=To%20determine%20calories%20expended%20by,%2F%20200%20%3D%20KCAL%2FMIN.&text=So%20in%2045%20minutes%2C%20this,NEAT%20or%20non%2Dactivity%20thermogenesis.

exercise_data = {
    1: {
        "type": "Bicycling",
        "effort": {
            "light": {
                "description": "<10 mph, leisure, for pleasure",
                "METS": 4.0
            },
            "moderate": {
                "description": "10-11.9 mph, light effort",
                "METS": 8.0
            },
            "vigorous": {
                "description": "12-13.9 mph, moderate effort",
                "METS": 10.0
            },
            "very vigorous": {
                "description": "14-15.9 mph, racing or vigorous effort",
                "METS": 12.0
            }
        }
    },
    2: {
        "type": "Conditioning exercise",
        "effort": {
            "light": {
                "description": "calisthenics, home exercise, light or moderate effort, general (example: back "
                               "exercises), going up & down from the floor",
                "METS": 3.5
            },
            "moderate": {
                "description": "water aerobics, water calisthenics",
                "METS": 4.0
            },
            "vigorous": {
                "description": "calisthenics (e.g., pushups, situps, pullups, jumping jacks), heavy, vigorous effort",
                "METS": 8.0
            },
            "very vigorous": {
                "description": "circuit training, including some aerobic movement with minimal rest, general",
                "METS": 8.0
            },
            "Heavy": {
                "description": "weight lifting, powerlifting or bodybuilding, vigorous effort",
                "METS": 6.0
            },
            "Stretching": {
                "description": "stretching, yoga",
                "METS": 2.5
            }
        }
    },
    3: {
        "type": "Home activities",
        "effort": {
            "light": {
                "description": "cleaning, light (dusting, straightening up, changing linen, carrying out the trash)",
                "METS": 2.5
            }
        }
    },
    4: {
        "type": "Walking",
        "effort": {
            "light": {
                "description": "<2.0 mph (strolling, very slow)",
                "METS": 2.0
            },
            "moderate": {
                "description": "3.5 mph (briskly & carrying objects less than 25 lbs)",
                "METS": 4.5
            }
        }
    },
    5: {
        "type": "Swimming",
        "effort": {
            "moderate": {
                "description": "Swimming laps (freestyle, slow, moderate, or light effort)",
                "METS": 7.0
            }
        }
    },
    6: {
        "type": "Running",
        "effort": {
            "moderate": {
                "description": "5 mph (12 min/mile)",
                "METS": 8.0
            },
            "vigorous": {
                "description": "7 mph (8.5 min/mile)",
                "METS": 11.5
            },
            "very vigorous": {
                "description": "10 mph (6 min/mile)",
                "METS": 16.0
            }
        }
    },
    7: {
        "type": "Sports",
        "effort": {
            "moderate": {
                "description": "Basketball, non-game, general",
                "METS": 6.0
            },
            "vigorous": {
                "description": "Boxing, in the ring, general",
                "METS": 12.0
            },
            "very vigorous": {
                "description": "Football, touch, flag, general",
                "METS": 8.0
            },
        }
    }
}


def clear():
    print("\n" * 50)


def obtain_fitness_goal(user_data):
    """Prompts user to provide fitness goal, confirms choice, and stores goal."""
    while True:
        # Obtain user's goal selection.
        try:
            goal_selection = int(input("\n"
                                       "First, what is your fitness goal?\n"
                                       "\n"
                                       "1. I want to lose weight.\n"
                                       "2. I want to gain weight.\n"
                                       "3. I want to maintain my weight.\n"
                                       "\n"
                                       "Type 1, 2, or 3 to enter your fitness goal. "))
            if goal_selection in range(1, 4):
                while True:
                    print(f"\n"
                          f"You chose {goals[goal_selection]} as your fitness goal.")
                    goal_confirmation = int(input("To confirm this goal, press 1.\n"
                                                  "To choose a different plan, press 2. "))
                    if goal_confirmation == 1:
                        clear()
                        print(f'You have confirmed {goals[goal_selection]} as your goal! \n')
                        user_data["user_goal"] = goals[goal_selection]
                        return user_data
                    elif goal_confirmation == 2:
                        clear()
                        break
                    else:
                        print("Sorry, that's not a valid input! Let's try again.")
            else:
                print("Sorry, that is not a valid input.")
        except ValueError:
            print("You must enter a number 1, 2, or 3.")

        # Obtain confirmation of chosen goal.


def obtain_age(user_info):
    """Obtains user's age."""
    clear()
    while True:
        try:
            age = int(input("What is your age? "))
            if age > 0:
                user_info["user_age"] = age
                return user_info
            else:
                print("Age must be greater than 0.")
        except ValueError:
            print("You must enter a number for your age.")


def obtain_gender(user_info):
    """Obtains user's gender."""
    clear()
    while True:
        gender = input("What is your gender? Enter m or f. ").lower()
        if gender == "m" or gender == "male":
            user_info["user_gender"] = "m"
            return user_info
        elif gender == "f" or gender == "female":
            user_info["user_gender"] = "f"
            return user_info
        else:
            print("Sorry, we could not register your input. Please try "
                  "again.")


def obtain_height(user_info):
    """Obtains user's height"""
    clear()
    while True:
        print("For your height, first enter how many feet tall you "
              "are. Then, enter how many additional inches taller "
              "you are. Your selection will be converted to centimeters."
              "\n")
        try:
            height_in_feet = int(input("What is your height in "
                                       "feet only? "))
            height_in_inches = int(input("How many additional "
                                         "inches taller are you? "))
            height_in_cm = round((height_in_feet * 30.48) + (
                    height_in_inches * 2.54))
            if height_in_cm > 0:
                user_info["user_height"] = height_in_cm
                return user_info
            else:
                print("Height must be greater than 0.")
        except ValueError:
            print("That is not a valid height.")


def obtain_weight(user_info):
    """Obtain user's weight."""
    clear()
    while True:
        try:
            weight = int(input("What is your weight in pounds? Your input will be converted to kilograms. "))
            weight_in_kg = round(weight * .45359237)
            if weight > 0:
                user_info["user_weight"] = weight_in_kg
                return user_info
            else:
                print("Your weight must be greater than 0.")
        except ValueError:
            print("That is not a valid weight.")


def obtain_activity_level(user_info):
    """Obtains user's activity level."""
    clear()
    while True:
        try:
            activity_level = int(input("\n"
                                       "Now, let's enter your activity level. How active would you say you "
                                       "are based upon the following? \n"
                                       "1. Sedentary (little to no exercise)\n"
                                       "2. Lightly active (1-3 days of exercise per week)\n"
                                       "3. Moderately active (3-5 days of exercise per week)\n"
                                       "4. Active (6-7 days of exercise per week)\n"
                                       "5. Very Active (6-7 days of strenuous exercise per week)\n"
                                       "\n"
                                       "Enter the corresponding number here: "))
            if activity_level not in range(1, 6):
                print("We could not register your input. Please try again.")
            else:
                user_info["user_activity_level"] = activity_levels[activity_level]
                return user_info
        except ValueError:
            print("That is not a valid input. Please enter a number 1-5.")


def confirm_personal_info(user_info):
    """Confirms entries by user for personal information."""
    clear()
    while True:
        data_confirmation = int(input(f'You chose the following selections: \n'
                                      f'Age: {user_info["user_age"]} \n'
                                      f'Gender: {user_info["user_gender"]} \n'
                                      f'Height: {user_info["user_height"]} cm \n'
                                      f'Weight: {user_info["user_weight"]} kg\n'
                                      f'Activity Level: {user_info["user_activity_level"]} \n'
                                      f'\n'
                                      f'Would you like to confirm these selections? \n'
                                      f'Press 1 if you would like to confirm these selections. Press 2 to start '
                                      f'over. '))
        if data_confirmation == 1 or data_confirmation == 2:
            return data_confirmation
        else:
            print("That is not a valid input."
                  "\n")


def obtain_personal_info(user_info):
    """Obtains personal data from user, if they choose to do so, to make
    personalized goal recommendations."""
    while True:
        print("Please enter the following information.")
        obtain_age(user_info)
        obtain_gender(user_info)
        obtain_height(user_info)
        obtain_weight(user_info)
        obtain_activity_level(user_info)
        confirmation = confirm_personal_info(user_info)
        if confirmation == 1:
            return user_info
        elif confirmation == 2:
            user_info = {}


def calculate_bmr(user_info):
    """Uses Harris-Benedict formula to determine basal metabolic rate, i.e, how many calories are burned by normal daily
    activity."""
    bmr = 0
    if user_info["user_gender"] == "f":
        bmr = 655.1 + (9.563 * user_info["user_weight"]) + (1.850 * user_info["user_height"]) - \
              (4.676 * user_info["user_age"])
    elif user_info["user_gender"] == "m":
        bmr = 66.47 + (13.75 * user_info["user_weight"]) + (5.003 * user_info["user_height"]) - \
              (6.755 * user_info["user_age"])
    return bmr


def calculate_amr(user_info, user_bmr):
    """Calculates user's active metabolic rate, which adjusts a user's BMR based upon how active they are."""
    amr = 0
    if user_info["user_activity_level"] == "sedentary":
        amr = user_bmr * 1.2
    elif user_info["user_activity_level"] == "lightly active":
        amr = user_bmr * 1.375
    elif user_info["user_activity_level"] == "moderately active":
        amr = user_bmr * 1.55
    elif user_info["user_activity_level"] == "active":
        amr = user_bmr * 1.725
    elif user_info["user_activity_level"] == "very active":
        amr = user_bmr * 1.9
    return round(amr)


def update_calories(user_amr, calories_consumed, num_servings, calories_exerted):
    """Calculates number of calories left in plan."""
    remaining_calories = user_amr + calories_exerted - (calories_consumed * num_servings)
    user_amr = remaining_calories
    return user_amr


def log_food(user_amr, food_log):
    """Logs a food a user has eaten."""
    clear()
    while True:
        print("What type of food would you like to log?")
        for category_number in foods:
            print(f'{category_number}. {foods[category_number]["category"]}')
        print("5. Go back")
        try:
            food_group_choice = int(input("Enter the number corresponding with your selection here. "))
            if food_group_choice not in range(1, 6):
                print("Sorry, that is not a valid input. Let's try again.")
            elif food_group_choice == 5:
                clear()
                break
            else:
                clear()
                print(
                    f'You picked {foods[food_group_choice]["category"]}. Below are various foods and their serving sizes.'
                    f' What food would you like to log?')
                while True:
                    for item in foods[food_group_choice]["items"]:
                        print(f'{item} | {foods[food_group_choice]["items"][item]["serving_size"]}')
                    print("\n")
                    item_choice = input("Type your selection here. ").lower()
                    while True:
                        try:
                            num_servings = int(input("How many servings of this food did you have? "))
                            if num_servings > 0:
                                break
                            else:
                                print("Your serving size cannot be negative.")
                        except ValueError:
                            print("You must enter a number.")
                    if item_choice in foods[food_group_choice]["items"]:
                        new_user_amr = update_calories(user_amr,
                                                       foods[food_group_choice]["items"][item_choice]["calories"],
                                                       num_servings, 0)
                        user_amr = new_user_amr
                        # Enter food in and calories consumed in food log.
                        food_key = str(foods[food_group_choice]["items"][item_choice])
                        total_calories_consumed = foods[food_group_choice]["items"][item_choice]["calories"] * num_servings
                        food_log.append({"food_name": item_choice, "calories_consumed": total_calories_consumed})
                        return user_amr
                    else:
                        print("We did not locate that food. Please check your food choice and spelling.")
        except ValueError:
            print("Sorry, that is not a valid input. Let's try again.")
        except KeyError:
            print("Sorry, that is not a valid input. Let's try again.")


def get_burned_calories(METS, weight, duration):
    """Sends request to calculate_calories microservice to obtain total calories burned from exercise."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ (REQUEST) socket for sending requests
    socket.connect("tcp://localhost:5555")  # Connect to the server

    # Prepare the request data
    request = {
        'METS': METS,
        'weight': weight,
        'duration': duration
    }
    # Send the request
    socket.send_json(request)

    # Wait for the reply
    response = socket.recv_json()
    return response


def choose_exercise(user_amr, weight, exercise_log):
    """Logs an exercise a user has done."""
    clear()
    while True:
        print("What workout or exercise did you do?")
        for category_number in exercise_data:
            print(f'{category_number}. {exercise_data[category_number]["type"]}')
        print("8. Go back")
        try:
            exercise_choice = int(input("Enter the number corresponding with your selection here. "))
            if exercise_choice not in range(1, 9):
                print("Sorry, that is not a valid input. Let's try again.")
            elif exercise_choice == 8:
                clear()
                break
            else:
                clear()
                print(f'You picked {exercise_data[exercise_choice]["type"].lower()}. Below are various effort levels.'
                      f' What best matches the exercise you completed?')
                while True:
                    for item in exercise_data[exercise_choice]["effort"]:
                        print(f'{item} | {exercise_data[exercise_choice]["effort"][item]["description"]}')
                    print("\n")
                    item_choice = input("Type your selection here. ").lower()
                    while True:
                        try:
                            duration = int(input("For how many minutes did you conduct this exercise? "))
                            if duration > 0:
                                break
                            else:
                                print("Your exercise duration cannot be negative.")
                        except ValueError:
                            print("You must enter a number.")
                    if item_choice in exercise_data[exercise_choice]["effort"]:
                        calories_burned = get_burned_calories(
                            exercise_data[exercise_choice]["effort"][item_choice]["METS"], weight, duration)
                        calories_remaining = update_calories(user_amr, 0, 0, calories_burned)
                        # Add to exercise_data dictionary for compiling of report
                        exercise_name = exercise_data[exercise_choice]["type"]
                        exercise_log.append({"exercise_name": exercise_name, "duration": duration, "calories_burned": calories_burned})
                        return calories_remaining
                    else:
                        clear()
                        print("We could not calculate how many calories you burned.")
        except ValueError:
            print("Sorry, that is not a valid input. Let's try again.")
        except KeyError:
            print("Sorry, that is not a valid input. Let's try again.")


def produce_log(food_log, exercise_log):
    """Sends request to prepare_log microservice to return a log of all foods eaten and exercises performed."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ (REQUEST) socket for sending requests
    socket.connect("tcp://localhost:5600")  # Connect to the server

    # Prepare logs to send
    food_log_json = json.dumps(food_log)
    exercise_log_json = json.dumps(exercise_log)

    # Send logs
    socket.send_json({'food': food_log_json, 'exercise': exercise_log_json})

    # Wait for the reply
    response = socket.recv_string()
    return response


def check_recommended_exercise_goal(exercise_log):
    """Sends request to exercise_duration_tracker microservice to return a report of whether exercise goal is met."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ (REQUEST) socket for sending requests
    socket.connect("tcp://localhost:5700")  # Connect to the server

    # Prepare logs to send
    exercise_log_json = json.dumps(exercise_log)

    # Send logs
    socket.send_json(exercise_log_json)

    # Wait for the reply
    response = socket.recv_string()
    return response


def main_menu_choice(user_data, user_amr):
    """Determines user's choice re: whether to log food, log exercise, or exit Calorie Tracker."""
    while True:
        try:
            choice = int(input(
                (f'Your current plan is "{user_data["user_goal"]}". You can still eat {user_amr} calories '
                 f'today. What would you like to do? \n'
                 f'1. Log food.\n'
                 f'2. Log exercise.\n'
                 f'3. Generate food and exercise report.\n'
                 f'4. Check exercise duration goal. \n'
                 f'5. Exit Calorie Tracker.\n'
                 f'\n'
                 f'Enter your selection here: ')))
            if choice not in range(1, 6):
                print("Sorry, that is not a valid input. Let's try again.")
            else:
                return choice
        except ValueError:
            print("Sorry, that is not a valid input. Let's try again.")
