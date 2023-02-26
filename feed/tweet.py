from bson.objectid import ObjectId

# Import the database module
import sys
sys.path.append('../')
import database


class Tweet:

    # Add
    def add(self, author, content):

        # Add the tweet to the database
        database.tweet.insert_one({"author":author, "content":content})

    # Delete
    def delete(self, id, author):

        # Remove the tweet from the database
        database.tweet.find_one_and_delete({"_id":ObjectId(id), "author":author})