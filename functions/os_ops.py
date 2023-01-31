# os dependencies
import os
import subprocess as sp

# path 
paths = {
    'notepad': "path",
    'discord': "path",
    'calculator': "path"
}

# function
def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
    sp.Popen(paths['calculator'])
