import re

class FileParser:
    def __init__(self, path) -> None:
        self.path = path
        self.word_list = []
        self.REGEX_ALL_CHARS = '\(.*?\)'
        self.REGEX_PARENTHESES = r'\([^)]*\)'

    def read_file(self) -> list[str]:
        with open(self.path, 'r') as file:
            for line in file:
                word_meaning_list = [self.process_word(line)]
                self.word_list.append(dict(word_meaning_list))
        return self.word_list

    def process_word(self, line: str) -> str | None:
        word = line.strip().split(":")
        if len(word) < 2:
            return None
        
        transliteration = re.findall(self.REGEX_ALL_CHARS, word[0])
        word[0] = re.sub(self.REGEX_PARENTHESES, '', word[0]).strip()
        word[1] = "".join(transliteration) + " " + word[1].lstrip() if transliteration else word[1].lstrip()
        print(word)
        return word