import csv

def show_categories():
    with open('mobile_products.csv', newline='') as f:
        rows = list(csv.reader(f))
    cats = sorted(set(r[1] for r in rows[1:]))
    for i, c in enumerate(cats, 1):
        print(f"{i}. {c}")
    return cats

def show_topups(cat):
    with open('mobile_products.csv', newline='') as f:
        rows = list(csv.reader(f))
    data = [r for r in rows[1:] if r[1] == cat]
    for i, r in enumerate(data, 1):
        print(f"{i}. {r[4]} | {int(r[5])/100:.2f} £ | {r[6]} | {r[7]} | Qty: {r[9]}")

while True:
    print("\n=== NCTX Ticket Menu ===")
    print("1. View categories")
    print("2. Pick category & see top-ups")
    print("3. Exit")
    ch = input("Choice: ")
    if ch == "1":
        cats = show_categories()
    elif ch == "2":
        cats = show_categories()
        c = int(input("Select category number: ")) - 1
        show_topups(cats[c])
    elif ch == "3":
        print("Goodbye!"); break
    else:
        print("Invalid choice!")
