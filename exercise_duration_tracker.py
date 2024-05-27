import json
import zmq


def generate_exercise_duration_report(exercise_data):
    """Generates report of progress toward Mayo Clinic's recommended 30-minute-per-day exercise duration goal."""
    total_time_exercised = 0
    for exercise in exercise_data:
        total_time_exercised += exercise["duration"]
    remaining_time = 30 - total_time_exercised

    if remaining_time > 0:
        response = f'The Mayo Clinic recommends 30 minutes of exercise daily. Based on your logged exercise time,' \
                   f'you should exercise for {remaining_time} more minutes to reach that goal.'

    else:
        response = f' The May Clinic recommends 30 minutes of exercise daily. Based on your logged exercise time, ' \
                   f'you have reached that goal!'

    return response


context = zmq.Context()
socket = context.socket(zmq.REP)  # Socket for sending responses
socket.bind("tcp://*:5700")  # Bind to port 5700

while True:
    # Wait for next request from client
    exercise_log_json = socket.recv_json()

    # Unpack log
    exercise_dictionary = json.loads(exercise_log_json)

    # Call generate_daily_report to create the report
    report = generate_exercise_duration_report(exercise_dictionary)

    # Send response to main program
    socket.send_string(report)