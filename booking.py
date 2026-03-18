import threading
from storage import save_data

lock = threading.Lock()

def process_request(request, seats):

    parts = request.split()

    if not parts:
        return "Invalid command"

    command = parts[0].upper()

    if command == "BOOK":

        if len(parts) != 2:
            return "Usage: BOOK <seat>"

        try:
            seat = int(parts[1])
        except:
            return "Invalid seat number"

        with lock:

            if seat not in seats:
                return "Seat does not exist"

            if seats[seat] == "Available":
                seats[seat] = "Booked"
                save_data(seats)
                return f"Seat {seat} booked successfully"

            else:
                return f"Seat {seat} already booked"

    elif command == "VIEW":

        available = [s for s in seats if seats[s] == "Available"]
        booked = [s for s in seats if seats[s] == "Booked"]

        return f"Available: {available}\nBooked: {booked}"

    elif command == "EXIT":
        return "Goodbye"

    else:
        return "Invalid command"