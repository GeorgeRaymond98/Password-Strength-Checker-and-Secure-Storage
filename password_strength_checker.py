import hashlib  # Library for hashing (not used in this code, but can be used for hashing passwords)
import getpass  # Library to securely accept password input from the user
from cryptography.fernet import Fernet  # Fernet is a symmetric encryption library

# Function to generate and return an encryption key
def generate_key():
    return Fernet.generate_key()  # Generates a secure key for encryption using the Fernet module

# Function to encrypt the password using the provided key
def encrypt_password(password, key):
    f = Fernet(key)  # Creates a Fernet encryption object using the provided key
    encrypted_password = f.encrypt(password.encode())  # Encrypts the password (converted to bytes)
    return encrypted_password  # Returns the encrypted password

# Function to check the strength of the password and return a score out of 5
def check_password_strength(password):
    score = 0  # Initialize the score to 0
    
    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        score += 1  # Increase score by 1 if true
    
    # Check if the password contains any digits
    if any(char.isdigit() for char in password):
        score += 1  # Increase score by 1 if true
    
    # Check if the password contains any uppercase letters
    if any(char.isupper() for char in password):
        score += 1  # Increase score by 1 if true
    
    # Check if the password contains any lowercase letters
    if any(char.islower() for char in password):
        score += 1  # Increase score by 1 if true
    
    # Check if the password contains any special characters
    if any(char in "!@#$%^&*()-_" for char in password):
        score += 1  # Increase score by 1 if true
    
    return score  # Return the final strength score (out of 5)

# Main execution starts here
password = getpass.getpass("Enter a password: ")  # Securely prompt the user to enter a password
strength = check_password_strength(password)  # Check the strength of the entered password
print(f"Password strength: {strength}/5")  # Print the strength score of the password

key = generate_key()  # Generate an encryption key using the generate_key function
encrypted_password = encrypt_password(password, key)  # Encrypt the password using the generated key
print(f"Encrypted password: {encrypted_password}")  # Print the encrypted password
