import pytest

from usefullib import extract_nums


@pytest.mark.parametrize('enter,expected', [
    ('', []),
    ('1', [1]),
    ('1 2 3', [1, 2, 3])
])
def test_extract_nums(enter: str, expected: list[int]):
    actual = list(extract_nums(enter))
    assert actual == expected
