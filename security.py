import sys       # Used to exit the program, get system-specific info

# Protect your assistant with password
def password_lock():
    correct_password = "kushal@123"
    attempts = 3     # allow 3 tries

    while attempts > 0:
        entered = input("Enter Password: ")

        if entered == correct_password:
            print("✅ Access Granted.")
            return   
        else:
            attempts -= 1
            print(f"❌ Incorrect. Attempts left: {attempts}")
    
    print("🚫 Too many failed attempts. Exiting...")
    sys.exit()     # Exit program if too many wrong attempts