
# Import the database module
import sys
sys.path.append('../')
import database


class Like:

    # Like
    def like(self, id, username):

        # Add the like to the database
        database.like.insert_one({"id":id, "username":username})


    # Unlike
    def unlike(self, id, username):

        # Remove the like from the database
        database.like.find_one_and_delete({"id":id, "username":username})


    # Is liked by
    def isLikedBy(self, id, username):

        # Initialize the result
        res = False

        # Check if the given tweet has been liked by the user
        if database.like.find_one({"id":str(id), "username":username}):

            # Update the result
            res = True
        
        # Return the result
        return res


    # Liked by
    def likedBy(self, id):

        # Get the data of the like table
        data = database.like.find().sort('_id', - 1)

        # Initializes the list of likes
        likes = []

        # Search for the likes corresponding to the given ID
        for like in data:

            # Match the like with the ID
            if like['id'] == str(id):

                # Add the username to the list
                likes.append(like['username'])

        # Get the number of likes
        count = len(likes)

        # Initializes the output text
        res = ''

        # One like
        if count == 1:

            # Update the text
            res = 'Liked by ' + likes[0]

        # Two likes
        elif count == 2:

            # Update the text
            res = 'Liked by ' + likes[0] + ' and ' + likes[1]

        # More than two likes
        elif count > 2:

            # Update the text
            res = 'Liked by ' + likes[0] + ', ' + likes[1] + ' and ' + str(count - 2) + ' other'

            # More than three likes
            if count > 3:

                # Update the text
                res += 's'

        # Return the text
        return res