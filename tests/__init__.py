# Test suite for Xenith
from .test_basic import test_basic
from .test_variables import test_variables
from .test_arithmetic import test_arithmetic
from .test_comparisons import test_comparisons
from .test_control_flow import test_control_flow
from .test_loops import test_loops
from .test_lists import test_lists
from .test_functions import test_functions
from .test_builtins import test_builtins
from .test_errors import test_errors

__all__ = [
    'test_basic',
    'test_variables',
    'test_arithmetic',
    'test_comparisons',
    'test_control_flow',
    'test_loops',
    'test_lists',
    'test_functions',
    'test_builtins',
    'test_errors',
]
