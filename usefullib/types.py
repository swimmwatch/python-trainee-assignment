"""
Aliases for type annotations.
"""
from collections.abc import Sequence
from numbers import Number
from typing import TypeVar

T = TypeVar('T', int, float, Number)
Matrix2D = Sequence[Sequence[T]]
