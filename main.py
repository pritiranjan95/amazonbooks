import imp
from optparse import TitledHelpFormatter
from fastapi import FastAPI
from utils.mongo import collection
from bson.json_util import dumps
from model.books import Bookdetail


app=FastAPI()

@app.get("/")
def search():
    return "Hi there"

@app.get("/{title}")
def search(title:str):

    a= dumps(collection.find({"TITLE":title}))
    return a

@app.post("/newbook")
def add(bookdetail: Bookdetail):
    b= collection.insert_one(bookdetail.__dict__)
    if b:
        return ("A new Book has been upated")

@app.put("/update/{title}")
def update(title:str, bookdetail: Bookdetail):
    prev={"TITLE": title}
    next={"$set":bookdetail.__dict__}
    u= collection.update_one(prev, next)
    if u: 
        return ("Update Successful")

@app.delete("/remove/{title}")
def remove(title: str):
    d= collection.delete_one({"TITLE":title})
    if d:
        return ("Successfull deleted")
     