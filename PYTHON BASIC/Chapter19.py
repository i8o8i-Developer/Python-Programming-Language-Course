# ╔═══════════════════════════════════════════════════════════════╗
# ║                   CHAPTER 19: OS MODULE                       ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Directory Operations                                      ║
# ║     - getcwd() - Get Current Directory                        ║
# ║     - chdir() - Change Directory                              ║
# ║     - mkdir() - Create Directory                              ║
# ║     - rmdir() - Remove Directory                              ║
# ║     - listdir() - List Directory Contents                     ║
# ║                                                               ║
# ║  2. File Operations                                           ║
# ║     - remove() - Delete File                                  ║
# ║     - rename() - Rename File                                  ║
# ║                                                               ║
# ║  3. OS Information                                            ║
# ║     - os.name - Operating System Name                         ║
# ║     - os.sep - Path Separator                                 ║
# ║     - os.pathsep - Path Separator                             ║
# ║                                                               ║
# ║  4. File Statistics (os.stat)                                 ║
# ║     - st_size - File Size                                     ║
# ║     - st_mtime - Modification Time                            ║
# ║     - st_atime - Access Time                                  ║
# ║     - st_ctime - Metadata Change Time                         ║
# ║     - st_birthtime - Creation Time                            ║
# ║                                                               ║
# ║  5. Path Operations (os.path)                                 ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Directory Operations
# ═══════════════════════════════════════════════════════════════

# Full OS Module 

import os

# Returns The Current Working Directory
H = os.getcwd()

# Changes The Current Working Directory
os.chdir("")

# Creates A New Directory
os.mkdir("Os-New-Folder")

# Removes A Directory
os.rmdir("Os-New-Folder")

# Removes A File
os.remove("< FileName >")

# Renames A File
os.rename("From",f"To")

# Returns The List Of Files And Folders
os.listdir("< Directory >")

# Return The Name of OS
os.name 
''' (nt) = Windows | & | Linux = (posix)'''

# Return The Directory Separater Used By OS
os.sep
''' (\) = Windows | & | Linux = (/)'''

# Return The Path Separator
os.pathsep
''' (\) = Windows | & | Linux = (/)'''

# Files Descripter
H = os.stat("< FileName >")

# Return The Size Of File
H = os.stat("< FileName >").st_size

# Return The Last Modification Time
H = os.stat("< FileName >").st_mtime

# Return The Last Access Time
H = os.stat("< FileName >").st_atime

# Return The Last MetaData Modification Time
H = os.stat("< FileName >").st_ctime # Since January 1 ,1970

# Return The File Creation Time
H = os.stat("< FileName >").st_birthtime
# In Floating Point Number Since January 1, 1970 (Seconds)

# Absolute Path Joining
Abs_Path1 = "/var/www"
Abs_Path2 = "html"
FileName = "index.html"
Full_Abs_Path = os.path.join(Abs_Path1 , Abs_Path2 , FileName)
# "/var/www/html/index.html"

# Return Boolean If File Exists
os.path.exists("< FileName >")

# Return Boolean If Directory Exists
os.path.isdir("< Directory >")

# Split Path To Head And  Tail
os.path.split("Relative/Path/To/File.txt")
# Output: ('Relative/Path/To', 'File.txt')

# Return The Extension Of File
os.path.splitext("Relative/Path/To/File.txt")
# Output: ('Relative/Path/To/File', '.txt')

# Return The Absolute Path
os.path.abspath("Relative/Path/To/File.txt")
# Output: 'Relative/Path/To/File.txt'

# Return The Base Name
os.path.basename("Relative/Path/To/File.txt")
# Output: 'File.txt'

# Return The Directory Name
os.path.dirname("Relative/Path/To/File.txt")
# Output: 'Relative/Path/To'

# Walk Function # Returns Root , Dir , SubFiles
for Root, Dirs, Files in os.walk('/Path/To/Directory'):
    print(f"Directory : {Root}")
    print(f"SubDirectories : {Dirs}")
    print(f"Files : {Files}")

# Platform Module For System Information
import platform as PlatForm

Uname_Info = PlatForm.uname()
H = (f"System: {Uname_Info.system}")
J = (f"Node Name: {Uname_Info.node}")
K = (f"Release: {Uname_Info.release}")
L = (f"Version: {Uname_Info.version}")
U = (f"Machine: {Uname_Info.machine}")
O = (f"Processor: {Uname_Info.processor}")

# getpass Module
import getpass as GetPass

H = GetPass.getuser()
J = GetPass.getpass("Enter Password : ")
# To Get User Name And Type Hidden Password

# Used To Create Directory And Its Parent Directory
try:
    os.makedirs('Path/To/New/Directory')
except FileExistsError:
    print("Directory Already Exists!")
# Used To Create Directory And Make = ( Its Parent Directory ) If Not Exist
os.makedirs('Path/To/New/Directory', exist_ok=True)



""" SHUTILL MODULE """
import shutil

# Copy File
shutil.copy("Source", "Destination")

# Copy2 Function
shutil.copy2("Source", "Destination")

# Move File
shutil.move("Source", "Destination")

# Copy Directory
shutil.copytree("Source", "Destination")

# Remove Directory
shutil.rmtree("Directory")