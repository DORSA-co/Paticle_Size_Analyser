import bcrypt
import CONSTANTS

class passwordManager:

    @staticmethod
    def to_byte(x: str) -> bytes:
        """converts a string to bytes

        Args:
            x (str): input str

        Returns:
            bytes: bytes of input
        """
        
        if isinstance(x,bytes):
            return x
        if isinstance(x, str):
            return x.encode("utf-8")

        assert False, "input only can be <class str> or <class bytes>"


    @staticmethod
    def hash_password(password: str, decode: bool =True) -> str:
        """hash an input str password

        Args:
            password (str): input password
            decode (bool): if True, returns hashed password in <class str> . if not, returns in <class bytes> format. Default is True

        Returns:
            str: hashes password
        """

        pwd_bytes = passwordManager.to_byte(password)
        #salt make a hash more strong
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw( pwd_bytes, salt )
        if decode:
            return hashed_pass.decode()
        return hashed_pass
    
    @staticmethod
    def check_password(input_pass:str, stored_pass:str) -> bool:
        """check a input password is correct or not

        Args:
            input_pass (str): Password entered for login
            stored_pass (str): hashed password that saved in you database

        Returns:
            bool: returns True if password is correct
        """

        input_pass_bytes = passwordManager.to_byte(input_pass)
        stored_pass_bytes = passwordManager.to_byte(stored_pass)
        return bcrypt.checkpw( input_pass_bytes, stored_pass_bytes)



class regiterUtils:
    #CONSTANT
    
    @staticmethod
    def is_pass_confrim( password:str, confirm:str) -> bool:
        """returns True if password and its confirm be same
        """
        return password == confirm
    
    def is_pass_lenght_ok(password:str) -> bool:
        return len(password) >= CONSTANTS.MIN_PASS_LENGHT
    


if __name__ == "__main__":
    username = 'amir'
    password = '1234'

    hashed_pass = passwordManager.hash_password(password)
    print('hashed password', hashed_pass)

    input_pass_1 = 'a131'
    print('first input pass is: ', passwordManager.check_password(input_pass_1, hashed_pass))


    input_pass_2 = '1234'
    print('first input pass is: ', passwordManager.check_password(input_pass_2, hashed_pass))

