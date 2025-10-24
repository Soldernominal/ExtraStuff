# Lang conversion from/to gamecode ver 0.1
# Author: Rufat
# Licensed under the MIT License

#!/usr/bin/env python3
import sys
import os
import shutil
"""
1) Makes lang directory and necessary .txt files inside, if you don't have them
2) You have to input gamecode lines into the rawstr.txt file on each line, in order for script to work
3) You have to manually copy/paste all new batches from eng.txt to ru.txt(separate batches by AT LEAST 1 line)
4) Enjoy
"""
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller exe."""
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def readable_to_gamecode(translatedfile = "ru.txt", gamecodefile="ru_gamecode_lines.txt", eng_fiename="eng.txt"):
    """
    Converts readable file intended as russian translation back into the gamecode structure, saved as .txt
    Expected structure:
        translatedfile: Multiple lines until the first empty line are a translated batch,
                        akin to the output result from gamecode_to_readable() function.
                        They are expected to be separated by 1 or more lines.
        gamecodefile: Each line is of the raw gamecode form, each corresponds to a singular batch.
    """
    folder = resource_path("lang")
    os.makedirs(folder, exist_ok=True)  # create lang if DNE

    # Full path to the output file
    translatedfile = os.path.join(folder, translatedfile)
    gamecodefile = os.path.join(folder, gamecodefile)
    eng_fiename = os.path.join(folder, eng_fiename)

    # Create file if DNE
    if not os.path.exists(translatedfile):
        print(f"Creating eng.txt at {eng_fiename}")
        with open(translatedfile, "w", encoding="utf-8") as f:
            shutil.copyfile(eng_fiename, translatedfile)

    translated_batches = []
    batchstr = str()
    with open(translatedfile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line.strip() != "":  # empty line (only whitespace)
                batchstr += line
            else:
                if batchstr != "":
                    translated_batches.append(batchstr)
                batchstr = ""

    with open(gamecodefile, "w", encoding="utf-8") as f:
        for batch in translated_batches:
            converted_string = batch.replace('\\n\n', '\\n')
            f.write(converted_string)

def gamecode_to_readable(rawfilename="rawstr.txt", filtered_fiename="eng.txt"):
    """
    Converts gamecode line into the translation batches, separated by space, saved into .txt file
    Expected structure:
        rawfilename: Each line is of form: var dia_intro = 'intro#\nINPUT: Have it now. You there?\nSARAH:...'
        filtered_fiename: Each line from the raw file gets converted into multiple lines,
                            until the first empty line translated batch
    """
    #folder = os.path.join(os.path.dirname(__file__), "lang")
    folder = resource_path("lang")
    os.makedirs(folder, exist_ok=True)  # create lang if it DNE

    # Full path to the output file
    rawfilename = os.path.join(folder, rawfilename)
    filtered_fiename = os.path.join(folder, filtered_fiename)

    # create rawstr.txt if it DNE
    if not os.path.exists(rawfilename):
        print(f"Creating rawstr.txt at {rawfilename}")
        with open(rawfilename, "w", encoding="utf-8") as f:
            f.write("")  # empty file

    # Read raw strings and store them all into the list
    with open(rawfilename, "r", encoding="utf-8") as f:
        rawlinelist = f.readlines()

    # Convert raw strings from the list into readable form and store into filtered.txt
    with open(filtered_fiename, "w", encoding="utf-8") as f:
        for rawstring in rawlinelist:
            content = rawstring.replace('\\"', '"').replace('\\n', '\\n\n').strip()
            converted__string = f'{content};'
            f.write(converted__string)
            f.write("\n\n\n")


# Example use
#gamecode_to_readable()
#readable_to_gamecode()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mymodule.exe readable_to_gamecode|gamecode_to_readable")
        sys.exit(1)
    cmd = sys.argv[1].lower()
    if cmd == "readable_to_gamecode":
        readable_to_gamecode()
    elif cmd == "gamecode_to_readable":
        gamecode_to_readable()
    else:
        print(f"Unknown command: {cmd}")
