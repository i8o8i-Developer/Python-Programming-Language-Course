# ╔═══════════════════════════════════════════════════════════════╗
# ║                 CHAPTER 23: OS MODULE                         ║
# ║          File System Operations & Path Manipulation           ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
┌─────────────────────────────────────────────────────────────────┐
│                     TABLE OF CONTENTS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Introduction To OS Module                                   │
│     ├─ What Is OS Module?                                       │
│     ├─ Importing OS Module                                      │
│     └─ Platform-Independent Operations                          │
│                                                                 │
│  2. Path Operations (os.path)                                   │
│     ├─ os.path.join() - Join Path Components                    │
│     ├─ os.path.dirname() - Get Directory Name                   │
│     ├─ os.path.basename() - Get File Name                       │
│     ├─ os.path.split() - Split Path                             │
│     ├─ os.path.splitext() - Split Extension                     │
│     ├─ os.path.abspath() - Get Absolute Path                    │
│     ├─ os.path.relpath() - Get Relative Path                    │
│     ├─ os.path.normpath() - Normalize Path                      │
│     └─ os.path.realpath() - Resolve Symbolic Links              │
│                                                                 │
│  3. Path Checking Functions                                     │
│     ├─ os.path.exists() - Check If Path Exists                  │
│     ├─ os.path.isfile() - Check If File                         │
│     ├─ os.path.isdir() - Check If Directory                     │
│     ├─ os.path.isabs() - Check If Absolute Path                 │
│     ├─ os.path.islink() - Check If Symbolic Link                │
│     └─ os.path.ismount() - Check If Mount Point                 │
│                                                                 │
│  4. File And Directory Information                              │
│     ├─ os.path.getsize() - Get File Size                        │
│     ├─ os.path.getmtime() - Get Modification Time               │
│     ├─ os.path.getatime() - Get Access Time                     │
│     ├─ os.path.getctime() - Get Creation Time                   │
│     └─ os.stat() - Complete File Stats                          │
│                                                                 │
│  5. Directory Operations                                        │
│     ├─ os.getcwd() - Get Current Working Directory              │
│     ├─ os.chdir() - Change Directory                            │
│     ├─ os.listdir() - List Directory Contents                   │
│     ├─ os.mkdir() - Create Single Directory                     │
│     ├─ os.makedirs() - Create Nested Directories                │
│     ├─ os.rmdir() - Remove Empty Directory                      │
│     ├─ os.removedirs() - Remove Nested Empty Directories        │
│     └─ os.walk() - Recursive Directory Traversal                │
│                                                                 │
│  6. File Operations                                             │
│     ├─ os.rename() - Rename File/Directory                      │
│     ├─ os.renames() - Rename With Directory Creation            │
│     ├─ os.remove() - Delete File                                │
│     ├─ os.unlink() - Delete File (Alias)                        │
│     └─ os.replace() - Replace File Atomically                   │
│                                                                 │
│  7. Environment Variables                                       │
│     ├─ os.environ - Environment Dictionary                      │
│     ├─ os.getenv() - Get Environment Variable                   │
│     ├─ os.putenv() - Set Environment Variable                   │
│     ├─ os.unsetenv() - Remove Environment Variable              │
│     └─ Working With .env Files                                  │
│                                                                 │
│  8. Special Variables And Constants                             │
│     ├─ __file__ - Current Script Path                           │
│     ├─ os.sep - Path Separator                                  │
│     ├─ os.pathsep - PATH Separator                              │
│     ├─ os.linesep - Line Separator                              │
│     ├─ os.name - Operating System Name                          │
│     └─ os.curdir And os.pardir                                  │
│                                                                 │
│  9. Process Management                                          │
│     ├─ os.getpid() - Get Process ID                             │
│     ├─ os.getppid() - Get Parent Process ID                     │
│     ├─ os.system() - Execute System Command                     │
│     └─ os.popen() - Open Pipe To/From Command                   │
│                                                                 │
│  10. Absolute Vs Relative Paths                                 │
│      ├─ Understanding Path Types                                │
│      ├─ Converting Between Path Types                           │
│      ├─ Best Practices                                          │
│      └─ Cross-Platform Considerations                           │
│                                                                 │
│  11. Advanced Path Patterns                                     │
│      ├─ Building Project Paths                                  │
│      ├─ Config File Locations                                   │
│      ├─ .env File Loading Pattern                               │
│      ├─ Dynamic Path Construction                               │
│      └─ Error Handling For Paths                                │
│                                                                 │
│  12. Real-World Examples                                        │
│      ├─ Project Structure Navigation                            │
│      ├─ Configuration File Management                           │
│      ├─ Log File Organization                                   │
│      ├─ Backup And Archive Paths                                │
│      └─ Cross-Platform Script Development                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════
# 1. INTRODUCTION TO OS MODULE
# ═══════════════════════════════════════════════════════════════

