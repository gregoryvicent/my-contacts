from fastapi import HTTPException

from src.lib.managefile import ManageFile

def delete_contact(id_contact):
  mf = ManageFile()
  contacts = mf.read_file()

  for index, contact in enumerate(contacts):
    if contact["id"] == id_contact:
      contacts.pop(index)

      mf.write_file(contacts)

      return {
        "success": True,
        "message": "Deleted Contact"
      }

  raise HTTPException(status_code=404, detail="Contact not found") 