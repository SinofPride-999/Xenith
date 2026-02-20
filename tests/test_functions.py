#######################################
# FUNCTION TESTS
# Tests function definition and calling
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import RTError

def test_functions():
    runner = TestRunner()

    def test_basic_function():
        source = """
        FUN greet(name) {
            RETURN "Hello, " + name + "!"
        }
        PRINT(greet("World"))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_function_with_multiple_params():
        source = """
        FUN add(a, b) {
            RETURN a + b
        }
        PRINT(PRINT_RET(add(5, 3)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_arrow_function():
        source = """
        FUN double(x) -> x * 2
        PRINT(PRINT_RET(double(7)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_function_no_return():
        source = """
        FUN doNothing() {
            VAR x = 42
        }
        PRINT(PRINT_RET(doNothing()))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_recursive_function_iterative():
        source = """
        FUN factorial(n) {
            VAR result = 1
            VAR i = 1
            WHILE i <= n {
                VAR result = result * i
                VAR i = i + 1
            }
            RETURN result
        }
        PRINT(PRINT_RET(factorial(5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_function_returning_list():
        source = """
        FUN range(n) {
            VAR result = []
            VAR i = 0
            WHILE i < n {
                APPEND(result, i)
                VAR i = i + 1
            }
            RETURN result
        }
        PRINT(PRINT_RET(range(5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_first_class_function():
        source = """
        FUN double(x) -> x * 2
        VAR my_func = double
        PRINT(PRINT_RET(my_func(10)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_function_as_argument():
        source = """
        FUN apply(func, x) {
            RETURN func(x)
        }
        FUN double(x) -> x * 2
        PRINT(PRINT_RET(apply(double, 5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_higher_order_function():
        source = """
        FUN make_multiplier(factor) {
            FUN multiplier(x) -> x * factor
            RETURN multiplier
        }
        VAR times3 = make_multiplier(3)
        PRINT(PRINT_RET(times3(10)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_function_scope():
        source = """
        VAR x = 10
        FUN test() {
            VAR x = 20
            RETURN x
        }
        PRINT(PRINT_RET(test()))
        PRINT(PRINT_RET(x))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_too_few_args():
        source = """
        FUN add(a, b) {
            RETURN a + b
        }
        PRINT(PRINT_RET(add(5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)

    def test_too_many_args():
        source = """
        FUN add(a, b) {
            RETURN a + b
        }
        PRINT(PRINT_RET(add(5, 3, 2)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)

    runner.add_test("Basic function", test_basic_function)
    runner.add_test("Multiple parameters", test_function_with_multiple_params)
    runner.add_test("Arrow function", test_arrow_function)
    runner.add_test("Function no return", test_function_no_return)
    runner.add_test("Recursive function (iterative)", test_recursive_function_iterative)
    runner.add_test("Function returning list", test_function_returning_list)
    runner.add_test("First-class function", test_first_class_function)
    runner.add_test("Function as argument", test_function_as_argument)
    runner.add_test("Higher-order function", test_higher_order_function)
    runner.add_test("Function scope", test_function_scope)
    runner.add_test("Too few arguments", test_too_few_args)
    runner.add_test("Too many arguments", test_too_many_args)

    runner.run_all()

if __name__ == "__main__":
    test_functions()
