import string
import secrets

def generate_password(length=12):
    # Character sets
    letters = string.ascii_letters   # a-z + A-Z
    digits = string.digits           # 0-9


    # Combine all character sets
    all_chars = letters + digits

    # Ensure password contains at least one of each
    password = [
        secrets.choice(letters),
        secrets.choice(digits),

    ]

    # Fill the rest of the password
    password += [secrets.choice(all_chars) for _ in range(length - 3)]

    # Shuffle to avoid predictable order
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(16))

