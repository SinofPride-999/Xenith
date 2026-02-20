#######################################
# COMPARISON TESTS
# Tests comparison and logical operators
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_runner import TestRunner, assert_error, run_jhay_script

def test_comparisons():
    runner = TestRunner()

    def test_equal():
        source = """
        PRINT(PRINT_RET(5 == 5))
        PRINT(PRINT_RET(5 == 3))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_not_equal():
        source = """
        PRINT(PRINT_RET(5 != 3))
        PRINT(PRINT_RET(5 != 5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_less_than():
        source = """
        PRINT(PRINT_RET(3 < 5))
        PRINT(PRINT_RET(5 < 3))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_greater_than():
        source = """
        PRINT(PRINT_RET(5 > 3))
        PRINT(PRINT_RET(3 > 5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_less_than_equal():
        source = """
        PRINT(PRINT_RET(3 <= 5))
        PRINT(PRINT_RET(5 <= 5))
        PRINT(PRINT_RET(6 <= 5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_greater_than_equal():
        source = """
        PRINT(PRINT_RET(5 >= 3))
        PRINT(PRINT_RET(5 >= 5))
        PRINT(PRINT_RET(3 >= 5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_and():
        source = """
        PRINT(PRINT_RET((5 > 3) AND (10 > 5)))
        PRINT(PRINT_RET((5 > 3) AND (10 < 5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_or():
        source = """
        PRINT(PRINT_RET((5 > 3) OR (10 < 5)))
        PRINT(PRINT_RET((5 < 3) OR (10 < 5)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_not():
        source = """
        PRINT(PRINT_RET(NOT (5 > 3)))
        PRINT(PRINT_RET(NOT (5 < 3)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("Equal", test_equal)
    runner.add_test("Not equal", test_not_equal)
    runner.add_test("Less than", test_less_than)
    runner.add_test("Greater than", test_greater_than)
    runner.add_test("Less than or equal", test_less_than_equal)
    runner.add_test("Greater than or equal", test_greater_than_equal)
    runner.add_test("AND", test_and)
    runner.add_test("OR", test_or)
    runner.add_test("NOT", test_not)

    runner.run_all()

if __name__ == "__main__":
    test_comparisons()
