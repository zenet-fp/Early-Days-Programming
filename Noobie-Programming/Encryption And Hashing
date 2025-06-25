import hashlib
from cryptography.fernet import Fernet


# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()


# Function to encrypt a password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password


# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password


# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Main function
def main():
    password = input("Enter your password: ")

    # Generate a key for encryption
    key = generate_key()

    # Encrypt the password
    encrypted_password = encrypt_password(password, key)

    # Hash the password
    hashed_password = hash_password(password)

    # Store the original password, encrypted password, and hashed password
    print("\nStored Information:")
    print(f"Original Password: {password}")
    print(f"Encrypted Password: {encrypted_password}")
    print(f"Hashed Password: {hashed_password}")

    # Decrypt the password for demonstration
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"\nDecrypted Password: {decrypted_password}")


if __name__ == "__main__":
    main()
