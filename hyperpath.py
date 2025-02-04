import os
import hashlib
from cryptography.fernet import Fernet
import getpass

class HyperPath:
    def __init__(self):
        self.encryption_key = self.generate_key()
        self.fernet = Fernet(self.encryption_key)

    def generate_key(self):
        """
        Generate a secure encryption key.
        """
        key = Fernet.generate_key()
        print(f"Encryption key generated: {key.decode()}")
        return key

    def hash_password(self, password):
        """
        Hash the password using SHA-256.
        """
        hashed = hashlib.sha256(password.encode()).hexdigest()
        print(f"Password hashed: {hashed}")
        return hashed

    def encrypt_data(self, data):
        """
        Encrypt the data using the Fernet symmetric encryption.
        """
        encrypted = self.fernet.encrypt(data.encode())
        print(f"Data encrypted: {encrypted.decode()}")
        return encrypted

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the data using the Fernet symmetric encryption.
        """
        try:
            decrypted = self.fernet.decrypt(encrypted_data).decode()
            print(f"Data decrypted: {decrypted}")
            return decrypted
        except Exception as e:
            print("Failed to decrypt data: ", e)
            return None

    def authenticate_user(self, stored_hash):
        """
        Authenticate a user by comparing provided password hash with stored hash.
        """
        password = getpass.getpass("Enter your password: ")
        hashed_password = self.hash_password(password)
        if hashed_password == stored_hash:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False


if __name__ == "__main__":
    hyperpath = HyperPath()

    # Example usage
    password = getpass.getpass("Set a password: ")
    password_hash = hyperpath.hash_password(password)

    data_to_secure = "Sensitive information"
    encrypted_data = hyperpath.encrypt_data(data_to_secure)

    # Simulate authentication
    if hyperpath.authenticate_user(password_hash):
        decrypted_data = hyperpath.decrypt_data(encrypted_data)
        print("Decrypted data: ", decrypted_data)
    else:
        print("Access denied.")