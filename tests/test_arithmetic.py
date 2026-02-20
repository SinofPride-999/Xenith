#######################################
# ARITHMETIC TESTS
# Tests arithmetic operations
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import RTError

def test_arithmetic():
    runner = TestRunner()

    def capture_output(source):
        """Helper to capture PRINT output"""
        result, error = run_jhay_script("<test>", source)
        return result, error

    def test_addition():
        source = """
        PRINT(PRINT_RET(5 + 3))
        PRINT(PRINT_RET(2.5 + 1.5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_subtraction():
        source = """
        PRINT(PRINT_RET(10 - 4))
        PRINT(PRINT_RET(5.5 - 2.2))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_multiplication():
        source = """
        PRINT(PRINT_RET(6 * 7))
        PRINT(PRINT_RET(2.5 * 3))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_division():
        source = """
        PRINT(PRINT_RET(15 / 3))
        PRINT(PRINT_RET(7 / 2))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_division_by_zero():
        source = "PRINT(PRINT_RET(5 / 0))"
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)
        assert "Division by zero" in error.details if error else ""

    def test_power():
        source = """
        PRINT(PRINT_RET(2 ^ 3))
        PRINT(PRINT_RET(5 ^ 2))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_precedence():
        source = """
        PRINT(PRINT_RET(2 + 3 * 4))
        PRINT(PRINT_RET((2 + 3) * 4))
        PRINT(PRINT_RET(10 - 2 ^ 3))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_unary_minus():
        source = """
        PRINT(PRINT_RET(-5))
        PRINT(PRINT_RET(-(10 + 3)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_complex_expression():
        source = """
        VAR x = 10
        VAR y = 3
        VAR z = (x + y) * (x - y) / 2
        PRINT(PRINT_RET(z))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("Addition", test_addition)
    runner.add_test("Subtraction", test_subtraction)
    runner.add_test("Multiplication", test_multiplication)
    runner.add_test("Division", test_division)
    runner.add_test("Division by zero", test_division_by_zero)
    runner.add_test("Power", test_power)
    runner.add_test("Operator precedence", test_precedence)
    runner.add_test("Unary minus", test_unary_minus)
    runner.add_test("Complex expression", test_complex_expression)

    runner.run_all()

if __name__ == "__main__":
    test_arithmetic()
