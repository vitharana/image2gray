import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"includes": ["tkinter"]}
includes = ["tkinter"]
#includefiles = ['Source_Code/', 'wait.png',"imageTrack.png"]
includefiles = []
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Image2Gray",
    version="1.1",
    author = "SS Vitharana (Sri Lanka)",

    description="Image2Gray",


    options = {'build_exe': {'includes':includes,'include_files':includefiles}},
    executables=[Executable("main.py",shortcut_name = 'Image2Gray', shortcut_dir = 'DesktopFolder',icon='favicon.ico')],
)

