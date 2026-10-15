"""HW5 Question 1 Tests"""


import sys

sys.path.append('.')
from src.q1 import replace_word, WordPair

class TestReplaceWord:
    """Tests for the replace_word function."""
    def test_replace_word(self) -> None:
        """Tests the replace_word function"""
        assert replace_word("drums guitar drums", WordPair("drums", "piano")) == "piano guitar piano"
        assert replace_word("hello world", WordPair("world", "ava")) == "hello ava"
