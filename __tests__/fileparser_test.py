import sys
sys.path.append('../src/fileparser.py')
from src.fileparser import FileParser

def test_read_file():
    words_list = FileParser("./resources/words_test").read_file()
    assert words_list == [
    {"word": "(transliteration1) meaning for testing"},
    {"new word": "(transliteration2) second meaning for another testing"}
]