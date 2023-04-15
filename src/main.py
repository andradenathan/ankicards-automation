#!/usr/bin/python3 
import os
from chromedriver import ChromeDriver
from fileparser import FileParser
from machine import Machine
from ankiwriter import AnkiWriter
from dotenv import load_dotenv

load_dotenv()
WORDS_PATH = os.getenv("WORDS_PATH")
SOUNDS_DIR_PATH = os.getenv("SOUNDS_DIR_PATH")
FORVO_WORD_URL_BASE = os.getenv("FORVO_WORD_URL_BASE")

if __name__ == "__main__":
    word_list = FileParser(WORDS_PATH).read_file()

    chrome_driver = ChromeDriver(SOUNDS_DIR_PATH)
    driver = chrome_driver.setup()
    
    #TODO: Make the request here
    machine = Machine(driver, word_list)
    machine.download(FORVO_WORD_URL_BASE)

    #TODO: 
    writer = AnkiWriter(word_list)
    writer.execute()