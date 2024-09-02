import zmq


def request_calories_burned_calculation():
    """Calculates calories burned by exercise."""
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Socket for sending responses
    socket.bind("tcp://*:5558")  # Bind to port 5555

    while True:
        # Wait for next request from client
        request = socket.recv_json()
        print(f'Request received: {request}')

        # Convert data sent from client json
        mets = float(request["METS"])
        weight = float(request["weight"])
        duration = float(request["duration"])

        try:
            calories_burned_per_min = mets * 3.5 * weight / 200
            response = round(calories_burned_per_min * duration)
        except Exception as exception:
            response = str(exception)

        # Send response to main program
        print(f"Response to be returned: {response}")
        socket.send_json(response)


if __name__ == "__main__":
    request_calories_burned_calculation()
