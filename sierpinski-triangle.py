import shutil


# Use the terminal size as the number of "pixels" on the screen
viewport = shutil.get_terminal_size()

for y in range(viewport.lines):
    for x in range(viewport.columns):
        if x & y:
            print(" ", end = "")
        else:
            print(".", end = "")
            