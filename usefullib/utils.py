"""
Some utilities.
"""
import re
from typing import Iterable


def extract_nums(content: str) -> Iterable[int]:
    """
    Extract numbers from string.

    :param content: Input string
    :return: Parsed numbers
    """
    pattern = re.compile(r'\d+')
    matches = re.findall(pattern, content)
    return (int(match) for match in matches)
