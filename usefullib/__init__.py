import math
from http import HTTPStatus
from http.client import HTTPException
from typing import List, Iterable

import httpx
import numpy as np

from usefullib.types import Matrix2D
from usefullib.utils import extract_nums


def spiral_order(matrix: Matrix2D[int]) -> Iterable[int]:
    """
    Iterate over matrix 2D in spiral order
    (counterclockwise, starting from the upper left corner).

    :param matrix: Matrix 2D
    :return: Iterator
    """
    rows = len(matrix)
    if not rows:
        return iter([])

    cols = len(matrix[0])
    if not cols:
        raise ValueError('Incorrect matrix: no columns')

    if rows != cols:
        raise ValueError('Matrix must be square')

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    direction = 0
    while top <= bottom and left <= right:
        if direction == 0:
            # moving top->bottom
            for i in range(top, bottom + 1):
                yield matrix[i][left]

            left += 1
            direction = 1
        elif direction == 1:
            # moving left->right
            for i in range(left, right + 1):
                yield matrix[bottom][i]

            bottom -= 1
            direction = 2
        elif direction == 2:
            # moving bottom->top
            for i in range(bottom, top - 1, -1):
                yield matrix[i][right]

            right -= 1
            direction = 3
        elif direction == 3:
            # moving right->left
            for i in range(right, left - 1, -1):
                yield matrix[top][i]

            top += 1
            direction = 0


async def get_matrix(url: str) -> List[int]:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != HTTPStatus.OK:
            raise HTTPException(
                f'Request was unsuccessful: {HTTPStatus(resp.status_code)}'
            )
        nums = list(extract_nums(resp.text))
        dim = int(math.sqrt(len(nums)))
        matrix = np.reshape(nums, (dim, dim))
    return list(spiral_order(matrix))
