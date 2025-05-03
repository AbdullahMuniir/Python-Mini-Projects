import random

class TicketSystem:
    def __init__(self):
        self.punjab_cities = [
            "Lahore", "Faisalabad", "Rawalpindi", "Gujranwala", "Multan",
            "Sargodha", "Bahawalpur", "Sialkot", "Sheikhupura", "Rahim Yar Khan"
        ]
        self.sindh_cities = [
            "Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah",
            "Mirpur Khas", "Shikarpur", "Jacobabad", "Thatta", "Dadu"
        ]

    def generate_ticket(self, departure, destination):
        departure = departure.strip().title()
        destination = destination.strip().title()

        if departure in self.punjab_cities and destination in self.sindh_cities:
            ticket_number = f"TKT{random.randint(10000, 99999)}"
            train_number = f"PKX-{random.randint(100, 999)}"
            ticket_fare = random.randint(1000, 3000)

            print("\nTicket Generated Successfully:")
            print(f"Ticket Number   : {ticket_number}")
            print(f"Train Number    : {train_number}")
            print(f"Ticket Fare     : PKR {ticket_fare}")
            print(f"From            : {departure}")
            print(f"To              : {destination}")
        else:
            print("\nRoute Unavailable. Ticket cannot be generated.")

# Run the ticket system
system = TicketSystem()
departure_input = input("Enter Departure City: ")
destination_input = input("Enter Destination City: ")
system.generate_ticket(departure_input, destination_input)
