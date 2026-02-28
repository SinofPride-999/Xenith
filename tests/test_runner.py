#######################################
# TEST RUNNER MODULE
# Runs all Xenith tests and reports results
#######################################

import sys
import os
import time
from pathlib import Path

# Add core to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.main import run

class TestResult:
    def __init__(self, name):
        self.name = name
        self.passed = False
        self.error = None
        self.time = 0

class TestRunner:
    def __init__(self):
        self.tests = []
        self.passed = 0
        self.failed = 0
        self.total_time = 0

    def add_test(self, name, test_func):
        self.tests.append((name, test_func))

    def run_all(self):
        print("\n" + "=" * 60)
        print("Xenith TEST SUITE")
        print("=" * 60)

        for name, test_func in self.tests:
            result = self.run_test(name, test_func)

            if result.passed:
                self.passed += 1
                print(f"✅ {result.name} ({result.time:.3f}s)")
            else:
                self.failed += 1
                print(f"❌ {result.name} ({result.time:.3f}s)")
                if result.error:
                    print(f"   Error: {result.error}")

        self.print_summary()

    def run_test(self, name, test_func):
        result = TestResult(name)
        start_time = time.time()

        try:
            test_func()
            result.passed = True
        except AssertionError as e:
            result.error = str(e)
        except Exception as e:
            result.error = f"Exception: {type(e).__name__}: {e}"

        result.time = time.time() - start_time
        self.total_time += result.time
        return result

    def print_summary(self):
        print("\n" + "=" * 60)
        print(f"RESULTS: {self.passed} passed, {self.failed} failed")
        print(f"Total time: {self.total_time:.3f}s")
        print("=" * 60)

        if self.failed == 0:
            print("🎉 ALL TESTS PASSED!")
        else:
            print("❌ Some tests failed.")
        print()

def assert_output(actual, expected, message=""):
    """Assert that actual output matches expected"""
    if actual != expected:
        raise AssertionError(f"{message}\nExpected: {expected}\nGot: {actual}")

def assert_error(error, expected_type, message=""):
    """Assert that error is of expected type"""
    if error is None:
        raise AssertionError(f"{message}\nExpected error {expected_type}, got no error")
    if not isinstance(error, expected_type):
        raise AssertionError(f"{message}\nExpected error type {expected_type}, got {type(error).__name__}")

def run_jhay_script(filename, source=None):
    """Run a Xenith file and return (result, error)"""
    if source is None:
        with open(filename, 'r') as f:
            source = f.read()
    return run(filename, source)
