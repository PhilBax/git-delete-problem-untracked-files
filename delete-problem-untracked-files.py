# Simple tool to solve an annoyance in git. Once in a while, when changing
# branches in UE4 -- particularly if the branch is in a different version 
# of UE4 -- I will the following error message:
# 
# "error: The following untracked working tree files would be overwritten by checkout:"
#
# followed by a humongous list of files. Execute this script with the 
# checkout command to have the files automatically deleted.
#
# Example: 
#   python delete-problem-untracked-files.py git checkout my-feature

import sys
import subprocess
import os

# Confirm command
print(sys.argv[1:])

while True:
    # Run the passed-in command. No checks here; this is a debug tool; presume 
    # the user did the right thing
    result = subprocess.run(sys.argv[1:], check=False, stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, universal_newlines=True)

    bDeleting = False
    for line in result.stderr.splitlines():
        # The line before the list starts
        if line == 'error: The following untracked working tree files would '\
            'be overwritten by checkout:':
            bDeleting = True
            continue
        
        # The line after the list is over
        if bDeleting and line == 'Aborting':
            bDeleting = False
            break

        # In the middle of the list; print so the user knows what's going on,
        # then make sure the file exists and delete it
        if bDeleting:
            filename = line.lstrip()
            print("Delete: " + filename)
            if os.path.isfile(filename):
                os.remove(filename)
    
    # If we had an error, run the command again until we're error-free
    if result.returncode == 0:
        break
