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

def clear():
    print("\n" * 1000)


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


def obtain_personal_info(user_info):
    """Obtains personal data from user, if they choose to do so, to make
    personalized goal recommendations."""
    opt_in_procedure = True
    while opt_in_procedure is True:
        entering_age = True
        entering_gender = True
        entering_height = True
        entering_weight = True
        entering_activity_level = True
        confirming_data = True
        print("Please enter the following information.")

        # Obtain age.
        clear()
        while entering_age:
            try:
                age = int(input("What is your age? "))
                if age > 0:
                    user_info["user_age"] = age
                    entering_age = False
                else:
                    print("Age must be greater than 0.")
            except ValueError:
                print("You must enter a number for your age.")

        # Obtain gender
        clear()
        while entering_gender:
            gender = input("What is your gender? Enter m or f. ").lower()
            if gender == "m" or gender == "male":
                user_info["user_gender"] = "m"
                entering_gender = False
            elif gender == "f" or gender == "female":
                user_info["user_gender"] = "f"
                entering_gender = False
            else:
                print("Sorry, we could not register your input. Please try "
                      "again.")
        # Obtain height
        clear()
        while entering_height:
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
                    entering_height = False
                else:
                    print("Height must be greater than 0.")
            except ValueError:
                print("That is not a valid height.")

        # Obtain weight
        clear()
        while entering_weight:
            try:
                weight = int(input("What is your weight in pounds? Your input will be converted to kilograms. "))
                weight_in_kg = round(weight * .45359237)
                if weight > 0:
                    user_info["user_weight"] = weight_in_kg
                    entering_weight = False
                else:
                    print("Your weight must be greater than 0.")
            except ValueError:
                print("That is not a valid weight.")

        # Obtain activity level
        clear()
        while entering_activity_level:
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
                    entering_activity_level = False
            except ValueError:
                print("That is not a valid input. Please enter a number 1-5.")

        # Confirm selections
        clear()
        while confirming_data is True:
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
            if data_confirmation == 1:
                return user_info
            elif data_confirmation == 2:
                confirming_data = False
            else:
                print("That is not a valid input."
                      "\n")


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


def log_food(user_amr):
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
            if food_group_choice == 5:
                clear()
                break
        except ValueError:
            print("Sorry, that is not a valid input. Let's try again.")
        clear()
        print(f'You picked {foods[food_group_choice]["category"]}. Below are various foods and their serving sizes.'
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
                new_user_amr = update_calories(user_amr, foods[food_group_choice]["items"][item_choice]["calories"], num_servings, 0)
                user_amr = new_user_amr
                return user_amr
            else:
                print("We did not locate that food. Please check type your food choice and check your spelling.")


def log_exercise():
    """Logs an exercise a user has done."""
    pass


def main_menu_choice(user_data, user_amr):
    """Determine's user's choice re: whether to log food, log exercise, or exit Calorie Tracker."""
    while True:
        try:
            choice = int(input(
                (f'Your current plan is "{user_data["user_goal"]}". You can still eat {user_amr} calories '
                 f'today. What would you like to do? \n'
                 f'1. Log food.\n'
                 f'2. Log exercise.\n'
                 f'3. Exit Calorie Tracker.\n'
                 f'\n'
                 f'Enter your selection here: ')))
            if choice not in range(1, 4):
                print("Sorry, that is not a valid input. Let's try again.")
            else:
                return choice
        except ValueError:
            print("Sorry, that is not a valid input. Let's try again.")
