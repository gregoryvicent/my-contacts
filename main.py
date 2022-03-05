from fastapi import FastAPI
from pydantic import BaseModel

from src.routes.get_contacts import get_contacts
from src.routes.get_contact import get_contact
from src.routes.post_contact import post_contact
from src.routes.put_contact import put_contact
from src.routes.delete_contact import delete_contact

app = FastAPI()

class Contact(BaseModel):
  id: str = ""
  name: str
  phone: str

@app.get('/')
def root():
  return {"message": "Hi, Welcome to my API with FastAPI"}

@app.get('/api/contacts')
def get_all_contacts():
  return get_contacts()

@app.get('/api/contacts/{id_contact}')
def get_single_contact(id_contact:str):
  return get_contact(id_contact)

@app.post('/api/contacts')
def add_contact(new_contact:Contact):
  return post_contact(new_contact)

@app.put('/api/contacts/{id_contact}')
def update_contact(id_contact:str, contact_up:Contact):
  return put_contact(id_contact, contact_up)

@app.delete('/api/contacts/{id_contact}')
def remove_contact(id_contact:str):
  return delete_contact(id_contact)