from fastapi import FastAPI, HTTPException

from src.lib.managefile import ManageFile

app = FastAPI()
mf = ManageFile()

@app.get('/')
def root():
  return {"message": "Hi, Welcome to my API with FastAPI"}

@app.get('/api/contacts')
def get_all_contacts():
  return mf.read_file() 

@app.get('/api/contacts/{id_contact}')
def get_single_contact(id_contact:str):
  contacs = mf.read_file()  
  
  for contac in contacs:
    if id_contact == contac['id']:
      return contac

  raise HTTPException(status_code=404, detail="Contact not found")

@app.post('/api/contacts')
def add_contact(item:str):
  print(item)

@app.put('/api/contacts/{id_contact}')
def update_contact():
  pass

@app.delete('/api/contacts/{id_contact}')
def delete_contact():
  pass