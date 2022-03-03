import pathlib
import json

class ManageFile:
  __file_path = "{0}/src/db/contacts.json".format(pathlib.Path().absolute())

  def read_file(self):
    with open(self.__file_path, "r") as contacts:
      return json.loads(contacts.read())

  def write_file(self):
    pass