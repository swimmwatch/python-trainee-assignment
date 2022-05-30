from typing import Type

import pytest

from usefullib import Matrix2D, spiral_order


@pytest.mark.parametrize('matrix,expected', [
    ([], []),
    ([[1]], [1]),
    (
        [
            [1, 2],
            [3, 4]
        ],
        [1, 3, 4, 2]
    ),
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [1, 4, 7, 8, 9, 6, 3, 2, 5]
    )
])
def test_spiral_order(matrix: Matrix2D[int], expected: list[int]):
    actual = list(spiral_order(matrix))
    assert expected == actual


@pytest.mark.parametrize('matrix,expected_exception', [
    ([[]], ValueError),
    ([[1, 2]], ValueError),
    ([[1], [2]], ValueError)
])
def test_spiral_order_negative_cases(matrix: Matrix2D[int], expected_exception: Type[Exception]):
    with pytest.raises(expected_exception):
        list(spiral_order(matrix))
