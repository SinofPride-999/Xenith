#######################################
# CONTROL FLOW TESTS
# Tests IF/ELIF/ELSE and ternary operator
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import InvalidSyntaxError

def test_control_flow():
    runner = TestRunner()

    def test_if_true():
        source = """
        VAR x = 10
        IF x > 5 {
            PRINT("PASS")
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_if_false():
        source = """
        VAR x = 3
        IF x > 5 {
            PRINT("FAIL")
        }
        PRINT("DONE")
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_if_else():
        source = """
        VAR x = 3
        IF x > 5 {
            PRINT("GREATER")
        } ELSE {
            PRINT("LESS OR EQUAL")
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_if_elif_else():
        source = """
        VAR score = 85
        IF score >= 90 {
            PRINT("A")
        } ELIF score >= 80 {
            PRINT("B")
        } ELIF score >= 70 {
            PRINT("C")
        } ELSE {
            PRINT("F")
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_nested_if():
        source = """
        VAR x = 10
        VAR y = 20
        IF x > 5 {
            IF y > 15 {
                PRINT("BOTH TRUE")
            }
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_ternary_basic():
        source = """
        VAR age = 20
        VAR status = age >= 18 ? "Adult" : "Minor"
        PRINT(status)
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_ternary_chained():
        source = """
        VAR score = 85
        VAR grade = score >= 90 ? "A" :
                   score >= 80 ? "B" :
                   score >= 70 ? "C" : "F"
        PRINT(grade)
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_ternary_with_arithmetic():
        source = """
        VAR x = 5
        VAR y = 10
        VAR max = x > y ? x : y
        PRINT(PRINT_RET(max))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_if_without_braces_single():
        source = """
        VAR x = 10
        IF x > 5
            PRINT("Single line")
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_invalid_syntax():
        source = """
        IF x > 5 {
            PRINT("Missing brace"
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, InvalidSyntaxError)

    runner.add_test("IF true", test_if_true)
    runner.add_test("IF false", test_if_false)
    runner.add_test("IF-ELSE", test_if_else)
    runner.add_test("IF-ELIF-ELSE", test_if_elif_else)
    runner.add_test("Nested IF", test_nested_if)
    runner.add_test("Ternary basic", test_ternary_basic)
    runner.add_test("Ternary chained", test_ternary_chained)
    runner.add_test("Ternary with arithmetic", test_ternary_with_arithmetic)
    runner.add_test("IF without braces", test_if_without_braces_single)
    runner.add_test("Invalid syntax", test_invalid_syntax)

    runner.run_all()

if __name__ == "__main__":
    test_control_flow()
