class FileParser:
    def __init__(self, path) -> None:
        self.path = path
        self.word_list = []

    def read_file(self) -> list[str]:
        with open(self.path, 'r') as file:
            for line in file:
                word_meaning_list = [self.process_word(line)]
                self.word_list.append(dict(word_meaning_list))
        return self.word_list

    def process_word(self, line: str) -> str:
        word = line.strip().split(":")
        if len(word) < 2:
            return None

        word[1] = word[1].lstrip()
        return word