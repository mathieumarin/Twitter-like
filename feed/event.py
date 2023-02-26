from feed.tweet import Tweet
from feed.like import Like

# Import the database module
import sys
sys.path.append('../')
import database


"""
    Add : Function
"""
def add(author, content):

    # Initialize result
    res = False

    # Check the inputs
    if author and content:

        # Add
        tweet = Tweet()
        tweet.add(author, content)

        # Update the result
        res = True

    # Return the result
    return res


"""
    Delete : Function
"""
def delete(id, author):

    # Initialize result
    res = False

    # Check the inputs
    if id and author:

        # Delete
        tweet = Tweet()
        tweet.delete(id, author)

        # Update the result
        res = True

    # Return the result
    return res


"""
    Get tweets : Function
"""
def getTweets():

    # Get and reverse the data list
    data =  database.tweet.find().sort('_id', - 1)

    # Return the data
    return data


"""
    Like : Function
"""
def like(id, username):

    # Initialize result
    res = False

    # Check the inputs
    if id and username:

        # Initialize the class
        like = Like()

        # Check if the user already like
        if database.like.find_one({"id":id, "username":username}):

            # Unlike
            like.unlike(id, username)

        else: 

            # Like
            like.like(id, username)

            # Update the result
            res = True

    # Return the result
    return res