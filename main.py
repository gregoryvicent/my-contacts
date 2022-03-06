from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

from src.lib.managedb import ManageDb

class ContactModel(BaseModel):
    id: str = "" 
    name: str
    phone: str

app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI"}

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()

    for contact in contacts:
        if contact["id"] == id_contact:
            return contact

    raise HTTPException(status_code=404, detail="Contact not Found")

@app.post("/api/contacts")
def add_contact(new_contact:ContactModel):
    contacts = md.read_contacts()
    new_contact.id = str(uuid())
    new_contact = new_contact.dict()

    contacts.append(new_contact)
    md.write_contact(contacts)

    return {
        "success": True,
        "message": "Added new Contact"
    }
