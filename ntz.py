# add your code in this file
import os
import sys
import yaml

#file = /usr/local/bin/notes.yaml
# main function
def cli():
  notes = read_yaml()
  cmd = get_args()
  if len(cmd) == 1:
    for all_keys in notes.keys():
      print_notes(notes, all_keys)
  elif cmd[1] == "r":
    remember(cmd, notes)
  elif cmd[1] == "-c":
    create(cmd, notes)
  elif cmd[1] == "f":
    forget(cmd, notes)
  elif cmd[1] == "e":
    edit(cmd, notes)
  elif cmd[1] == "clear":
    clear(cmd, notes)
  else:
    print("Not a command")
  write_to_file(notes)
  return notes

def remember(input, dict):
  """Adds note to the Remember key

  Input: r new_note
  """
  if len(input) == 3:
    note_new = input[2]
    dict["Remember"].append(note_new)
    print_notes(dict, "Remember")
  else:
    print("Enter in the form: r 'note'")

def create(input, dict):
  """Creates note
  If key not yet created, creates key

  Input: -c key note
  """
  if len(input) == 4:
    key = input[2]
    note_new = input[3]
    if key in dict:
      dict[key].append(note_new)
    else:
      dict[key] = []
      dict[key].append(note_new)
    print_notes(dict, key)
  else:
    print("Enter in the form: -c category 'note'")

def forget(input, dict):
  """Deletes a note

  Input: f key note_rem
  """
  if len(input) == 4:
    key = input[2]
    note_rem = input[3]
    if key in dict:
      if note_rem in dict[key]:
        dict[key].remove(note_rem)
        print_notes(dict, key)
      else:
        print("That note did not exist.")
    else:
      print("That category does not exist.")
  else:
    print("Enter in the form: f category 'note'")

def edit(input, dict):
  """Replaces a note with a new note

  Input: e key note_rem note_new
  """
  if len(input) == 5:
    key = input[2]
    note_rem = input[3]
    new_note = input[4]
    if key in dict:
      if note_rem in dict[key]:
        ind = dict[key].index(note_rem)
        dict[key][ind] = new_note
        print_notes(dict, key)
      else:
        print("That note did not exist in that category")
        print_notes(dict, key)
    else:
      print("That category does not exist.")
  else:
    print("Enter in the form: e category 'note to be removed' 'note to be added'")

def clear(input, dict):
  """Deletes a whole key

  Input: clear key
  """
  if len(input) == 3:
    key = input[2]
    if key in dict:
      del dict[key]
      print("The category " + str(key) + " was deleted.")
    else:
      print("That category does not exist in your notes.")
  else:
    print("Enter in the form: clear category")

def create_file():
  notes = {"Remember": []}
  write_to_file(notes)

def write_to_file(notes):
  """Writes dictionary to yaml file
  """
  with open(r'/usr/local/bin/notes.yaml','w') as file:
    Var = yaml.dump(notes, file)

def read_yaml():
  """Reads yaml file and constructs dictionary
  """
  if os.path.isfile('/usr/local/bin/notes.yaml'):
    notes = dict()
    with open(r'/usr/local/bin/notes.yaml') as file:
      notes_file = yaml.full_load(file)
    for item in notes_file:
      notes[item] = []
      for note in notes_file[item]:
        notes[item].append(note)
  else:
    notes = dict()
    notes["Remember"] = []
  return notes

def print_notes(notes, Category):
  """Prints notes
  """
  print("\n",Category)
  if len(notes[Category]) > 0:
    for index, element in enumerate(notes[Category], start=1):
      print(index, element)
  else:
    print("Empty")
    print("\n")
  
def get_args():
  """Gets arguments from the command line
  """
  return sys.argv
  
# run the main function
#create_file()
cli()

