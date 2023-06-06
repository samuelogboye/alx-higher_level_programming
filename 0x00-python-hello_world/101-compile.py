#!/usr/bin/python3
import os
import py_compile

filename = os.environ.get('PYFILE')

if filename:
    output_filename = filename + 'c'

    try:
        py_compile.compile(filename, cfile=output_filename)
        print("Compiling {}...".format(filename))
    except py_compile.PyCompileError:
        print("Error compiling file")
else:
    print("PYFILE environment variable not set")
