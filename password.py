def password_check(password):
    if len(password) < 8:
        return False
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False
    special_character = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

    for i in password:
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
        if i in special_character:
            has_special = True

    if has_digit and has_upper and has_lower and has_special:
        return True
    else:
        return False

attempts = 3
while attempts > 0:
    password = input(f"Enter your password ({attempts} attempts left): ")
    
    if password_check(password):
        print("Strong password")
        break  # Exit loop if the password is strong
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Weak password. Use at least 8 characters, including uppercase, lowercase, a digit, and a special character. Try again!\n")
        else:
            print("Too many failed attempts! Access denied.")

        
    
            
            