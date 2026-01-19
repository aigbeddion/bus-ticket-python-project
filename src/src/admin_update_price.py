import csv

CSV_FILE = "data/tickets.csv"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def load_tickets():
    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        tickets = list(reader)
    return header, tickets

def save_tickets(header, tickets):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(tickets)

def update_ticket_price():
    header, tickets = load_tickets()

    print("\nShowing first 10 tickets only:\n")
    for i, ticket in enumerate(tickets[:10]):
        print(f"{i+1}. {ticket[1]} | Price: {ticket[5]}")

    choice = int(input("\nSelect ticket number to update: ")) - 1
    new_price = input("Enter new price: ")

    tickets[choice][5] = new_price
    save_tickets(header, tickets)

    print("✅ Ticket price updated successfully!")

if admin_login():
    update_ticket_price()
else:
    print("❌ Access denied")


