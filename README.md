# 🔐 Secure Coding Review - Flask Login Module

A professional secure code audit project for a basic Flask-based login system. This project showcases how to identify and fix real-world vulnerabilities like SQL injection, insecure password handling, and hardcoded secrets using secure coding practices and tools like Bandit.

---

## 📌 Objective

- Perform a **secure coding review** of a vulnerable Flask login app.
- Use **manual inspection** and **static analysis tools** to identify issues.
- Refactor the code using **OWASP** and **industry best practices**.
- Document vulnerabilities, fixes, and suggestions for future development.

---

## 📁 Project Structure

secure-coding-review/
├── vulnerable_app.py # Insecure login logic
├── secure_app.py # Secure refactored login logic
├── bandit_report.txt # Static analysis report
├── requirements.txt # Python dependencies
├── .gitignore # Files ignored by Git
└── README.md # Full documentation

---

## ⚠️ Identified Vulnerabilities in `vulnerable_app/login.py`

| 🔢 | Vulnerability              | Description |
|----|----------------------------|-------------|
| 1  | **SQL Injection**          | User inputs are directly injected into raw SQL queries without sanitization. |
| 2  | **Hardcoded Secret Key**  | Flask's `app.secret_key` is exposed in source code. |
| 3  | **Plaintext Passwords**   | Passwords are compared in plain text without hashing. |
| 4  | **No Input Validation**   | Username/password not validated for length/type. |
| 5  | **No Secure Session Handling** | Session management is default and insecure. |

---

## ✅ Secure Fixes in `secure_app/login_secure.py`

| 🔢 | Fix Applied                  | Explanation |
|----|------------------------------|-------------|
| 1  | **Parameterized Queries**    | Prevent SQL Injection using `?` placeholders. |
| 2  | **Use of `.env` Secret Key** | Secret key loaded from environment variables. |
| 3  | **Password Hashing**         | `generate_password_hash()` and `check_password_hash()` used. |
| 4  | **Input Validation**         | Basic length checks added for inputs. |
| 5  | **Secure Session Management**| Secret key is kept private and protected. |

---

## 🛠️ Tools Used

- [Bandit](https://bandit.readthedocs.io/en/latest/) – Python static analyzer for security issues.
- [Flask](https://flask.palletsprojects.com/) – Lightweight web framework.
- [Werkzeug](https://werkzeug.palletsprojects.com/) – Password hashing utilities.
- `.env` – To store environment variables securely.

---

## 📋 Bandit Report Sample

```bash
>> bandit vulnerable_app.py
```
## To Run the Secure App

Step 1
```bash
https://github.com/astephen-git/codealpha_Secure.coding.review.git
cd codealpha_Secure.coding.review
```
Step 2

Add the your SECRET_KEY in Secure_app.py in this case the SECRET_KEY available in vulnerable_app.py 

Step 3

Install Required Packages
```bash
pip install -r ../requirements.txt
```
Step 4

Run the Secure App
```bash
python Secure_app.py
```
