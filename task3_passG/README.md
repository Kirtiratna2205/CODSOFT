📌 Features
✅ Password Generation

User chooses password length

User selects complexity:

Uppercase letters

Lowercase letters

Numbers

Special characters

Ensures strong password

At least one character from each selected type

Random and secure password creation

🔁 Update Password System

Verifies old password

Allows user to set a new password

Confirms password before saving

Blocks weak passwords

Displays proper success/error messages

🛠️ Technologies Used

Python 3

Built-in modules:

random

string

🚀 How to Run the Program

Install Python 3 on your system

Save the file as:

password_generator.py


Open terminal / command prompt

Run the program:

python password_generator.py

📖 How the Program Works

User enters desired password length

User selects character types

Program generates a strong password

User can choose to update the password

System checks:

Old password correctness

New password strength

Password is updated successfully

🖥️ Sample Output
🔹 Generate Password
========== PASSWORD GENERATOR SYSTEM ==========

--- PASSWORD GENERATOR ---
Enter password length (min 6): 10
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

✅ Generated Password: A9@kP#7mQ!

🔹 Update Password
Do you want to update the password? (y/n): y

--- UPDATE PASSWORD ---
Enter old password: A9@kP#7mQ!
Enter new password: New@Pass123
Confirm new password: New@Pass123
✅ Password updated successfully!

❗ Password Strength Rules

A strong password must contain:

At least 1 uppercase letter

At least 1 lowercase letter

At least 1 number

At least 1 special character

Minimum 6 characters

🎯 Future Enhancements

GUI version using Tkinter

Save passwords securely using hashing

Add password strength meter

Export password to file