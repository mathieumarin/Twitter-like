from flask import Blueprint, render_template, request, url_for, redirect, make_response
from user import auth
from feed import event
from feed.like import Like
import datetime

app = Blueprint('user', __name__)


"""
    Root : Function
"""
@app.route('/', methods=['GET', 'POST'])
def root():

    # Get the username and the password
    username = request.cookies.get('username')
    password = request.cookies.get('password')

    # Get the auth results
    (res, err) = auth.login(username, password)

    # Check if the authentification is a success
    if res == True:

        # Redirect to the home page
        return redirect(url_for('user.home'))

    else:

        # Redirect to the signup page
        return redirect(url_for('user.signup'))


"""
    Signup : Function
"""
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    # Check for the request method
    if request.method == 'POST':

        # Get the user inputs
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Signup the user
        (res, err) = auth.signup(email, username, password)

        # Check the signup is a sucess
        if res == True :

            # Redirect to the login page
            return redirect(url_for('user.login'))

        else :

            # Display the error message
            return render_template('signup.html', error=err)
    
    # Display the signup page as default
    return render_template('signup.html')


"""
    Login : Function
"""
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Check for the request method
    if request.method == 'POST':

        # Get the user inputs
        username = request.form.get('username')
        password = request.form.get('password')

        # Login the user
        (res, err) = auth.login(username, password)

        # Check the login is a sucess
        if res == True :

            # Initialize the response redirection
            resp = make_response(redirect(url_for('user.home')))

            # Set the exiration time
            time = datetime.datetime.utcnow() + datetime.timedelta(days=1)

            # Set the cookies
            resp.set_cookie('username', username, expires=time)
            resp.set_cookie('password', password, expires=time)
   
            # Redirect to the home page
            return resp

        else :

            # Display the error message
            return render_template('login.html', error=err)

    # Display the login page as default
    return render_template('login.html')


"""
    Logout : Function
"""
@app.route('/logout', methods=['GET', 'POST'])
def logout():

    # Initialize the response redirection
    resp = make_response(redirect(url_for('user.signup')))

    # Delete the cookies
    resp.delete_cookie('username')
    resp.delete_cookie('password')
   
    # Redirect to the home page
    return resp


"""
    Home : Function
"""
@app.route('/home', methods=['GET', 'POST'])
def home():

    # Get the username
    username = request.cookies.get('username')

    # Check for the request method
    if request.method == 'POST':

        # Get the user input
        content = request.form.get('content')

        # Check the user input
        if len(content) > 75:

            # Display the home page with the error
            return render_template('feed.html', username=username, error='* Tweet must contain less that 75 characters')

        # Add the tweet
        event.add(username, content)

    # Check for the request method
    if request.method == 'GET':

        # Get the ID of the tweet
        id = request.args.get('delete')

        # Check the input
        if id:

            # Delete the tweet
            event.delete(id, username)

            # Redirect to the home page
            return redirect(url_for('user.home'))

        # Reset ID
        id = None

        # Get the ID of the tweet
        id = request.args.get('like')

        # Check the input
        if id:

            # Like the tweet
            event.like(id, username)

            # Redirect to the home page
            return redirect(url_for('user.home'))

    # Get the list of tweet
    tweets = event.getTweets()

    # Initialize the class
    likes = Like()

    # Display the home page as default
    return render_template('feed.html', username=username, tweets=tweets, likes=likes)