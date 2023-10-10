from cryptography.fernet import Fernet


class cryptoFile:

    def __init__(self, key=None) -> None:
        self.key = key

    def generate_key(self,):
        self.key = Fernet.generate_key()
        return self.key
    

    def encrypt_file(self, path):
        fernet = Fernet(self.key)

        with open(path, 'rb') as file:
            original = file.read()
        
        encrypted  = fernet.encrypt(original)
        with open(path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    
    def decrypt_file(self, path:str):
        fernet = Fernet(self.key)
 
        # opening the encrypted file
        with open(path, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        return decrypted