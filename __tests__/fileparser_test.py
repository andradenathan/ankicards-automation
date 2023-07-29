from src.fileparser import FileParser

file_parser = FileParser(
        "./__tests__/resources/words_test",
        "./__tests__/resources/sounds_test"
    )

def test_read_file():
    words_list = file_parser.read_file()
    assert words_list == [
        {"word": "(transliteration1) meaning for testing"},
        {"new word": "(transliteration2) second meaning for another testing"}
    ]