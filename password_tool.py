import re
import os
import random
import string

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = ''
        GREEN = ''
        YELLOW = ''
        CYAN = ''
        MAGENTA = ''
        BLUE = ''
    class Style:
        RESET_ALL = ''

# Load common or breached passwords
def load_common_passwords(filename="common_passwords.txt"):
    if not os.path.exists(filename):
        print(Fore.RED + "⚠️  common_passwords.txt not found!")
        return set()
    with open(filename, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file)

# Evaluate password strength
def evaluate_password(password, common_passwords):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("📏 Length is okay, but 12+ is better.")
    else:
        feedback.append("❌ Too short. Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔠 Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔡 Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Add numbers.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("💥 Add special characters.")

    if password in common_passwords:
        feedback.append("🚫 Common or breached password.")
    else:
        score += 1

    if score >= 7:
        strength = Fore.GREEN + "💪 Very Strong"
    elif score >= 5:
        strength = Fore.CYAN + "✅ Strong"
    elif score >= 3:
        strength = Fore.YELLOW + "⚠️ Moderate"
    else:
        strength = Fore.RED + "❌ Weak"

    return strength, feedback

# Password generator
def generate_password(length=12):
    if length < 8:
        length = 8
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Check if password is in breach list
def check_breach(password, common_passwords):
    if password in common_passwords:
        print(Fore.RED + "❗ This password has been found in known breaches!")
    else:
        print(Fore.GREEN + "✅ This password is not found in the local breach list.")
    print(Fore.YELLOW + "Note: This is a basic local check. Use real-time services like 'Have I Been Pwned' for advanced checks.\n")

# Password tips viewer
def show_tips():
    print(Fore.MAGENTA + "\n🔐 Password Best Practices:")
    tips = [
        "✅ Use at least 12 characters.",
        "✅ Include uppercase, lowercase, numbers, and symbols.",
        "✅ Avoid using your name, DOB, or common words.",
        "✅ Never reuse passwords across important accounts.",
        "✅ Use a password manager to save strong passwords.",
        "✅ Enable two-factor authentication (2FA) wherever possible."
    ]
    for tip in tips:
        print(" - " + tip)
    print()

# Menu banner
def banner():
    print(Fore.MAGENTA + "\n╔══════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║      🔐 PASSWORD SECURITY TOOL           ║")
    print(Fore.MAGENTA + "╚══════════════════════════════════════════╝")
    print(Fore.BLUE + "Options:")
    print("1️⃣  Check password strength")
    print("2️⃣  Generate a strong password")
    print("3️⃣  Check if a password was breached")
    print("4️⃣  View password best practices")
    print("5️⃣  Exit\n")

# Main function
def main():
    common_passwords = load_common_passwords()

    while True:
        banner()
        choice = input(Fore.YELLOW + "👉 Enter your choice (1-5): ")

        if choice == "1":
            password = input("\n🔑 Enter your password: ")
            strength, tips = evaluate_password(password, common_passwords)
            print(f"\n🔎 Password Strength: {strength}{Style.RESET_ALL}")
            if tips:
                print(Fore.YELLOW + "💡 Suggestions:")
                for tip in tips:
                    print(f" - {tip}")
            else:
                print(Fore.GREEN + "✅ Your password is excellent!")
            print("\n" + "-" * 50 + "\n")

        elif choice == "2":
            try:
                length = int(input("🔢 Desired password length (minimum 8): "))
            except ValueError:
                print(Fore.RED + "❌ Invalid number. Using default length (12).")
                length = 12
            if length < 8:
                print(Fore.RED + "❌ Too short. Length adjusted to 12.")
                length = 12
            password = generate_password(length)
            print(Fore.GREEN + f"\n🔐 Suggested Password: {password}")
            print("💡 Tip: Copy this and store it in a password manager.\n")
            print("-" * 50 + "\n")

        elif choice == "3":
            password = input("🔎 Enter password to check breach: ")
            check_breach(password, common_passwords)

        elif choice == "4":
            show_tips()

        elif choice == "5":
            print(Fore.CYAN + "\n👋 Goodbye! Stay safe online.\n")
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please enter a number between 1–5.\n")

# Run the script
if __name__ == "__main__":
    main()
