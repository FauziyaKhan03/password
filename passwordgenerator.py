import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    num_passwords = int(input("How many passwords do you want to generate? "))
    min_length = num_passwords

    print(f"Generate {num_passwords} password:")
    print(f"Minimum length of password should be {min_length}")

    passwords = []

    for _ in range(num_passwords):
        password_length = int(input("Enter the length of password:"))
        password = generate_password(password_length)
        passwords.append(password)

   