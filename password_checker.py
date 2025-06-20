import re
import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # Fallback if colorama is not installed
    class Fore:
        RED = ''
        GREEN = ''
        YELLOW = ''
        CYAN = ''
        MAGENTA = ''
        BLUE = ''
    class Style:
        RESET_ALL = ''

# Load common passwords from the text file
def load_common_passwords(filename="common_passwords.txt"):
    if not os.path.exists(filename):
        print(Fore.RED + "⚠️  common_passwords.txt not found in the project folder!")
        return set()
    with open(filename, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file)

# Evaluate password strength
def evaluate_password(password, common_passwords):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("📏 Length is okay, but try 12+ characters.")
    else:
        feedback.append("❌ Too short! Use at least 8 characters.")

    # Complexity checks
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
        feedback.append("💥 Add special characters (e.g., ! @ #).")

    # Common password check
    if password in common_passwords:
        feedback.append("🚫 This is a common password. Use something more unique.")
    else:
        score += 1

    # Determine strength level
    if score >= 7:
        strength = Fore.GREEN + "💪 Very Strong"
    elif score >= 5:
        strength = Fore.CYAN + "✅ Strong"
    elif score >= 3:
        strength = Fore.YELLOW + "⚠️ Moderate"
    else:
        strength = Fore.RED + "❌ Weak"

    return strength, feedback

# Welcome banner
def banner():
    print(Fore.MAGENTA + "╔═════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║        🔐 PASSWORD STRENGTH CHECKER         ║")
    print(Fore.MAGENTA + "╚═════════════════════════════════════════════╝")
    print(Fore.BLUE + "Type 'exit' anytime to quit the checker.\n")

# Main function
def main():
    banner()
    common_passwords = load_common_passwords()

    while True:
        password = input(Fore.YELLOW + "🔑 Enter your password: ")

        if password.lower() == "exit":
            print(Fore.CYAN + "\n👋 Exiting Password Checker. Stay safe and secure!")
            break

        strength, suggestions = evaluate_password(password, common_passwords)
        print(f"\n🔎 Password Strength: {strength}{Style.RESET_ALL}\n")

        if suggestions:
            print(Fore.YELLOW + "💡 Suggestions to improve your password:")
            for tip in suggestions:
                print(f" - {tip}")
        else:
            print(Fore.GREEN + "✅ Your password is excellent and secure!")

        print(Fore.MAGENTA + "\n" + "-" * 50 + "\n")

# Run the script
if __name__ == "__main__":
    main()