"""
The OS Module Provides A Portable Way Of Using Operating System 
Dependent Functionality. It Allows You To Interface With The 
Underlying Operating System That Python Is Running On.

Key Features:
✓ File And Directory Manipulation
✓ Path Operations
✓ Environment Variables
✓ Process Management
✓ Cross-Platform Compatibility
"""

# Importing OS Module
import os
import logging
from datetime import datetime

print("=" * 70)
print("CHAPTER 23: OS MODULE - FILE SYSTEM & PATH OPERATIONS")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════
# 2. PATH OPERATIONS (os.path)
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("2. PATH OPERATIONS (os.path)")
print("─" * 70)

# os.path.join() - Join Path Components
# Joins One Or More Path Components Intelligently
print("\n✓ os.path.join() - Join Path Components")
Path1 = os.path.join("folder", "subfolder", "file.txt")
print(f"  Joined Path: {Path1}")

Path2 = os.path.join("h:", "PYTHON COURSE", "PYTHON BASIC")
print(f"  Project Path: {Path2}")

# Cross-Platform Path Joining
ConfigPath = os.path.join(os.getcwd(), "config", "settings.ini")
print(f"  Config Path: {ConfigPath}")

# os.path.dirname() - Get Directory Name
# Returns The Directory Component Of A Pathname
print("\n✓ os.path.dirname() - Get Directory Name")
FilePath = "H:\\PYTHON COURSE\\PYTHON BASIC\\Chapter23.py"
DirName = os.path.dirname(FilePath)
print(f"  File Path: {FilePath}")
print(f"  Directory: {DirName}")

# Using With __file__
CurrentDir = os.path.dirname(__file__)
print(f"  Current Script Directory: {CurrentDir}")

# os.path.basename() - Get File Name
# Returns The Final Component Of A Pathname
print("\n✓ os.path.basename() - Get File Name")
FileName = os.path.basename(FilePath)
print(f"  File Name: {FileName}")

URLPath = "/home/user/documents/report.pdf"
print(f"  Unix File Name: {os.path.basename(URLPath)}")

# os.path.split() - Split Path Into Directory And File
print("\n✓ os.path.split() - Split Path")
Directory, File = os.path.split(FilePath)
print(f"  Original: {FilePath}")
print(f"  Directory: {Directory}")
print(f"  File: {File}")

# os.path.splitext() - Split Extension
print("\n✓ os.path.splitext() - Split Extension")
Name, Extension = os.path.splitext("document.pdf")
print(f"  File Name: {Name}")
print(f"  Extension: {Extension}")

# Multiple Extensions
FullName, Ext = os.path.splitext("archive.tar.gz")
print(f"  Archive Name: {FullName}")
print(f"  Extension: {Ext}")

# os.path.abspath() - Get Absolute Path
# Returns The Absolute Version Of A Path
print("\n✓ os.path.abspath() - Get Absolute Path")
RelativePath = "OuputFolder/Text.txt"
AbsolutePath = os.path.abspath(RelativePath)
print(f"  Relative Path: {RelativePath}")
print(f"  Absolute Path: {AbsolutePath}")

# os.path.relpath() - Get Relative Path
# Returns A Relative Filepath To Path From Start Directory
print("\n✓ os.path.relpath() - Get Relative Path")
Target = "h:\\PYTHON COURSE\\PYTHON BASIC\\OuputFolder"
Start = "h:\\PYTHON COURSE"
RelPath = os.path.relpath(Target, Start)
print(f"  Target: {Target}")
print(f"  Start: {Start}")
print(f"  Relative Path: {RelPath}")

# os.path.normpath() - Normalize Path
# Normalizes A Pathname By Collapsing Redundant Separators
print("\n✓ os.path.normpath() - Normalize Path")
MessyPath = "folder//subfolder\\.\\file.txt"
CleanPath = os.path.normpath(MessyPath)
print(f"  Messy Path: {MessyPath}")
print(f"  Clean Path: {CleanPath}")

# os.path.realpath() - Resolve Symbolic Links
# Returns The Canonical Path, Eliminating Symbolic Links
print("\n✓ os.path.realpath() - Resolve Symbolic Links")
RealPath = os.path.realpath(__file__)
print(f"  Real Path Of Current File: {RealPath}")

