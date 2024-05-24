import fitness_goals, time, zmq

print("""   _____      _            _        _______             _             
  / ____|    | |          (_)      |__   __|           | |            
 | |     __ _| | ___  _ __ _  ___     | |_ __ __ _  ___| | _____ _ __ 
 | |    / _` | |/ _ \| '__| |/ _ \    | | '__/ _` |/ __| |/ / _ \ '__|
 | |___| (_| | | (_) | |  | |  __/    | | | | (_| | (__|   <  __/ |   
  \_____\__,_|_|\___/|_|  |_|\___|    |_|_|  \__,_|\___|_|\_\___|_|                                                               
                                                                      """)


def clear():
    print("\n" * 50)


print("Welcome to Calorie Tracker!\n"
      "Use this app to track your fitness goals and obtain personalized assessments of your fitness habits!\n")
user_data = {}
# Obtain user's fitness goal
print("***YOUR FITNESS GOAL***")
fitness_goals.obtain_fitness_goal(user_data)

print("***YOUR INFORMATION***")
# Determine if user wants to provide personal data.
while True:
    opt_in_choice = int(input("Calorie Tracker can use your individual data to provide you with more personalized "
                              "assessments of whether you are meeting your goals. You may choose not to provide this "
                              "information, and a default calorie allotment will be assigned to you. However, "
                              "your assessments may be less accurate. \n "
                              "\n"
                              "Would you like to provide your personalized data? \n"
                              "Press 1 if you would like to enter your information. Otherwise, press 2. "))

    # If user opts to provide data, obtain user information.
    if opt_in_choice == 1:
        fitness_goals.obtain_personal_info(user_data)
        user_bmr = fitness_goals.calculate_bmr(user_data)
        user_amr = fitness_goals.calculate_amr(user_data, user_bmr)
        break

    # If user opts not to provide data, use standard 2000 calorie diet.
    elif opt_in_choice == 2:
        user_data["user_weight"] = 70
        user_amr = 2000
        break
    else:
        print("Sorry, that is not a valid input. Let's try again.")

# With plan and user information obtained (or default diet used), user can now log food or exercise.
clear()


print("***YOUR PLAN***")
while True:
    user_main_menu_choice = fitness_goals.main_menu_choice(user_data, user_amr)
    if user_main_menu_choice == 1:
        user_amr = fitness_goals.log_food(user_amr)
    elif user_main_menu_choice == 2:
        updated_calories = fitness_goals.choose_exercise(user_amr, user_data["user_weight"])
        user_amr = updated_calories
    elif user_main_menu_choice == 3:
        clear()
        print("Thank you for using Calorie Tracker!")
        time.sleep(3)
        exit()
