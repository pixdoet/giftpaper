#!/usr/bin/env python3

"""
    giftpaper - a python tool to compile different JS files into one main file

    Copyright 2022 Ian Hiew

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import json
import os
from jsmin import jsmin


class PrintColours:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    FAIL = "\033[91m"
    UNDERLINE = "\033[4m"
    STOP = "\033[0m"


colours = PrintColours()


def loadFile(file):
    f = open(file)
    return json.load(f)


def checkFiles():
    # check if the files exist
    if not os.path.isfile("compile.json"):
        print("compile.json not found!")
        return False
    else:
        # continue checking the files listed in compile.json
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


# get all .js files from src folder
def getAllFiles():
    if checkFiles():
        mainResponseContext = loadFile("compile.json")
        files = mainResponseContext["files"]
        fileList = []
        for file in files:
            fileList.append(file)
        print(f"Files to be bundled: {fileList}")
        return fileList


# bundle js files into main.js
def bundle():
    if checkFiles():
        mainResponseContext = loadFile("compile.json")
        outputFile = mainResponseContext["output"]
        useBabel = mainResponseContext["minify"]
        files = getAllFiles()
        # clear the already existing output file
        with open(outputFile, "w+") as mainF:
            for file in files:
                with open(file, "r") as f:
                    print(f"Bundling {file} into {outputFile}...")
                    mainF.write(f"\n// From {file}")
                    mainF.write(f"\n{f.read()}")
                    if mainF:
                        print(f"Bundled {file} into {outputFile}")
        if useBabel:
            print(
                f"""{colours.YELLOW}
            WARNING: The minifier library can make your code smaller, but can also result in unexpected editing of code
            Please use this option with care and expect your code to produce different results.
            {colours.STOP}
            """
            )
            print("Bundling finished. Now minifying with jsmin...")
            with open(f"{outputFile}", "r") as mainF:
                with open(f"{outputFile}.min.js", "w+") as f:
                    f.write(jsmin(mainF.read()))
                    if f:
                        print("Finished minifying with jsmin!")
        print(
            f"{colours.GREEN}Finished bundling! Your script can be found in {outputFile}{colours.STOP}"
        )


def main():
    if checkFiles():
        print("Start bundling files...")
        bundle()


if __name__ == "__main__":
    main()
# bundle()
