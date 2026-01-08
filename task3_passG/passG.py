import random
import string

# -------- Password Strength Check --------
def is_strong(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_symbol


# -------- Generate Password --------
def generate_password():
    print("\n--- PASSWORD GENERATOR ---")

    while True:
        try:
            length = int(input("Enter password length (min 6): "))
            if length < 6:
                print("Password must be at least 6 characters.")
            else:
                break
        except ValueError:
            print("Enter a valid number!")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include special characters? (y/n): ").lower() == "y"

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        print("You must choose at least one option!")
        return None

    password_chars = []

    if use_upper:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))

    while len(password_chars) < length:
        password_chars.append(random.choice(char_pool))

    random.shuffle(password_chars)
    password = "".join(password_chars)

    print("\n✅ Generated Password:", password)
    return password


# -------- Update Password --------
def update_password(old_pass):
    print("\n--- UPDATE PASSWORD ---")
    old = input("Enter old password: ")

    if old != old_pass:
        print("❌ Wrong old password!")
        return old_pass

    new_pass = input("Enter new password: ")
    confirm = input("Confirm new password: ")

    if new_pass != confirm:
        print("❌ Passwords do not match!")
        return old_pass

    if not is_strong(new_pass):
        print("❌ Weak password!")
        print("Password must contain:")
        print("- Uppercase letter")
        print("- Lowercase letter")
        print("- Number")
        print("- Special character")
        return old_pass

    print("✅ Password updated successfully!")
    return new_pass


# -------- Main Program --------
print("========== PASSWORD GENERATOR SYSTEM ==========")

current_password = generate_password()

if current_password:
    choice = input("\nDo you want to update the password? (y/n): ").lower()

    if choice == "y":
        current_password = update_password(current_password)

print("\nThank you for using the Password Generator!")
