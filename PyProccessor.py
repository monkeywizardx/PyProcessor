'''
PyProcessor is a macro-based text manipulation program patterned off of the C preprocessor.
It's designed to be easy to use and powerful. It uses simple instructions, one per line at most, prefixed with !.
The ! should not interfere with any not symbols, as it only matches ones that are alone on a line and have a command immediately afterwards.
It operates recursively on replacements, to allow multiple macro-uses, however they will not effect the macros themselves.
Currently, it does not support call-replacements, however that is on the line. It will require some serious regex work, however.
It is not written in a super pythonic style, and it does not have a class-based implementation.
It is written as a script for running over a file, and that does show in locations.
I have tried to keep it as clean and organized as possible.
It is also hopefully very well commented.
'''
# -------- Definitions --------
'''
This will take include argv, which will allow command line harvesting.
'''
from sys import argv

'''
This is preprocessor storage. It is where all macros are listed, so that way all functions can easily check through it.
It's stored as a dictionary, where the macro name is the key and the value is the result of the macro.
'''
macros = {
    
    }
'''
    These are the function definitions. They include every part of the preprocessor code that isn't simply "glue" code.
    These are vital to the functioning of the program itself.
    Each function will have a comment explaining there algorithim at the start of the function.
    This will also list what it's inputs are and what they do.
'''
def fileToString(file):
    '''
    fileToString is a function meant to make copies of a file as a string.
    It works using the fact that files are iterators.
    It starts by generating an empty array, then follows it by iteraing through the file,
    appending each line.
    Finally, it returns the file.
    '''
    file_array = []
    for line in file:
        file_array.append(line)
    return file_array    

def findAllMacros(file_array):
    '''
    findAllMacros iterates through the entire file.
    It splits each line, and checks the first word. If the first word is !DEFINE (which is not case sensitive, thanks to a call to str.Upper()),
    it takes the next word as a key, joins the rest of the line until new line, and assigns that as the value of the key.
    If it isn't !DEFINE, then it adds it to an array of non-preprocessor lines. The list of non-preprocessor lines is the return value of the program.
    '''
    non_preprocessed_lines = []
    for line in file_array:
        checked_line = line.split().append('')
        if checked_line[0].upper() == '!DEFINE':
            macros[checked_line[1]] = ' '.join(checked_line[2:len(checked_line)])
        else:
            non_preprocessed_lines.append(line)
    return non_preprocessed_lines
def macroReplacement(file_array):
    '''
    macroReplacment takes the file array. It creates a 'new_file' array that will hold the preproccessed file.
    It then iterates through the original file, iterating through each macro and calling a .replace() on each line. It appends the replaced line to the new_file array.
    Finally, it returns the preproccessed file.
    '''
    new_file = []
    for line in file_array:
        new_line = line
        for macro in macros:
                new_line = new_line.replace(macro, macros[macro])
        new_file.append(new_line)
    return new_file
# -------- Main Block --------
'''
PyProcessor takes two command line arguements, the input and the output.
It does not complain about having MORE inputs, but it does not use them.
'''
if len(argv) < 3:
    '''
    If it doesn't have enough arguements, make sure to display a simple but descriptive error message.
    '''
    print('Error: PyProcessor takes two arguements (input file and output file).')
else:
    '''
    If the file does have enough inputs, open the two files.
    These two files are the input file, which is opened in read mode to allow the reading of the file,
    and the output file, which is opened in write mode to allow the modified version to be written there.
    It then writes the "input file" into a string called 'preprocessor_input_array'.
    Next, it finds the macros, then calls the replacement.
    Finally, it writes all the new lines into the output file.
    '''
    preprocessor_input = open(argv[1], 'r')
    preprocessor_output = open(argv[2], 'w')
    preprocessor_input_array = fileToString(preprocessor_input)
    preprocessor_input_array = findAllMacros(preprocessor_input_array)
    preprocessor_input_array = macroReplacement(preprocessor_input_array)
    for line in preprocessor_input_array:
        preprocessor_output.write(line)
