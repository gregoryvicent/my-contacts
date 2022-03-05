from uuid import uuid4

from src.lib.managefile import ManageFile

def post_contact(new_contact):
  mf = ManageFile()
  new_contact.id = str(uuid4())
  contact_json = new_contact.dict()
  contacts = mf.read_file()

  contacts.append(contact_json)
  mf.write_file(contacts)

  return {
    "success": True,
    "message": "Added new contact"
  }