# ═══════════════════════════════════════════════════════════════
# 3. PATH CHECKING FUNCTIONS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("3. PATH CHECKING FUNCTIONS")
print("─" * 70)

# os.path.exists() - Check If Path Exists
print("\n✓ os.path.exists() - Check If Path Exists")
TestPath1 = "Chapter23.py"
TestPath2 = "NonExistent.txt"
print(f"  '{TestPath1}' Exists: {os.path.exists(TestPath1)}")
print(f"  '{TestPath2}' Exists: {os.path.exists(TestPath2)}")

# os.path.isfile() - Check If Path Is A File
print("\n✓ os.path.isfile() - Check If File")
print(f"  'Chapter23.py' Is File: {os.path.isfile('Chapter23.py')}")
print(f"  'OuputFolder' Is File: {os.path.isfile('OuputFolder')}")

# os.path.isdir() - Check If Path Is A Directory
print("\n✓ os.path.isdir() - Check If Directory")
print(f"  'OuputFolder' Is Directory: {os.path.isdir('OuputFolder')}")
print(f"  'Chapter23.py' Is Directory: {os.path.isdir('Chapter23.py')}")

# os.path.isabs() - Check If Absolute Path
print("\n✓ os.path.isabs() - Check If Absolute Path")
print(f"  'h:\\PYTHON COURSE' Is Absolute: {os.path.isabs('h:\\PYTHON COURSE')}")
print(f"  'folder/file.txt' Is Absolute: {os.path.isabs('folder/file.txt')}")

# os.path.islink() - Check If Symbolic Link (Unix/Linux)
print("\n✓ os.path.islink() - Check If Symbolic Link")
print(f"  Checking For Symbolic Links...")
# Note: Rarely Used On Windows

# ═══════════════════════════════════════════════════════════════
# 4. FILE AND DIRECTORY INFORMATION
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("4. FILE AND DIRECTORY INFORMATION")
print("─" * 70)

# os.path.getsize() - Get File Size In Bytes
print("\n✓ os.path.getsize() - Get File Size")
if os.path.exists("Chapter23.py"):
    Size = os.path.getsize("Chapter23.py")
    print(f"  File Size: {Size} Bytes ({Size / 1024:.2f} KB)")

# os.path.getmtime() - Get Modification Time
print("\n✓ os.path.getmtime() - Get Modification Time")
if os.path.exists("Chapter23.py"):
    ModTime = os.path.getmtime("Chapter23.py")
    ModDateTime = datetime.fromtimestamp(ModTime)
    print(f"  Last Modified: {ModDateTime}")

# os.path.getatime() - Get Access Time
print("\n✓ os.path.getatime() - Get Access Time")
if os.path.exists("Chapter23.py"):
    AccessTime = os.path.getatime("Chapter23.py")
    AccessDateTime = datetime.fromtimestamp(AccessTime)
    print(f"  Last Accessed: {AccessDateTime}")

# os.path.getctime() - Get Creation Time
print("\n✓ os.path.getctime() - Get Creation Time")
if os.path.exists("Chapter23.py"):
    CreateTime = os.path.getctime("Chapter23.py")
    CreateDateTime = datetime.fromtimestamp(CreateTime)
    print(f"  Created: {CreateDateTime}")

# os.stat() - Complete File Statistics
print("\n✓ os.stat() - Complete File Stats")
if os.path.exists("Chapter23.py"):
    Stats = os.stat("Chapter23.py")
    print(f"  Size: {Stats.st_size} Bytes")
    print(f"  Modified: {datetime.fromtimestamp(Stats.st_mtime)}")
    print(f"  Accessed: {datetime.fromtimestamp(Stats.st_atime)}")
    print(f"  Created: {datetime.fromtimestamp(Stats.st_ctime)}")

# ═══════════════════════════════════════════════════════════════
# 5. DIRECTORY OPERATIONS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("5. DIRECTORY OPERATIONS")
print("─" * 70)

# os.getcwd() - Get Current Working Directory
print("\n✓ os.getcwd() - Get Current Working Directory")
CurrentWorkingDir = os.getcwd()
print(f"  Current Directory: {CurrentWorkingDir}")

# os.chdir() - Change Directory
print("\n✓ os.chdir() - Change Directory")
OriginalDir = os.getcwd()
print(f"  Original Directory: {OriginalDir}")
# Note: Commenting Out To Avoid Changing Directory
# os.chdir("OuputFolder")
# print(f"  New Directory: {os.getcwd()}")
# os.chdir(OriginalDir)  # Change Back

