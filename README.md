
# Email Project (Python)

A simple Python project that sends an email using Python’s built‑in `smtplib` library.  
This project demonstrates how to connect to an SMTP server, log in securely, and send a basic message programmatically.

---

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-Email_Automation-blue)



## 📂 Project Structure
Email-Project/
- main.py        – primary email-sending script
- main_2.py      – alternative version of the email script (performs the same function as main.py but with slight variations in code)

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Email-Project.git

2. **Navigate into the project folder**
   cd Email-Project

3. **Run the script**
   python main.py


## ⚙️ Requirements
Python 3.x
An SMTP-enabled email account (e.g., Gmail)
App Password if using Gmail with 2‑Factor Authentication


## 🔐 Security Note
Never store your real email password directly inside the script.
Use any of the following secure methods instead:

Environment variables
A .env file (excluded from GitHub)
Gmail App Passwords

This keeps your credentials safe.

## 📧 About This Project
This project was created for learning and practice — specifically to understand how Python’s smtplib works, how SMTP authentication functions, and how to send automated emails from a Python script.
