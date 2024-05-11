def check_password(password, difficulty):
    if difficulty == "Easy":
        if len(password) >= 6:
            return True
        else:
            return "Password must be at least 6 characters long."

    elif difficulty == "Medium":
        if len(password) >= 8 and any(c.isupper() for c in password) \
                and any(c.islower() for c in password) \
                and any(c.isdigit() for c in password):
            return True
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(c.isupper() for c in password):
                feedback.append("Password must contain at least one uppercase letter.")
            if not any(c.islower() for c in password):
                feedback.append("Password must contain at least one lowercase letter.")
            if not any(c.isdigit() for c in password):
                feedback.append("Password must contain at least one digit.")
            return ", ".join(feedback)

    elif difficulty == "Hard":
        if len(password) >= 8 and any(c.isupper() for c in password) \
                and any(c.islower() for c in password) \
                and any(c.isdigit() for c in password) \
                and any(not c.isalnum() for c in password):
            return True
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(c.isupper() for c in password):
                feedback.append("Password must contain at least one uppercase letter.")
            if not any(c.islower() for c in password):
                feedback.append("Password must contain at least one lowercase letter.")
            if not any(c.isdigit() for c in password):
                feedback.append("Password must contain at least one digit.")
            if not any(not c.isalnum() for c in password):
                feedback.append("Password must contain at least one special character.")
            return ", ".join(feedback)

    else:
        return "Invalid difficulty level."


def main():
    difficulty = input("Choose the difficulty level (Easy, Medium, Hard): ").strip().capitalize()
    password = input("Enter your password: ").strip()

    result = check_password(password, difficulty)
    if result is True:
        print("Password meets the complexity requirements!")
    else:
        print("Password does not meet the complexity requirements. Details:", result)


if __name__ == "__main__":
    main()
