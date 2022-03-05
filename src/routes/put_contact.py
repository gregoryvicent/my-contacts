from fastapi import HTTPException

from src.lib.managefile import ManageFile

def put_contact(id_contact, contact_up):
  mf = ManageFile()
  contacts = mf.read_file()  
  contact_up = contact_up.dict()

  for index, contact in enumerate(contacts):
    if contact["id"] == id_contact:
      name = contacts[index]["name"] 
      phone = contacts[index]["phone"] 

      contacts[index] = contact_up
      contacts[index]["id"] = contact["id"]

      if contacts[index]["name"] == "":
        contacts[index]["name"] = name 

      if contacts[index]["phone"] == "":
        contacts[index]["phone"] = phone

      mf.write_file(contacts)      

      return {
        "success": True,
        "message": "Updated Contact"
      }

  raise HTTPException(status_code=404, detail="Contact not found")