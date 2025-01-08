class Flight:
    """
    A class to represent a flight with a fixed capacity and a list of passengers.
    """
    def __init__(self, capacity):
        """
        Initializes a Flight object with a specified capacity.

        Args:
            capacity (int): The maximum number of passengers the flight can hold.
        """
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        """
        Attempts to add a passenger to the flight if there are open seats.

        Args:
            name (str): The name of the passenger.

        Returns:
            bool: True if the passenger was added, False if no seats are available.
        """
        if self.open_seats() > 0:
            self.passengers.append(name)
            return True
        return False

    def open_seats(self):
        """
        Calculates the number of available seats on the flight.

        Returns:
            int: The number of open seats.
        """
        return self.capacity - len(self.passengers)


# Example usage
flight = Flight(3)  # Create a flight with a capacity of 3 seats

people = ["Samuel", "Ngige", "Mungai", "John"]  # List of people trying to board the flight
for person in people:
    # Attempt to add each person to the flight
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to the flight successfully.")
    else:
        print(f"No available seats for {person}.")
