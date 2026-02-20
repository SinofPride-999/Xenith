#######################################
# LIST TESTS
# Tests list operations and built-in functions
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script
from core.error import RTError

def test_lists():
    runner = TestRunner()

    def test_list_creation():
        source = """
        VAR empty = []
        VAR numbers = [1, 2, 3]
        VAR mixed = [1, "two", 3.0]
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_list_access():
        source = """
        VAR list = [10, 20, 30]
        PRINT(PRINT_RET(list/0))
        PRINT(PRINT_RET(list/1))
        PRINT(PRINT_RET(list/2))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_list_access_out_of_bounds():
        source = """
        VAR list = [1, 2, 3]
        PRINT(PRINT_RET(list/5))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)

    def test_append():
        source = """
        VAR list = [1, 2, 3]
        APPEND(list, 4)
        PRINT(PRINT_RET(list))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_pop():
        source = """
        VAR list = [10, 20, 30]
        VAR popped = POP(list, 1)
        PRINT("Popped: " + popped)
        PRINT("Remaining: " + PRINT_RET(list))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_pop_out_of_bounds():
        source = """
        VAR list = [1, 2, 3]
        VAR popped = POP(list, 5)
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, RTError)

    def test_extend():
        source = """
        VAR list1 = [1, 2, 3]
        VAR list2 = [4, 5, 6]
        EXTEND(list1, list2)
        PRINT(PRINT_RET(list1))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_len():
        source = """
        VAR list = [10, 20, 30, 40]
        PRINT(PRINT_RET(LEN(list)))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_list_concatenation():
        source = """
        VAR a = [1, 2]
        VAR b = [3, 4]
        VAR c = a + b
        PRINT(PRINT_RET(c))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_nested_lists():
        source = """
        VAR matrix = [[1, 2], [3, 4], [5, 6]]
        PRINT(PRINT_RET(matrix/1/0))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_list_operations_chain():
        source = """
        VAR list = []
        APPEND(list, 1)
        APPEND(list, 2)
        APPEND(list, 3)
        VAR popped = POP(list, 1)
        EXTEND(list, [4, 5])
        PRINT(PRINT_RET(list))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("List creation", test_list_creation)
    runner.add_test("List access", test_list_access)
    runner.add_test("List access out of bounds", test_list_access_out_of_bounds)
    runner.add_test("APPEND", test_append)
    runner.add_test("POP", test_pop)
    runner.add_test("POP out of bounds", test_pop_out_of_bounds)
    runner.add_test("EXTEND", test_extend)
    runner.add_test("LEN", test_len)
    runner.add_test("List concatenation", test_list_concatenation)
    runner.add_test("Nested lists", test_nested_lists)
    runner.add_test("List operations chain", test_list_operations_chain)

    runner.run_all()

if __name__ == "__main__":
    test_lists()
