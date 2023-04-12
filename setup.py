from cx_Freeze import setup, Executable

base = None
executables = [Executable("autoKpass.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "AutoKeepass",
    options = options,
    version = "1.0.5",
    description = 'keepass open',
    executables = executables
)
