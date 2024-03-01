def display_room_types_and_rates(room_types, nightly_rates):
    print("\nAvailable Room Types:")
    for i in range(len(room_types)):
        print(f"{i+1}. {room_types[i]} - RM {nightly_rates[i]} per night")

def calculate_total_cost(room_type_index, num_rooms, check_in, check_out, nightly_rates):
    total_nights = (check_out - check_in).days
    total_cost = nightly_rates[room_type_index] * num_rooms * total_nights
    return total_cost

def main():
    room_types = ["Single", "Double", "Suite"]
    nightly_rates = [100, 150, 250]
    additional_services = {"breakfast": 20, "wifi": 10, "parking": 15}

    print("\nWelcome to One World Hotel Reservation System")
    display_room_types_and_rates(room_types, nightly_rates)

    try:
        room_type_index = int(input("\nPlease select a room type (1/2/3): ")) - 1
        num_rooms = int(input("\nEnter number of rooms: "))
        check_in = input("\nEnter check-in date (YYYY-MM-DD): ")
        check_out = input("Enter check-out date (YYYY-MM-DD): ")

        check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d")
        check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d")

        total_cost = calculate_total_cost(room_type_index, num_rooms, check_in, check_out, nightly_rates)

        print("\nReservation Details:")
        print(f"Room Type: {room_types[room_type_index]}")
        print(f"Number of Rooms: {num_rooms}")
        print(f"Check-in Date: {check_in.strftime('%Y-%m-%d')}")
        print(f"Check-out Date: {check_out.strftime('%Y-%m-%d')}")
        print(f"Total Cost for Room(s) Only: RM {total_cost:.2f}")

        additional_services_cost = 0
        while True:
            service = input("Would you like to add breakfast, wifi, or parking? (Enter service name or 'done' to proceed): ").lower()
            if service == "done":
                break
            elif service in additional_services:
                additional_services_cost += additional_services[service]
            else:
                print("Invalid service. Please choose from breakfast, wifi, or parking.")

        total_cost += additional_services_cost
        print(f"\nTotal Cost including Additional Services: RM {total_cost:.2f}")

        confirm = input("\nWould you like to confirm your reservation? (yes/no): ")
        if confirm.lower() == "yes":
            print("Reservation confirmed. Thank you for choosing our hotel. Enjoy your stay!")
        else:
            print("Reservation canceled.")

    except ValueError:
        print("Invalid input. Please enter valid information.")

if __name__ == "__main__":
    import datetime
    main()