# os.listdir() - List Directory Contents
print("\n✓ os.listdir() - List Directory Contents")
if os.path.exists("OuputFolder"):
    Contents = os.listdir("OuputFolder")
    print(f"  Contents Of 'OuputFolder': {len(Contents)} Items")
    for Item in Contents[:5]:  # Show First 5
        print(f"    - {Item}")

# os.mkdir() - Create Single Directory
print("\n✓ os.mkdir() - Create Single Directory")
print("  Example: os.mkdir('NewFolder')")
# Note: Not Actually Creating To Avoid Side Effects

# os.makedirs() - Create Nested Directories
print("\n✓ os.makedirs() - Create Nested Directories")
print("  Example: os.makedirs('Parent/Child/GrandChild', exist_ok=True)")
# exist_ok=True Prevents Error If Directory Already Exists

# os.rmdir() - Remove Empty Directory
print("\n✓ os.rmdir() - Remove Empty Directory")
print("  Example: os.rmdir('EmptyFolder')")
# Only Works On Empty Directories

# os.removedirs() - Remove Nested Empty Directories
print("\n✓ os.removedirs() - Remove Nested Empty Directories")
print("  Example: os.removedirs('Parent/Child/GrandChild')")
# Removes Directories Recursively If Empty

# os.walk() - Recursive Directory Traversal
print("\n✓ os.walk() - Recursive Directory Traversal")
print("  Walking Through Directory Tree...")
Count = 0
for Root, Dirs, Files in os.walk("."):
    if Count < 2:  # Show First 2 Levels
        print(f"  Directory: {Root}")
        print(f"    Subdirectories: {len(Dirs)}")
        print(f"    Files: {len(Files)}")
        Count += 1

# ═══════════════════════════════════════════════════════════════
# 6. FILE OPERATIONS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("6. FILE OPERATIONS")
print("─" * 70)

# os.rename() - Rename File Or Directory
print("\n✓ os.rename() - Rename File/Directory")
print("  Example: os.rename('OldName.txt', 'NewName.txt')")

# os.renames() - Rename With Directory Creation
print("\n✓ os.renames() - Rename With Directory Creation")
print("  Example: os.renames('old.txt', 'NewFolder/new.txt')")
# Creates Intermediate Directories If Needed

# os.remove() - Delete File
print("\n✓ os.remove() - Delete File")
print("  Example: os.remove('TempFile.txt')")

# os.unlink() - Delete File (Alias For os.remove)
print("\n✓ os.unlink() - Delete File (Alias)")
print("  Example: os.unlink('TempFile.txt')")

# os.replace() - Replace File Atomically
print("\n✓ os.replace() - Replace File Atomically")
print("  Example: os.replace('Source.txt', 'Destination.txt')")
# Atomic Operation, Overwrites Destination

# ═══════════════════════════════════════════════════════════════
# 7. ENVIRONMENT VARIABLES
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("7. ENVIRONMENT VARIABLES")
print("─" * 70)

# os.environ - Environment Dictionary
print("\n✓ os.environ - Environment Dictionary")
print(f"  Total Environment Variables: {len(os.environ)}")
print("\n  Sample Environment Variables:")
for Key in list(os.environ.keys())[:3]:
    print(f"    {Key} = {os.environ[Key][:50]}...")  # Truncate Long Values

# os.getenv() - Get Environment Variable
print("\n✓ os.getenv() - Get Environment Variable")
UserName = os.getenv("USERNAME", "Unknown")
print(f"  USERNAME: {UserName}")

# Get With Default Value
DatabaseURL = os.getenv("DATABASE_URL", "sqlite:///default.db")
print(f"  DATABASE_URL: {DatabaseURL}")

# os.putenv() - Set Environment Variable (For Child Processes)
print("\n✓ os.putenv() - Set Environment Variable")
print("  Example: os.putenv('MY_VAR', 'MyValue')")
# Note: Changes Only Affect Child Processes

# Setting In os.environ (Preferred Method)
os.environ["CUSTOM_VAR"] = "CustomValue"
print(f"  Set CUSTOM_VAR: {os.environ.get('CUSTOM_VAR')}")

# Working With .env Files
print("\n✓ Working With .env Files")
print("  .env Files Store Environment Configuration")

