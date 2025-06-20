# password_strength_checker


# 🔐 Password Strength Checker Tool

A simple yet powerful Python tool to evaluate the strength of passwords, check for common/breached passwords, generate secure passwords, and guide users with best practices for online safety.

---

## 🧠 Features

- ✅ **Password Strength Evaluation**  
  Get feedback based on length, use of uppercase, lowercase, numbers, and special characters.

- 🔍 **Breach Check (Offline)**  
  Compares entered passwords against a list of common or leaked passwords (`common_passwords.txt`).

- 🔐 **Secure Password Generator**  
  Generates strong passwords with custom length (minimum 8 characters).

- 💡 **Password Security Tips**  
  Shows best practices for creating and managing strong passwords.

---

## 🛠️ Technologies Used

- **Python 3**
- `re` (Regex for password validation)
- `random`, `string` (Password generation)
- `colorama` (Colored terminal output for better UX)

---

## 📁 Project Structure
password_strength_checker/
├── password_checker.py
├── common_passwords.txt
├── README.md


---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- Install `colorama` (optional for color support)

```bash
pip install colorama


▶️ Run the Tool

python password_checker.py

📸 Tool Preview (CLI)

╔══════════════════════════════════════════╗
║      🔐 PASSWORD SECURITY TOOL           ║
╚══════════════════════════════════════════╝
Options:
1️⃣  Check password strength
2️⃣  Generate a strong password
3️⃣  Check if a password was breached
4️⃣  View password best practices
5️⃣  Exit

📌 Notes

    The breach check is based on a local list of common passwords (common_passwords.txt). For real-world use, integration with APIs like HaveIBeenPwned is recommended.

    Passwords are not saved or logged — your data stays safe and private.

✨ Author

Safwana Nasrin
B.Sc. Computer Science | Cybersecurity Enthusiast
LinkedIn (www.linkedin.com/in/safwananasrin)

📜 License

This project is open-source and free to use under the MIT License.


🙌 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change or add.
🔖 Tags

#Python #CyberSecurity #PasswordChecker #BeginnerProject #CLIApp


---

Let me know if you also want a **demo video script**, GitHub **topics/tags**, or to add this to your resume!
