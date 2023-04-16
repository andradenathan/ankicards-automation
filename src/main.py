#!/usr/bin/python3 
import os
import os.path
import subprocess
from chromedriver import ChromeDriver
from fileparser import FileParser
from machine import Machine
from ankiwriter import AnkiWriter
from dotenv import load_dotenv

load_dotenv()
WORDS_PATH = os.getenv("WORDS_PATH")
SOUNDS_DIR_PATH = os.getenv("SOUNDS_DIR_PATH")
FORVO_WORD_URL_BASE = os.getenv("FORVO_WORD_URL_BASE")
COLLECTION_MEDIA_PATH = os.getenv("COLLECTION_MEDIA_PATH")

if __name__ == "__main__":
    word_list = FileParser(WORDS_PATH, SOUNDS_DIR_PATH).read_file()
    
    chrome_driver = ChromeDriver(SOUNDS_DIR_PATH)
    driver = chrome_driver.setup()
    
    machine = Machine(driver, word_list)
    machine.download(FORVO_WORD_URL_BASE)

    writer = AnkiWriter(word_list, SOUNDS_DIR_PATH)
    writer.execute()
    
    subprocess.call(["mv", SOUNDS_DIR_PATH, os.path.abspath(COLLECTION_MEDIA_PATH)])
    