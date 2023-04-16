import genanki
import os.path
from random import randrange
from genanki import Note
from datetime import datetime

class AnkiWriter:
    def __init__(self, word_list: dict, sounds_dir_path: str) -> None:
        __DECK_ID = randrange(1 << 30, 1 << 31)
        __DECK_NAME = "Simulado"
        __PATH = "/home/nathan/projects/ankicards-automation/src/"
        self.__word_list = word_list
        self.__deck_name = __DECK_NAME
        self.__deck = genanki.Deck(__DECK_ID, __DECK_NAME)
        self.__path = __PATH
        self.__sounds_dir_path = sounds_dir_path

    def execute(self):
        model = self.__create_model()
        notes = self.__create_notes(model)
        for note in notes:
            self.__deck.add_note(note)
        self.__parse_deck_to_anki_apkg()

    def __create_model(self):
        model_id = randrange(1 << 30, 1 << 31)
        model = genanki.Model(model_id, self.__deck_name, fields=[
            {"name": "Question"}, 
            {"name": "Answer"},
            {"name": "Audio"}
        ],
        templates=[
        {
            "name": "Card 1",
            "qfmt": "<h2><center>{{Question}}</center></h2>",
            "afmt": '{{FrontSide}}<br><center><h2>{{' + 'Answer' + '}}</h2></center><br><audio controls src="{{' + 'Audio' + '}}"></audio>',
        }
        ])
        return model

    def __create_notes(self, model) -> list[Note]:
        notes = []
        for word_dict in self.__word_list:
            for word in word_dict:
                meaning = word_dict[word]
                audio_file = self.__get_audio_by_word(word)
                audio = f'[sound:{audio_file}]'
                fields = [word, meaning, audio]
                note = genanki.Note(model, fields)
                notes.append(note)
        return notes
    
    def __get_audio_by_word(self, word: str):
        path_to_word = f'{self.__sounds_dir_path}/pronunciation_ja_{word}.mp3'
        if not os.path.exists(path_to_word):
            return None
        print(os.path.basename(path_to_word))
        return os.path.basename(path_to_word)
        

    def __parse_deck_to_anki_apkg(self):
        date = datetime.now()
        anki_questions_file = self.__path + f"anki_question{date}.apkg"
        genanki.Package(self.__deck).write_to_file(anki_questions_file)