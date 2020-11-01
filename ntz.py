# add your code in this file
import os
import sys
import yaml

#notes = {"Remember":[]}
# main function
def cli():
  notes = read_yaml()
  #print(notes)
  cmd = get_args()
  if len(cmd) == 1:
    print_notes(notes, "Remember")
  elif cmd[1] == "r":
    #print("Remember")
    new_note = cmd[2]
    print(new_note)
    print(notes["Remember"])
    notes["Remember"].append(cmd[2])
    #print(notes.values())
    print_notes(notes, "Remember")
    write_to_file(notes)
  elif cmd[1] == "-c":
    print("Create")
    if cmd[2] in notes:
      print(notes[cmd])
      notes[cmd[2]].append(cmd[3])
  elif cmd[1] == "f":
    print("Forget")
  elif cmd[1] == "e":
    print("Edit")
  elif cmd[1] == "clear":
    print("Clear")
  else:
    print("Not a command")
  return notes

def write_to_file(notes):
  print("Write to file")
  with open(r'notes.yaml','w') as file:
    Var = yaml.dump(notes, file)

def read_yaml():
  print("Read Loop")
  notes = dict()
  with open(r'notes.yaml') as file:
    notes_file = yaml.full_load(file)
  for item in notes_file:
    print(item)
    notes[item] = []
    for note in notes_file[item]:
      notes[item].append(note)
      print(note)
  return notes
  print("Done Reading File")

"""def remember(notes):
  print("Remember")"""

def print_notes(notes, Category):
  #Doesn't know notes
  #Argument category?
  #print("Remember")
  #if Category == 1
  print("Print Loop")
  print(Category)
  if len(notes) > 0:
    for index, element in enumerate(notes[Category], start=1):
      print(index, element)
  else:
    print("Empty")
  
def get_args():
  return sys.argv
  
# run the main function
cli()

#print(sys.argv[1])