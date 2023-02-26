from pymongo import MongoClient

# Connect the cluster using the URL
cluster = MongoClient("mongodb+srv://mathieumarin:I6pv5L6W6AKeId3R@cluster0.rlvnt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Get the database and initialize the collections
db = cluster["database"]
user = db["user"]
tweet = db["tweet"]
like = db["like"]