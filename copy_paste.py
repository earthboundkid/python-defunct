#! /usr/bin/env python3

"""copy_paste: Lets you manipulate the clipboard in OS X."""

import functools
from subprocess import Popen, PIPE

def copy(s):
    "Copy string argument to clipboard"
    
    copy = Popen(["pbcopy"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    _, err = copy.communicate(bytes(s, encoding="utf-8"))
    
    #Unlikely
    if err:
        raise Exception(err)

def paste():
    "Returns contents of clipboard"
    
    paste = Popen(["pbpaste"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    b, err = paste.communicate()
    
    #Unlikely
    if err:
        raise Exception(err)
    
    return b.decode("UTF-8")
