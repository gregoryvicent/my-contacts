from fastapi import HTTPException

from src.lib.managedb import ManageDb

def delete_contact(id_contact):
    md = ManageDb()
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)

            md.write_contact(contacts)

            return {
                "success": True,
                "message": "Deleted Contact"
            }

    raise HTTPException(status_code=404, detail="Contact not Found")


