#!/usr/bin/python3
"""
Write a function named index_range that takes
two integer arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Simple Helper Function

    Args:
        page -> The page number
        page_size -> The size of data to be accomodated

    Return:
        Tuple of size two with
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
