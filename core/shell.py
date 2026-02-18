#######################################
# INTERACTIVE SHELL MODULE
# Implements the REPL (Read-Eval-Print Loop) for JhayScript.
# Allows users to interactively execute code and see immediate results.
# Useful for testing and learning the language.
#######################################

import sys
sys.path.append('./core')
from main import run

while True:
    text = input('basic > ')
    if text.strip() == "":
        continue
    result, error = run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if hasattr(result, 'elements') and len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