# Example Pattern For Loading .env File
try:
    from dotenv import load_dotenv
    
    # Pattern 1: Load .env From Current Directory
    load_dotenv()
    
    # Pattern 2: Load .env From Specific Path
    EnvPath = os.path.join(os.path.dirname(__file__), "Utils", ".env")
    if os.path.exists(EnvPath):
        load_dotenv(dotenv_path=EnvPath)
        print(f"  ✓ .env Loaded From: {EnvPath}")
    else:
        logging.warning(f"  ⚠ .env File Not Found At {EnvPath}")
    
    # Pattern 3: Load From Parent Directory
    ParentEnv = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(ParentEnv):
        load_dotenv(dotenv_path=ParentEnv)
        print(f"  ✓ Parent .env Loaded From: {ParentEnv}")
        
except ImportError:
    print("  ℹ python-dotenv Not Installed")
    print("  Install: pip install python-dotenv")

# ═══════════════════════════════════════════════════════════════
# 8. SPECIAL VARIABLES AND CONSTANTS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("8. SPECIAL VARIABLES AND CONSTANTS")
print("─" * 70)

# __file__ - Current Script Path
print("\n✓ __file__ - Current Script Path")
print(f"  __file__: {__file__}")
print(f"  Absolute: {os.path.abspath(__file__)}")
print(f"  Directory: {os.path.dirname(os.path.abspath(__file__))}")

# os.sep - Path Separator
print("\n✓ os.sep - Path Separator")
print(f"  Path Separator: '{os.sep}'")
print(f"  Example Path: folder{os.sep}subfolder{os.sep}file.txt")

# os.pathsep - PATH Environment Variable Separator
print("\n✓ os.pathsep - PATH Separator")
print(f"  PATH Separator: '{os.pathsep}'")
print(f"  Example: C:{os.pathsep}D:{os.pathsep}E:")

# os.linesep - Line Separator
print("\n✓ os.linesep - Line Separator")
print(f"  Line Separator: {repr(os.linesep)}")

# os.name - Operating System Name
print("\n✓ os.name - Operating System Name")
print(f"  OS Name: {os.name}")
# 'nt' For Windows, 'posix' For Unix/Linux/Mac

# os.curdir And os.pardir
print("\n✓ os.curdir And os.pardir")
print(f"  Current Directory Symbol: '{os.curdir}'")  # '.'
print(f"  Parent Directory Symbol: '{os.pardir}'")   # '..'

# ═══════════════════════════════════════════════════════════════
# 9. PROCESS MANAGEMENT
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("9. PROCESS MANAGEMENT")
print("─" * 70)

# os.getpid() - Get Process ID
print("\n✓ os.getpid() - Get Process ID")
ProcessID = os.getpid()
print(f"  Current Process ID: {ProcessID}")

# os.getppid() - Get Parent Process ID
print("\n✓ os.getppid() - Get Parent Process ID")
ParentPID = os.getppid()
print(f"  Parent Process ID: {ParentPID}")

# os.system() - Execute System Command
print("\n✓ os.system() - Execute System Command")
print("  Example: os.system('dir') Or os.system('ls')")
# Returns Exit Code

# os.popen() - Open Pipe To/From Command
print("\n✓ os.popen() - Open Pipe To/From Command")
print("  Example: os.popen('dir').read()")
# Note: subprocess Module Is Preferred For New Code

# ═══════════════════════════════════════════════════════════════
# 10. ABSOLUTE VS RELATIVE PATHS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("10. ABSOLUTE VS RELATIVE PATHS")
print("─" * 70)

print("\n✓ Understanding Path Types")

# Absolute Path
AbsPath = "h:\\PYTHON COURSE\\PYTHON BASIC\\Chapter23.py"
print(f"\n  Absolute Path Example:")
print(f"    {AbsPath}")
print(f"    - Complete Path From Root")
print(f"    - Not Dependent On Current Directory")
print(f"    - Is Absolute: {os.path.isabs(AbsPath)}")

# Relative Path
RelPath = "OuputFolder/Text.txt"
print(f"\n  Relative Path Example:")
print(f"    {RelPath}")
print(f"    - Relative To Current Directory")
print(f"    - Shorter And More Portable")
print(f"    - Is Absolute: {os.path.isabs(RelPath)}")

# Converting Between Path Types
print("\n✓ Converting Between Path Types")
print(f"  Relative To Absolute: {os.path.abspath(RelPath)}")
print(f"  Absolute To Relative: {os.path.relpath(AbsPath)}")

# Best Practices
print("\n✓ Best Practices")
print("  1. Use Relative Paths For Project Files")
print("  2. Use Absolute Paths For System Resources")
print("  3. Always Use os.path.join() For Path Construction")
print("  4. Use __file__ For Script-Relative Paths")

