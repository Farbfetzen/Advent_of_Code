from typing import Callable, Type, Union
from unittest import skip, TestCase

from test.parse_test_args import parsed_args


_T = Union[Type[TestCase], Callable[..., None]]


def sample(test_item: _T) -> _T:
    if parsed_args.skip_samples:
        return skip("sample data")(test_item)
    return test_item
