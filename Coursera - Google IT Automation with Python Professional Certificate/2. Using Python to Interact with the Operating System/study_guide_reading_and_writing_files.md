
## Study guide: Reading and writing files

Opening a file or file-like object to read or write is one of the fundamental steps of a Python programmer. For example, you may want to read a .csv file and convert it to JSON format. Or you may want to select data from a database and write it to an output file.
Reading and writing files

To read or write a file, use open(). This function includes two arguments: the file path and the mode.

```Python
with  open("sample_data/declaration.txt", "rt") as textfile:
for line in textfile:
print(line)
```

In this example, the first argument is a string containing the filename (sample_data/declaration.txt). The second argument identifies the mode or the way in which the file will be used (rt). “r” means open for reading, and “t” tells Python to expect a text file.

```Python
f = open("sample_data/declaration.txt", “w”)
```

In this example, the code tells Python to open this file for writing (“w” mode). 
Mode

The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

    “r”  open for reading (default)

    “w”  open for writing, truncating the file first

    “x”  open for exclusive creation, failing if the file already exists

    “a”  open for writing, appending to the end of the file if it exists

    “+”  open for both reading and writing

Attempting to write to a file opened for read (“r”) will cause a runtime error.
Encoding

Python distinguishes between binary mode (“b”) and text mode (“t”). By default, files are opened in the text mode, which means you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform-dependent. This means that locale.getencoding() is called to get the current locale encoding. If you need to open the text in a specific encoding, you must specify it.

```Python
f = open('workfile', 'w', encoding="utf-8")
```

In this example, the encoding=“utf-8” specifies that the file should be opened with UTF-8, the modern de facto standard. Binary mode data is read and written as bytes objects. You cannot specify encoding when opening a file in binary mode.

You have to have permission to write to the directory where you’re placing the file. It’s a best practice to always close a file .close() when you’re done working with it.
Key takeaways

To open a file for reading or writing, use open(filename, mode). Two arguments that are needed include the file name and the mode. Python will encode the file as text (“t”) by default unless a specific encoding is specified.
Resources for more information

More information about reading and writing files can be found in Built-in Functions:

    https://docs.python.org/3/library/functions.html#open
