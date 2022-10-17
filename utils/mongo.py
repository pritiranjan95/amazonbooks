import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["BSamazon"]
collection=db["amazondataBS"]