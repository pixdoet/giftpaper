#!/usr/bin/env python3

"""
    giftpaper - a python tool to compile different JS files into one main file

    (C) 2022 Ian Hiew. All rights reserved.
"""

import json
import os
import sys


def loadFile(file):
    f = open(file)
    return json.load(f)


def checkFiles():
    # check if the files exist
    if not os.path.isfile("compile.json"):
        print("compile.json not found!")
        return False
    else:
        # continue checking the files listed in critter.json
        mainResponseContext = loadFile("compile.json")
        if not mainResponseContext["files"]:
            print('compile.json error: no "files" array found!')
            return False
        else:
            for file in mainResponseContext["files"]:
                if not os.path.isfile(file):
                    print(f"file error: {file} not found!")
                    return False
            print("Checking done")
            return True


checkFiles()

# get all .js files from src folder
def getAllFiles():
    if checkFiles():
        mainResponseContext = loadFile("compile.json")
        files = mainResponseContext["files"]
        fileList = []
        for file in files:
            fileList.append(file)
        # print(files)
        print(fileList)
        return fileList


getAllFiles()

# bundle js files into main.js
def bundle():
    if checkFiles():
        mainResponseContext = loadFile("compile.json")
        outputFile = mainResponseContext["output"]
        files = getAllFiles()
        # clear the already existing output file
        with open(outputFile, "w+") as mainF:
            for file in files:
                with open(file, "r") as f:
                    print(f"Bundling {file} into main.js...")
                    mainF.write(f"\n// From {file}")
                    mainF.write(f"\n{f.read()}")
                    if mainF:
                        print(f"Bundled {file} into {outputFile}")
        print(f"Finished bundling! Your script can be found in {outputFile}")


def main():
    if checkFiles():
        print("Start bundling files...")
        bundle()


if __name__ == "__main__":
    main()
# bundle()
