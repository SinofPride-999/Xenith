#######################################
# VARIABLES TESTS
# Tests variable declaration, assignment, and access
#######################################

from core.values import Number, String, List
from core.error import RTError
from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_variables():
    runner = TestRunner()

    def test_var_declaration():
        source = """
        spawn x = 42
        spawn y = "hello"
        spawn z = [1, 2, 3]
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_access():
        source = """
        spawn x = 42
        spawn y = x
        PRINT(PRINT_RET(y))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_reassignment():
        source = """
        spawn x = 42
        spawn x = 100
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
        spawn a = 5
        spawn b = 10
        spawn c = a + b
        PRINT(PRINT_RET(c))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_scope():
        source = """
        spawn x = 10
        IF x > 5 {
            spawn y = 20
            spawn x = 30
            PRINT(PRINT_RET(x))
        }
        PRINT(PRINT_RET(x))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_var_naming():
        source = """
        spawn _underscore = 1
        spawn camelCase = 2
        spawn PascalCase = 3
        spawn with123 = 4
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("spawn declaration", test_var_declaration)
    runner.add_test("spawn access", test_var_access)
    runner.add_test("spawn reassignment", test_var_reassignment)
    runner.add_test("Undefined variable", test_undefined_var)
    runner.add_test("Multiple variables", test_multiple_vars)
    runner.add_test("Variable scope", test_var_scope)
    runner.add_test("Variable naming", test_var_naming)

    runner.run_all()


if __name__ == "__main__":
    test_variables()
