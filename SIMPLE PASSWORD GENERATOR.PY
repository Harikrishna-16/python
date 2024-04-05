import random
import string

def generate_password(length=8):
    """
    Generate a random password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Simple Password Generator")
    print("-------------------------")
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Length must be greater than 0.")
        return
    
    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
