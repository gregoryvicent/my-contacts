from fastapi import HTTPException
from uuid import uuid4

from src.lib.managefile import ManageFile

class Router:
  __mf = ManageFile()
  __contacs = __mf.read_file()  

  def get_all_contacts(self):
    return self.__contacs

  def get_single_contact(self, id_contact):
    for contact in self.__contacs:
      if id_contact == contact['id']:
        return contact

    raise HTTPException(status_code=404, detail="Contact not found")

  def add_contact(self, new_contact):
    new_contact.id = str(uuid4())
    contact_json = new_contact.dict()

    self.__contacts.append(contact_json)
    self.__mf.write_file(self.__contacts)

    return {
      "success": True,
      "message": "Added new contact"
    }