from src.lib.managedb import ManageDb

def post_contact(new_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    new_contact = new_contact.dict()

    contacts.append(new_contact)
    md.write_contact(contacts)

    return {
        "success": True,
        "message": "Added new Contact"
    }
