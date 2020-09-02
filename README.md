Simple tool to solve an annoyance in git. Once in a while, when changing
branches in UE4 -- particularly if the branch is in a different version 
of UE4 -- I will the following error message:

`error: The following untracked working tree files would be overwritten by checkout:`

followed by a humongous list of files. Execute this script with the 
checkout command to have the files automatically deleted.

### Example: 
  `python delete-problem-untracked-files.py git checkout my-feature`
