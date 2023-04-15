import genanki
from random import randrange
from genanki import Note
from datetime import datetime

class AnkiWriter:
    def __init__(self, word_list: dict) -> None:
        __DECK_ID = randrange(1 << 30, 1 << 31)
        __DECK_NAME = "Simulado"
        __PATH = "/home/nathan/projects/ankicards-automation/src/"
        self.__word_list = word_list
        self.__deck_name = __DECK_NAME
        self.__deck = genanki.Deck(__DECK_ID, __DECK_NAME)
        self.__path = __PATH

    def execute(self):
        model = self.__create_model()
        notes = self.__create_notes(model)
        for note in notes:
            self.__deck.add_note(note)
        self.parse_deck_to_anki_apkg()

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
            "afmt": "{{FrontSide}}<hr id=answer><h2><center>{{Answer}}</center></h2>",
        }
        ])
        return model

    def __create_notes(self, model) -> list[Note]:
        notes = []
        # TODO: Create a note for each word in the word_list from the given dictionary
        # and append every note in the notes list.
        fields = [self.question, self.answer]

        note = genanki.Note(model=model, fields=fields)
        # TODO: Return the notes list
        return note
    
    def __parse_deck_to_anki_apkg(self):
        date = datetime.now()
        anki_questions_file = self.__path + f"anki_question{date}.apkg"
        genanki.Package(self.__deck).write_to_file(anki_questions_file)