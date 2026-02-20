#######################################
# ERROR HANDLING TESTS
# Tests error messages and edge cases
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import IllegalCharError, InvalidSyntaxError, RTError, ExpectedCharError

def test_errors():
    runner = TestRunner()

    def test_illegal_char():
        source = "PRINT($)"  # $ is illegal
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, IllegalCharError)

    def test_unclosed_string():
        source = 'PRINT("hello)'
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, IllegalCharError) or isinstance(error, InvalidSyntaxError)

    def test_missing_brace():
        source = """
        IF x > 5 {
            PRINT("missing brace")
        """
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, InvalidSyntaxError)

    def test_extra_brace():
        source = """
        IF x > 5 {
            PRINT("extra brace")
        }}
        """
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, InvalidSyntaxError)

    def test_missing_equals_in_var():
        source = "VAR x 5"  # Missing =
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, InvalidSyntaxError)

    def test_missing_then_in_ternary():
        source = "VAR x = 5 ? 10 20"  # Missing colon
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, InvalidSyntaxError)

    def test_type_error_addition():
        source = 'PRINT(5 + "hello")'
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, RTError)

    def test_type_error_comparison():
        source = 'PRINT(5 > "hello")'
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, RTError)

    def test_undefined_function():
        source = "nonexistent()"
        result, error = run_jhay_script("<test>", source)
        assert error is not None
        assert isinstance(error, RTError)

    def test_empty_program():
        source = ""
        result, error = run_jhay_script("<test>", source)
        assert error is None

    def test_only_comments():
        source = """
        # This is a comment
        # Another comment
        """
        result, error = run_jhay_script("<test>", source)
        assert error is None

    runner.add_test("Illegal character", test_illegal_char)
    runner.add_test("Unclosed string", test_unclosed_string)
    runner.add_test("Missing brace", test_missing_brace)
    runner.add_test("Extra brace", test_extra_brace)
    runner.add_test("Missing equals in VAR", test_missing_equals_in_var)
    runner.add_test("Missing colon in ternary", test_missing_then_in_ternary)
    runner.add_test("Type error addition", test_type_error_addition)
    runner.add_test("Type error comparison", test_type_error_comparison)
    runner.add_test("Undefined function", test_undefined_function)
    runner.add_test("Empty program", test_empty_program)
    runner.add_test("Only comments", test_only_comments)

    runner.run_all()

if __name__ == "__main__":
    test_errors()