# Cross-Platform Considerations
print("\n✓ Cross-Platform Considerations")
print(f"  Current OS: {os.name}")
print("  Always Use os.path.join() Instead Of Manual Concatenation")
print("  Avoid Hardcoded \\ Or / - Use os.sep")

# ═══════════════════════════════════════════════════════════════
# 11. ADVANCED PATH PATTERNS
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("11. ADVANCED PATH PATTERNS")
print("─" * 70)

# Building Project Paths
print("\n✓ Building Project Paths")

# Get Script Directory
ScriptDir = os.path.dirname(os.path.abspath(__file__))
print(f"  Script Directory: {ScriptDir}")

# Get Project Root (Assuming Script Is In PYTHON BASIC Folder)
ProjectRoot = os.path.dirname(ScriptDir)
print(f"  Project Root: {ProjectRoot}")

# Build Paths Relative To Script
OutputFolder = os.path.join(ScriptDir, "OuputFolder")
print(f"  Output Folder: {OutputFolder}")

ConfigFile = os.path.join(ScriptDir, "config.ini")
print(f"  Config File Path: {ConfigFile}")

# Config File Location Patterns
print("\n✓ Config File Location Patterns")

# Pattern 1: Same Directory As Script
ConfigPath1 = os.path.join(os.path.dirname(__file__), "config.ini")
print(f"  Pattern 1 (Same Dir): {ConfigPath1}")

# Pattern 2: Config Subfolder
ConfigPath2 = os.path.join(os.path.dirname(__file__), "config", "settings.ini")
print(f"  Pattern 2 (Config Folder): {ConfigPath2}")

# Pattern 3: Parent Directory Config
ConfigPath3 = os.path.join(os.path.dirname(__file__), "..", "config.ini")
print(f"  Pattern 3 (Parent Dir): {ConfigPath3}")

# Pattern 4: User Home Directory
HomeConfig = os.path.join(os.path.expanduser("~"), ".myapp", "config.ini")
print(f"  Pattern 4 (Home Dir): {HomeConfig}")

# .env File Loading Pattern (Complete Example)
print("\n✓ .env File Loading Pattern")

def LoadEnvironmentFile(EnvFileName=".env"):
    """
    Comprehensive .env File Loading Function
    Searches Multiple Locations In Order Of Priority
    """
    SearchPaths = [
        # 1. Same Directory As Script
        os.path.join(os.path.dirname(__file__), EnvFileName),
        
        # 2. Utils Subfolder
        os.path.join(os.path.dirname(__file__), "Utils", EnvFileName),
        
        # 3. Config Subfolder
        os.path.join(os.path.dirname(__file__), "config", EnvFileName),
        
        # 4. Parent Directory
        os.path.join(os.path.dirname(__file__), "..", EnvFileName),
        
        # 5. Project Root
        os.path.join(os.path.dirname(os.path.dirname(__file__)), EnvFileName),
    ]
    
    for EnvPath in SearchPaths:
        NormalizedPath = os.path.normpath(EnvPath)
        if os.path.exists(NormalizedPath):
            print(f"  ✓ Found .env At: {NormalizedPath}")
            try:
                from dotenv import load_dotenv
                load_dotenv(dotenv_path=NormalizedPath)
                return NormalizedPath
            except ImportError:
                print("  ℹ python-dotenv Not Installed")
                return None
    
    print(f"  ⚠ .env File Not Found In Any Search Location")
    return None

# Execute The Function
LoadedEnvPath = LoadEnvironmentFile()

# Dynamic Path Construction
print("\n✓ Dynamic Path Construction")

# Build Path Based On OS
if os.name == "nt":  # Windows
    DataPath = os.path.join("C:", "ProgramData", "MyApp", "data.db")
else:  # Unix/Linux/Mac
    DataPath = os.path.join("/var", "lib", "myapp", "data.db")

print(f"  OS-Specific Data Path: {DataPath}")

# Build Path With Date
Today = datetime.now().strftime("%Y-%m-%d")
LogPath = os.path.join(ScriptDir, "logs", f"log_{Today}.txt")
print(f"  Dynamic Log Path: {LogPath}")

# Build Path With Environment Variable
UserProfile = os.getenv("USERPROFILE", os.path.expanduser("~"))
UserDataPath = os.path.join(UserProfile, "AppData", "Local", "MyApp")
print(f"  User Data Path: {UserDataPath}")

# Error Handling For Paths
print("\n✓ Error Handling For Paths")

