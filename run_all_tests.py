#!/usr/bin/env python3
#######################################
# RUN ALL JHAYSCRIPT TESTS
#######################################

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from tests.test_basic import test_basic
from tests.test_variables import test_variables
from tests.test_arithmetic import test_arithmetic
from tests.test_comparisons import test_comparisons
from tests.test_control_flow import test_control_flow
from tests.test_loops import test_loops
from tests.test_lists import test_lists
from tests.test_functions import test_functions
from tests.test_builtins import test_builtins
from tests.test_errors import test_errors

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("RUNNING ALL JHAYSCRIPT TESTS")
    print("=" * 60)

    tests = [
        ("Basic Syntax", test_basic),
        ("Variables", test_variables),
        ("Arithmetic", test_arithmetic),
        ("Comparisons", test_comparisons),
        ("Control Flow", test_control_flow),
        ("Loops", test_loops),
        ("Lists", test_lists),
        ("Functions", test_functions),
        ("Built-ins", test_builtins),
        ("Error Handling", test_errors),
    ]

    total_passed = 0
    total_failed = 0

    for name, test_func in tests:
        print(f"\n📋 {name.upper()} TESTS")
        print("-" * 40)
        # Each test function runs its own suite and prints results
        # We're just calling them sequentially
        test_func()

    print("\n" + "=" * 60)
    print("ALL TEST SUITES COMPLETE")
    print("=" * 60)
