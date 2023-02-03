import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    'includes': [
        'cx_Logging',
    ],
    "packages": ["os", 'sys'],
    "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="test_linter.py",
    base=base,
)

setup(
    name="test_workflow",
    version="2.0",
    description="Gas Oil Research project",
    options={"build_exe": build_exe_options},
    executables=[target],
)
