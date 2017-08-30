
#  PyProcessor

###  About PyProcessor

PyProcessor is a Python3 script designed to allow preprocessor like features for arbitrary
documents.

It's simple syntax should not interfere with anything.

###  Using PyProcessor

Using PyProcessor on a file is simple. 
```  python3 PyProcessor.py <input_file> <output_file> ``` 

Currently, it is only a single pass pre-processor. However, soon it will be switched
to an arbitrary pass pre-processor.

It only supports 1 command as of right now: ``` !DEFINE ``` . This is the macro generator
command. The name of the macro is the first space-seperated word after the !DEFINE. It's
value is the rest of the line.

