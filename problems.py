"""
In the sample text folder you will find a file named "strings.json". It is a list of strings.
Create a new file named "string_lengths_map.json" in the sample text folder that contains a dictionary of all the strings
in the first json as keys mapped to their lengths.
"""


def convert_json():
    pass


"""
In the sample_text folder you will find a file named "sonnets.txt". This file contains (almost) all the
sonnets written by William Shakespeare in a numbered order.

Create a new folder named "sonnets", and store each sonnet in it as a separate file named "sonnet_x.txt" where the x
is replaced with the sonnet number. The contents of each file should be only the lines of text for each sonnet, so
you don't need the empty lines above or below. Don't forget to have a newline at the end of the last line (that
should make things easier rather than harder)

The test will delete whatever harness you already created
"""


def separate_sonnets():
    pass


"""
In the sample_text folder you will find a file named "iso_8859-1.txt". This file contains a list of the
hexadecimal representation of commonly used characters.

The hex values and descriptions are currently in two columns.
Write a function that creates a new  file will all hex values and descriptions in a single column,
shifting the second column to continue immediately under the first. Name this file "iso_8859-1_two_columns.txt" and
place it in the sample_text folder.

Don't worry about any trailing whitespace on your lines, the tests will use strip before comparing your generated
file to the one it validated against.

Yes, you could just store a string copy of the entire file you want to write in your function. You are very clever. Don't do that.
You probably want to save a safe copy of the original on the indescribably small chance you mess it up along the way.
"""


def two_columns_to_one():
    pass
