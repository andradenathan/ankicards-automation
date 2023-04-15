import unittest
import sys
sys.path.append('../src/fileparser.py')
import fileparser

class FileParserTest(unittest.TestCase):
    def test_read_file(self):
        words_list = fileparser.FileParser("./resources/words_test").read_file()
        print(words_list)
        self.assertEqual(words_list, [
        {"word": "(transliteration1) meaning for testing"},
        {"new word": "(transliteration2) second meaning for another testing"}
    ])


if __name__ == '__main__':
    unittest.main()