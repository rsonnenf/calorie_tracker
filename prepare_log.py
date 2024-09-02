import json
import zmq


def generate_daily_report(food_data, exercise_data):
    """Generates a report of all food consumed and exercise undertaken."""
    report = "*** Here is a list of the foods you have eaten today. *** \n"
    total_calories_consumed = 0
    for food in food_data:
        report += f"- {food['food_name']} | {food['calories_consumed']} calories total\n"
        total_calories_consumed += food["calories_consumed"]

    report += f"You have consumed a total of {total_calories_consumed} calories.\n\n"

    report += "*** Here is a list of the exercises you have performed today. *** \n"
    total_calories_burned = 0
    for exercise in exercise_data:
        report += f"- {exercise['exercise_name']} | {exercise['calories_burned']} calories burned total\n"
        total_calories_burned += exercise['calories_burned']

    report += f"You have burned a total of {total_calories_burned} calories through exercise.\n"

    return report


context = zmq.Context()
socket = context.socket(zmq.REP)  # Socket for sending responses
socket.bind("tcp://*:5554")  # Bind to port 5600

while True:
    # Wait for next request from client
    logs = socket.recv_json()
    food_json = logs['food']
    exercise_json = logs['exercise']
    print(f"Request Received: {logs}")

    # Unpack lists
    food_dictionary = json.loads(food_json)
    exercise_dictionary = json.loads(exercise_json)

    # Call generate_daily_report to create the report
    report = generate_daily_report(food_dictionary, exercise_dictionary)

    # Send response to main program
    print(f"Response to be sent: {report}")
    socket.send_string(report)
