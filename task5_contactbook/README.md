# 📒 Contact Book – Python Project

A simple and user-friendly **Contact Book application** built using Python.  
This program allows users to store, manage, and update contact information with **phone number validation**.

---

## ✨ Features

- ➕ Add new contacts  
- 📋 View all saved contacts  
- 🔍 Search contacts by **name or phone number**  
- ✏️ Update contact details  
- 🗑️ Delete contacts  
- 📞 Phone number validation (**only 10 digits allowed**)  
- 🔁 Partial updates supported (keep old values if blank)  
- 🖥️ Menu-driven, easy-to-use interface  

---

## 🛠️ Technologies Used

- **Python 3**
- Built-in functions only (no external libraries required)

---

## ▶️ How to Run the Program

1. Make sure Python is installed:
   ```bash
   python --version
Save the file as:

bash
Copy code
contactbook.py
Run the program:

bash
Copy code
python contactbook.py
📞 Phone Number Validation
Only numbers are accepted

Phone number must be exactly 10 digits

Invalid numbers are rejected during:

Adding a contact

Updating a contact

🎮 Menu Options
markdown
Copy code
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
📷 Sample Output
mathematica
Copy code
===== CONTACT BOOK =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1

Enter Name: Rahul
Enter Phone Number (10 digits): 1234
❌ Invalid phone number! Enter exactly 10 digits.
Enter Phone Number (10 digits): 9876543210
Enter Email: rahul@gmail.com
Enter Address: Pune
✅ Contact added successfully!
🚀 Future Enhancements
💾 Save contacts to a file (persistent storage)

🖥️ GUI version using Tkinter

📧 Email validation

🔐 Password-protected access