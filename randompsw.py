import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    use_lowercase = string.ascii_lowercase if use_lowercase else ""
    use_uppercase = string.ascii_uppercase if use_uppercase else ""
    use_digit = string.digits if use_digits else ""
    use_special = string.punctuation if use_special else ""

    all_chars = use_lowercase + use_uppercase + use_digit + use_special

    if len(all_chars) == 0:
        return "invalid criteria. Please select at least one character set."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    use_lowercase = input("Include lowercase (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase (yes/no): ").lower() == 'yes'
    use_digit = input("Include digits (yes/no): ").lower() == 'yes'
    use_special = input("Include symbols (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_lowercase, use_uppercase, use_digit, use_special)
    if password:
        print("Your generated password is: "+password)  # Here the Random Password printed

if __name__ == "__main__":
    main()

