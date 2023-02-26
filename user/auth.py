import bcrypt
from user.user import User
import re

# Import the database module
import sys
sys.path.append('../')
import database


"""
    Signup : Function
"""
def signup(email, username, password):

    # Initialize results
    (res, err) = (False, "")

    # Check if the user inputs exist
    if email and username and password:

        # Check if the email is valid
        if re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$').match(email):

            # Check if the username is valid
            if re.compile('^(?![_.])[a-zA-Z0-9._]+').match(username):

                # Check if the password is valid
                if re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$').match(password):

                    # Check if the email is unique
                    if not database.user.find_one({'email': email}):

                        # Check if the username is unique
                        if not database.user.find_one({'username': username}):

                            # Signup
                            user = User()
                            user.signup(email, username, password)

                            # Update the result
                            res = True

                        else:

                            # Update the error message
                            err ="* Username already exists"

                    else:
                            
                        # Update the error message
                        err ="* Email already exists"

                else:

                    # Update the error message
                    err ="* Password too weak"

            else:

                # Update the error message
                err ="* Invalid username"

        else:

            # Update the error message
            err ="* Invalid email"

    # Return the results
    return (res, err)


"""
    Login : Function
"""
def login(username, password):

    # Initialize results
    (res, err) = (False, "")

    # Check if the user inputs exist
    if username and password:

        # Check if the user inputs exists
        if database.user.find_one({'username': username}):

            # Get the user
            user = database.user.find_one({'username': username})

            # Check if the password is valid
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):

                # Update the result
                res = True

            else:

                # Update the error message
                err ="* Password is incorrect"

        else:

            # Update the error message
            err ="* Username is incorrect"

    # Return the results
    return (res, err)