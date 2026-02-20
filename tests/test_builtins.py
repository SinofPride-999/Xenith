#######################################
# BUILT-IN FUNCTIONS TESTS
# Tests all built-in functions
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script

def test_builtins():
    runner = TestRunner()

    def test_is_number():
        source = """
        PRINT(PRINT_RET(IS_NUM(42)))
        PRINT(PRINT_RET(IS_NUM("hello")))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_is_string():
        source = """
        PRINT(PRINT_RET(IS_STR("hello")))
        PRINT(PRINT_RET(IS_STR(42)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_is_list():
        source = """
        PRINT(PRINT_RET(IS_LIST([1, 2, 3])))
        PRINT(PRINT_RET(IS_LIST(42)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_is_function():
        source = """
        FUN double(x) -> x * 2
        PRINT(PRINT_RET(IS_FUN(double)))
        PRINT(PRINT_RET(IS_FUN(42)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_print_ret():
        source = """
        VAR s = PRINT_RET(42)
        VAR t = PRINT_RET("hello")
        PRINT(s + " " + t)
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_math_constants():
        source = """
        PRINT(PRINT_RET(MATH_PI))
        PRINT(PRINT_RET(TRUE))
        PRINT(PRINT_RET(FALSE))
        PRINT(PRINT_RET(NULL))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_type_coercion():
        source = """
        PRINT(PRINT_RET(TRUE + FALSE))
        PRINT(PRINT_RET(TRUE * 5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("IS_NUM", test_is_number)
    runner.add_test("IS_STR", test_is_string)
    runner.add_test("IS_LIST", test_is_list)
    runner.add_test("IS_FUN", test_is_function)
    runner.add_test("PRINT_RET", test_print_ret)
    runner.add_test("Math constants", test_math_constants)
    runner.add_test("Type coercion", test_type_coercion)

    runner.run_all()

if __name__ == "__main__":
    test_builtins()
