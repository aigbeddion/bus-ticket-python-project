import csv

print("🚌  Welcome to NCTX Bus Ticket System")
print("1. View first 5 ticket rows")
print("2. Exit")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    with open('mobile_products.csv', newline='') as file:
        reader = csv.reader(file)
        for row in list(reader)[:5]:
            print(row)
elif choice == "2":
    print("Goodbye!")
else:
    print("Invalid choice!")
