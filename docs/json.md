# `compile.json` options
[compile.json](../compile.json) is the main configuration file of the script. There are multiple options in the JSON file that are documented here.

## `output`
Used to specify the output directory. The output file will be placed in the directory and filename specified here. **Note: the filename must be included.**

## `files`
An array that stores the files for compiling. The contents must be a full file path that points towards a file, ie: `/src/main.js`

## `minify`
**EXPERIMENTAL**

Uses the [jsmin](https://pypi.org/jsmin) minifier to minify the output, allowing for more compact and lightweight scripts. **Note: using this option can break certain scripts.**

## `verbose`
Currently unused.
