#######################################
# LOOP TESTS
# Tests FOR and WHILE loops with BREAK/CONTINUE
#######################################

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_runner import TestRunner, assert_output, assert_error, run_jhay_script

def test_loops():
    runner = TestRunner()

    def test_for_basic():
        source = """
        FOR i = 0 TO 5 {
            PRINT(PRINT_RET(i))
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_for_with_step():
        source = """
        FOR i = 0 TO 10 STEP 2 {
            PRINT(PRINT_RET(i))
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_for_negative_step():
        source = """
        FOR i = 10 TO 0 STEP -2 {
            PRINT(PRINT_RET(i))
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_while_basic():
        source = """
        VAR i = 0
        WHILE i < 5 {
            PRINT(PRINT_RET(i))
            VAR i = i + 1
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_break():
        source = """
        FOR i = 0 TO 10 {
            IF i == 5 {
                BREAK
            }
            PRINT(PRINT_RET(i))
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_continue():
        source = """
        FOR i = 0 TO 5 {
            IF i == 3 {
                CONTINUE
            }
            PRINT(PRINT_RET(i))
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_nested_loops():
        source = """
        FOR i = 0 TO 3 {
            FOR j = 0 TO 2 {
                PRINT(PRINT_RET(i) + "," + PRINT_RET(j))
            }
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_while_with_break():
        source = """
        VAR i = 0
        WHILE i < 10 {
            IF i == 5 {
                BREAK
            }
            PRINT(PRINT_RET(i))
            VAR i = i + 1
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_infinite_loop_with_break():
        source = """
        VAR i = 0
        WHILE 1 {
            PRINT(PRINT_RET(i))
            VAR i = i + 1
            IF i == 5 {
                BREAK
            }
        }
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    def test_for_collect_results():
        source = """
        VAR results = []
        FOR i = 0 TO 5 {
            APPEND(results, i)
        }
        PRINT(PRINT_RET(results))
        """
        result, error = run_jhay_script("<test>", source)
        assert_error(error, None)

    runner.add_test("FOR basic", test_for_basic)
    runner.add_test("FOR with STEP", test_for_with_step)
    runner.add_test("FOR negative STEP", test_for_negative_step)
    runner.add_test("WHILE basic", test_while_basic)
    runner.add_test("BREAK", test_break)
    runner.add_test("CONTINUE", test_continue)
    runner.add_test("Nested loops", test_nested_loops)
    runner.add_test("WHILE with BREAK", test_while_with_break)
    runner.add_test("Infinite loop with BREAK", test_infinite_loop_with_break)
    runner.add_test("FOR collect results", test_for_collect_results)

    runner.run_all()

if __name__ == "__main__":
    test_loops()
