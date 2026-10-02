# Simple Movie Ticket Booking - Fresher Version

shows = ["Avengers", "KGF 2", "Avatar 2"]
price = 230 # Fixed Rs.230 as per question

bookings = {} # {id: [movie, seats, total]}
booking_id = 1

def list_shows():
    print("Available Shows:")
    for movie in shows:
        print(f"- {movie} : Rs.{price} per ticket")

def calculate_total(price, quantity, discount=0):
    # Default argument discount=0
    total = price * quantity
    total = total - (total * discount / 100)
    return total

def book_tickets(show_name, number_of_tickets, *seat_numbers, payment_mode="Cash"):
    global booking_id

    # Simple validation
    if show_name not in shows:
        print("Movie not found!")
        return

    if len(seat_numbers)!= number_of_tickets:
        print("Seat numbers not matching ticket count")
        return

    # Step 1: Base total using calculate_total
    base_total = calculate_total(price, number_of_tickets)

    # Step 2: Payment based pricing as per assignment
    if payment_mode == "GPay":
        final_total = base_total + 30 # +30 fee
    elif payment_mode == "Credit Card":
        final_total = base_total * 0.70 # 30% discount
    else: # Cash
        final_total = base_total # Rs.230 normal

    # Save booking
    bookings[booking_id] = [show_name, seat_numbers, final_total, payment_mode]
    print(f"Booking Success! ID={booking_id}, Movie={show_name}, Seats={seat_numbers}, Paid=Rs.{final_total} via {payment_mode}")
    booking_id += 1

def recursive_bill(tickets):
    # Recursive: Rs.20 off for every 2 tickets
    if tickets <= 0:
        return 0
    if tickets == 1:
        return price
    if tickets == 2:
        return (price * 2) - 20
    return ((price * 2) - 20) + recursive_bill(tickets - 2)

def cancel_booking(bid):
    if bid in bookings:
        refund = bookings[bid][2] # refund using same pricing
        print(f"Booking {bid} Cancelled, Refund Rs.{refund}")
        del bookings[bid]
    else:
        print("Invalid ID")

# --- Main ---
while True:
    print("\n1.List 2.Book 3.Loyalty Bill 4.Cancel 5.Exit")
    ch = input("Choice: ")

    if ch == '1':
        list_shows()

    elif ch == '2':
        list_shows()
        movie = input("Enter movie name: ")
        qty = int(input("Enter no. of tickets: "))
        seats = input(f"Enter {qty} seat numbers: ").split()
        seats = [int(s) for s in seats]
        mode = input("Payment (GPay/Credit Card/Cash): ")
        book_tickets(movie, qty, *seats, payment_mode=mode)

    elif ch == '3':
        n = int(input("Enter tickets for loyalty offer: "))
        print(f"Total Bill = Rs.{recursive_bill(n)}")

    elif ch == '4':
        b = int(input("Enter Booking ID: "))
        cancel_booking(b)

    elif ch == '5':
        break