def SafePathOperation(FilePath):
    """
    Safely Perform Path Operations With Error Handling
    """
    try:
        # Normalize Path
        NormalizedPath = os.path.normpath(FilePath)
        
        # Check If Path Exists
        if not os.path.exists(NormalizedPath):
            print(f"  ⚠ Path Does Not Exist: {NormalizedPath}")
            return False
        
        # Check If It's A File
        if os.path.isfile(NormalizedPath):
            Size = os.path.getsize(NormalizedPath)
            print(f"  ✓ File Exists: {NormalizedPath} ({Size} Bytes)")
            return True
        
        # Check If It's A Directory
        elif os.path.isdir(NormalizedPath):
            Count = len(os.listdir(NormalizedPath))
            print(f"  ✓ Directory Exists: {NormalizedPath} ({Count} Items)")
            return True
            
    except PermissionError:
        print(f"  ✗ Permission Denied: {FilePath}")
        return False
    except OSError as E:
        print(f"  ✗ OS Error: {E}")
        return False

# Test The Function
SafePathOperation("Chapter23.py")
SafePathOperation("OuputFolder")

# ═══════════════════════════════════════════════════════════════
# 12. REAL-WORLD EXAMPLES
# ═══════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("12. REAL-WORLD EXAMPLES")
print("─" * 70)

# Example 1: Project Structure Navigation
print("\n✓ Example 1: Project Structure Navigation")

class ProjectPaths:
    """Centralized Project Path Management"""
    
    def __init__(self):
        # Get The Directory Where This Script Is Located
        self.ScriptDir = os.path.dirname(os.path.abspath(__file__))
        
        # Project Root (Parent Of Script Directory)
        self.ProjectRoot = os.path.dirname(self.ScriptDir)
        
        # Common Project Folders
        self.OutputDir = os.path.join(self.ScriptDir, "OuputFolder")
        self.ConfigDir = os.path.join(self.ScriptDir, "config")
        self.LogsDir = os.path.join(self.ScriptDir, "logs")
        self.DataDir = os.path.join(self.ScriptDir, "data")
    
    def GetOutputPath(self, FileName):
        """Get Full Path For Output File"""
        return os.path.join(self.OutputDir, FileName)
    
    def GetConfigPath(self, FileName):
        """Get Full Path For Config File"""
        return os.path.join(self.ConfigDir, FileName)
    
    def GetLogPath(self, FileName):
        """Get Full Path For Log File"""
        return os.path.join(self.LogsDir, FileName)
    
    def EnsureDirectories(self):
        """Create All Project Directories If They Don't Exist"""
        for Directory in [self.OutputDir, self.ConfigDir, self.LogsDir, self.DataDir]:
            if not os.path.exists(Directory):
                print(f"  Creating: {Directory}")
                # os.makedirs(Directory, exist_ok=True)
            else:
                print(f"  Exists: {Directory}")

# Use The Class
Paths = ProjectPaths()
print(f"  Output File Path: {Paths.GetOutputPath('result.txt')}")
print(f"  Config File Path: {Paths.GetConfigPath('settings.ini')}")
Paths.EnsureDirectories()

# Example 2: Configuration File Management
print("\n✓ Example 2: Configuration File Management")

def LoadConfiguration():
    """
    Load Configuration From Multiple Possible Locations
    Priority: Local > User > System
    """
    ConfigLocations = [
        # 1. Local Directory (Highest Priority)
        os.path.join(os.getcwd(), "config.ini"),
        
        # 2. Script Directory
        os.path.join(os.path.dirname(__file__), "config.ini"),
        
        # 3. User Home Directory
        os.path.join(os.path.expanduser("~"), ".myapp", "config.ini"),
        
        # 4. System-Wide (Windows)
        os.path.join("C:", "ProgramData", "MyApp", "config.ini") if os.name == "nt" else None,
        
        # 4. System-Wide (Unix/Linux)
        "/etc/myapp/config.ini" if os.name != "nt" else None,
    ]
    
    # Remove None Values
    ConfigLocations = [Loc for Loc in ConfigLocations if Loc]
    
    for ConfigPath in ConfigLocations:
        if os.path.exists(ConfigPath):
            print(f"  ✓ Loading Config From: {ConfigPath}")
            return ConfigPath
    
    print("  ⚠ No Configuration File Found")
    return None

LoadConfiguration()

# Example 3: Log File Organization
print("\n✓ Example 3: Log File Organization")

