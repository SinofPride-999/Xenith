#######################################
# BASIC SYNTAX TESTS
# Tests fundamental language features
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import IllegalCharError, InvalidSyntaxError

def test_basic():
    runner = TestRunner()

    def test_comments():
        source = """
        # This is a comment
        PRINT("Hello")  # inline comment
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_empty_program():
        source = ""
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_multiple_statements():
        source = """
        PRINT("First")
        PRINT("Second")
        PRINT("Third")
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_illegal_character():
        source = "PRINT(@)"  # @ is illegal
        result, error = run_jhay_script("<test>", source)
        assert_error(error, IllegalCharError)

    def test_string_with_escapes():
        source = """
        PRINT("Hello\\nWorld")
        PRINT("Tab\\tHere")
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("Comments", test_comments)
    runner.add_test("Empty program", test_empty_program)
    runner.add_test("Multiple statements", test_multiple_statements)
    runner.add_test("Illegal character", test_illegal_character)
    runner.add_test("String escapes", test_string_with_escapes)

    runner.run_all()

if __name__ == "__main__":
    test_basic()
