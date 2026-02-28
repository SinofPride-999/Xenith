#######################################
# FILE RUNNER FOR Xenith
# Run a Xenith file directly
#######################################

import sys
sys.path.append('./core')
from main import run
import os

def run_file(filename):
    try:
        with open(filename, 'r') as f:
            script = f.read()

        print(f"Running: {filename}")
        print("=" * 50)

        result, error = run(filename, script)

        if error:
            print(error.as_string())
        # Don't print the result - it's just internal values
        # The program output already happened via PRINT statements

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        print("Usage: python run_file.py <filename.jhay>")