def CreateLogPath():
    """
    Create Organized Log File Path With Date And Time
    """
    # Get Script Directory
    ScriptDir = os.path.dirname(os.path.abspath(__file__))
    
    # Create Logs Folder Path
    LogsFolder = os.path.join(ScriptDir, "logs")
    
    # Create Date-Based Subfolder
    Today = datetime.now().strftime("%Y-%m")
    DateFolder = os.path.join(LogsFolder, Today)
    
    # Create Log Filename With Timestamp
    Timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    LogFileName = f"app_log_{Timestamp}.txt"
    
    # Full Log Path
    LogPath = os.path.join(DateFolder, LogFileName)
    
    print(f"  Log Path: {LogPath}")
    print(f"  Would Create: {DateFolder}")
    
    return LogPath

CreateLogPath()

# Example 4: Backup And Archive Paths
print("\n✓ Example 4: Backup And Archive Paths")

def CreateBackupPath(OriginalFile):
    """
    Create Backup Path With Timestamp
    """
    if not os.path.exists(OriginalFile):
        print(f"  ⚠ Original File Not Found: {OriginalFile}")
        return None
    
    # Get File Components
    Directory = os.path.dirname(OriginalFile)
    FileName = os.path.basename(OriginalFile)
    Name, Extension = os.path.splitext(FileName)
    
    # Create Backup Filename
    Timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    BackupFileName = f"{Name}_backup_{Timestamp}{Extension}"
    
    # Create Backup Path
    BackupPath = os.path.join(Directory, "backups", BackupFileName)
    
    print(f"  Original: {OriginalFile}")
    print(f"  Backup: {BackupPath}")
    
    return BackupPath

CreateBackupPath("Chapter23.py")

# Example 5: Cross-Platform Script Development
print("\n✓ Example 5: Cross-Platform Script Development")

def GetPlatformSpecificPath(AppName):
    """
    Get Platform-Specific Application Data Path
    """
    if os.name == "nt":  # Windows
        BaseDir = os.getenv("APPDATA", os.path.expanduser("~"))
        AppDataPath = os.path.join(BaseDir, AppName)
    else:  # Unix/Linux/Mac
        HomeDir = os.path.expanduser("~")
        AppDataPath = os.path.join(HomeDir, f".{AppName.lower()}")
    
    print(f"  Platform: {os.name}")
    print(f"  App Data Path: {AppDataPath}")
    
    return AppDataPath

GetPlatformSpecificPath("MyApplication")

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("CHAPTER 23 SUMMARY: OS MODULE MASTERY")
print("═" * 70)

print("""
Key Takeaways:

✓ OS Module Basics
  - Platform-independent file system operations
  - Import with 'import os'
  - Essential for path manipulation and file handling

✓ Path Operations (os.path)
  - join(): Combine path components safely
  - dirname() & basename(): Extract path parts
  - abspath() & relpath(): Convert path types
  - exists(), isfile(), isdir(): Check paths

✓ Directory Operations
  - getcwd(): Get current directory
  - listdir(): List directory contents
  - makedirs(): Create directory trees
  - walk(): Recursive directory traversal

✓ File Operations
  - rename(), remove(): Modify files
  - stat(): Get file information
  - getsize(), getmtime(): File metadata

✓ Environment Variables
  - os.environ: Access environment dictionary
  - getenv(): Get variable with default
  - Load .env files with python-dotenv

✓ Special Variables
  - __file__: Current script path
  - os.sep: Path separator (/ or \\)
  - os.name: Operating system identifier

✓ Absolute Vs Relative Paths
  - Absolute: Full path from root
  - Relative: Path from current directory
  - Use os.path.join() for portability

✓ Best Practices
  - Always use os.path.join() for paths
  - Handle errors with try/except
  - Use __file__ for script-relative paths
  - Check existence before operations
  - Normalize paths with os.path.normpath()

✓ Real-World Patterns
  - Project structure management
  - Configuration file loading
  - Log file organization
  - Backup path creation
  - Cross-platform compatibility

Common Use Cases:
1. Building project-relative paths
2. Loading configuration files
3. Creating organized directory structures
4. Managing environment variables
5. Cross-platform file operations

Remember:
- OS module is essential for file system interaction
- Path operations prevent platform-specific issues
- Always validate paths before operations
- Use modern pathlib for new projects (Python 3.4+)
- Combine with __file__ for portable scripts

Next Steps:
- Explore pathlib module (modern alternative)
- Learn subprocess module for process management
- Study shutil for high-level file operations
- Practice cross-platform development
""")

print("=" * 70)
print("END OF CHAPTER 23: OS MODULE")
print("=" * 70)