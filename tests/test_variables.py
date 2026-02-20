#######################################
# VARIABLES TESTS
# Tests variable declaration, assignment, and access
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import RTError
from core.values import Number, String, List

def test_variables():
    runner = TestRunner()

    def test_var_declaration():
        source = """
        VAR x = 42
        VAR y = "hello"
        VAR z = [1, 2, 3]
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_access():
        source = """
        VAR x = 42
        VAR y = x
        PRINT(PRINT_RET(y))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_reassignment():
        source = """
        VAR x = 42
        VAR x = 100
        PRINT(PRINT_RET(x))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_undefined_var():
        source = "PRINT(PRINT_RET(undefined))"
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)
        assert "not defined" in error.details if error else ""

    def test_multiple_vars():
        source = """
        VAR a = 5
        VAR b = 10
        VAR c = a + b
        PRINT(PRINT_RET(c))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_scope():
        source = """
        VAR x = 10
        IF x > 5 {
            VAR y = 20
            VAR x = 30
            PRINT(PRINT_RET(x))
        }
        PRINT(PRINT_RET(x))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_naming():
        source = """
        VAR _underscore = 1
        VAR camelCase = 2
        VAR PascalCase = 3
        VAR with123 = 4
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("VAR declaration", test_var_declaration)
    runner.add_test("VAR access", test_var_access)
    runner.add_test("VAR reassignment", test_var_reassignment)
    runner.add_test("Undefined variable", test_undefined_var)
    runner.add_test("Multiple variables", test_multiple_vars)
    runner.add_test("Variable scope", test_var_scope)
    runner.add_test("Variable naming", test_var_naming)

    runner.run_all()

if __name__ == "__main__":
    test_variables()
