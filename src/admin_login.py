ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():
    print("\n--- Admin Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful! Welcome Admin.")
        return True
    else:
        print("Invalid login details.")
        return False


# Test the admin login
if admin_login():
    print("Admin panel accessed")
