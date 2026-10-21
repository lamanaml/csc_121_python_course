import pytest
from book_tracker import estimate_reading_time, format_book

def test_estimate_whole_hours():
    # assert that 40 pages returns 1.0
    # assert that 400 pages returns 10.0
    assert estimate_reading_time(40) == 1.0
    assert estimate_reading_time(400) == 10.0


def test_estimate_rounds_to_one_decimal():
    # assert that 438 pages returns 10.9
    # assert that 412 pages returns 10.3
    assert estimate_reading_time(438) == 10.9
    assert estimate_reading_time(412) == 10.3


def test_estimate_zero():
    # assert that 0 pages returns 0.0
    assert estimate_reading_time(0) == 0.0

def test_estimate_str():
    # use with pytest.raises(TypeError):
    # call estimate_reading_time with a string like "cat"
    # (you can't divide a string by 40, so Python should raise a TypeError)
    with pytest.raises(TypeError):
        estimate_reading_time("cat")
    
    # --- format_book ---
def test_format_book():
    # create a book dictionary for Dune by Frank Herbert, 412 pages, 10.3 hours
    book = {
        "title": "Dune",
        "author": "Frank Herbert",
        "pages": 412,
        "hours": 10.3
    }
    # assert that format_book(book, 1) returns exactly:
    #   "1. 'Dune' - Frank Herbert (412 pages - approx. 10.3 hours to read)"
    assert format_book(book, 1) == ("1. 'Dune' - Frank Herbert (412 pages - approx. 10.3 hours to read)")


def test_format_book_comma_in_title():
    # create a book dictionary for The Long Way To A Small, Angry Planet
    #   by Becky Chambers, 438 pages, 10.9 hours
    book = {
        "title": "The Long Way To A Small, Angry Planet",
        "author": "Becky Chambers",
        "pages": 438,
        "hours": 10.9
    }
    # assert that format_book(book, 2) returns the line starting with "2. "
    assert format_book(book, 2)[:3] == ("2. ")

