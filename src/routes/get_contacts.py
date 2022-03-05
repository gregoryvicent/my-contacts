from src.lib.managefile import ManageFile

def get_contacts():
  mf = ManageFile()

  return mf.read_file() 