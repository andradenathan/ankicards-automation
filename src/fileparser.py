import re
import os.path
from dotenv import load_dotenv

load_dotenv()

class FileParser:
    def __init__(self, words_path, sounds_dir_path) -> None:
        self.__words_path = words_path
        self.__word_list = []
        self.REGEX_ALL_CHARS_BETWEEN_PARENTHESES = '\(.*?\)'
        self.REGEX_PARENTHESES = r'\([^)]*\)'
        if not os.path.exists(os.path.basename(sounds_dir_path)):
            os.mkdir(os.path.basename(sounds_dir_path))
        

    def read_file(self) -> list[str]:
        with open(self.__words_path, 'r') as file:
            for line in file:
                word_meaning_list = [self.process_word(line)]
                self.__word_list.append(dict(word_meaning_list))
        return self.__word_list

    def process_word(self, line: str) -> str | None:
        word = line.strip().split(":")
        if len(word) < 2:
            return None
        
        transliteration = re.findall(
            self.REGEX_ALL_CHARS_BETWEEN_PARENTHESES, 
            word[0]
                )       

        word[0] = re.sub(self.REGEX_PARENTHESES, '', word[0]).strip()
        word[1] = "".join(transliteration) + " " + word[1].lstrip() if transliteration else word[1].lstrip()
        return word