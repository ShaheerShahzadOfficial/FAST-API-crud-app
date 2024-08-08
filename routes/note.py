from bson import ObjectId
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntity
notes = APIRouter()


@notes.get("/notes/")
async def get_note():
    docs = conn.notes.notes.find({})
    newDocs = []
    print(newDocs)
    for doc in docs:
        newDocs.append(noteEntity(doc))
    return{
        "docs":newDocs
    }

@notes.post("/notes/")
async def create_note(note: Note):
    
    inserttedNode = conn.notes.notes.insert_one(dict(note))
    print(inserttedNode)
    return {"message": "Note created successfully"}

@notes.put("/notes/{id}")
async def update_note(id: str, note: Note):
    print(note,id)
    note = dict(note)
    conn.notes.notes.update_one({"_id": ObjectId(id)}, {"$set": note})
    return {"message": "Note updated successfully"}

@notes.delete("/notes/{id}")
async def delete_note(id: str):
    conn.notes.notes.delete_one({"_id" : ObjectId(id)})
    return {"message": "Note deleted successfully"}
