from fastapi import HTTPException

from src.lib.managefile import ManageFile

def get_contact(id_contact):
  mf = ManageFile()
  contacs = mf.read_file()  
  
  for contac in contacs:
    if id_contact == contac['id']:
      return contac

  raise HTTPException(status_code=404, detail="Contact not found")