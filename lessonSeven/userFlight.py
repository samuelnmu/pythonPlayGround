print("WELCOME TO SAMMYBANKS AIRPORT, FEEL HOME")

class Flight:
    def __init__(self, capacity):
        """
        Initializes the flight with a given seat capacity and an empty list of passengers.
        """
        self.capacity = capacity
        self.passengers = []  # List to keep track of passengers on the flight

    def check_seats(self):
        """
        Checks if there are available seats on the flight.
        """
        return len(self.passengers) < self.capacity

    def add_passenger(self, name):
        """
        Attempts to add a passenger to the flight.
        """
        if self.check_seats():
            self.passengers.append(name)
            print(f"Passenger {name} has been added to the flight.")
            return True
        else:
            print(f"Sorry {name}, the flight is full!")
            return False

# Main logic for interacting with the Flight class
if __name__ == "__main__":
    flight_capacity = 2  # Define the capacity of the flight
    flight = Flight(flight_capacity)

    while True:
        # Get user input
        user_name = input("Enter your name (or type 'exit' to quit): ").strip()
        if user_name.lower() == 'exit':
            print("Thank you for visiting SAMMYBANKS AIRPORT!")
            break

        # Try to add the user to the flight
        flight.add_passenger(user_name)

        # Display current passengers
        print(f"Current passengers: {flight.passengers}")
