#######################################
# INTERACTIVE SHELL MODULE
# Implements the REPL (Read-Eval-Print Loop) for Xenith.
# Allows users to interactively execute code and see immediate results.
# Only shows output from PRINT statements, not internal return values.
#######################################

import sys
sys.path.append('./core')
from main import run

def run_interactive():
    print("Xenith Interactive Shell")
    print("Type 'exit()' to quit")
    print("=" * 40)

    while True:
        try:
            text = input('jhay > ')
            if text.strip() == "":
                continue
            if text.strip() == "exit()":
                print("Goodbye!")
                break

            result, error = run('<stdin>', text)

            if error:
                print(error.as_string())
            # Don't print the result - only output from PRINT statements appears

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def run_file(filename):
    try:
        with open(filename, 'r') as f:
            script = f.read()

        print(f"Running: {filename}")
        print("=" * 50)

        result, error = run(filename, script)

        if error:
            print(error.as_string())
        # Don't print the result - only output from PRINT statements appears

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_interactive()
