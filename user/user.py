import bcrypt

# Import the database module
import sys
sys.path.append('../')
import database


class User:

    # Signup
    def signup(self, email, username, password):

        # Encrypt the password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Add the user to the database
        database.user.insert_one({"email":email, "username":username, "password":hashed})