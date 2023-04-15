#!/usr/bin/python3 
from chromedriver import ChromeDriver
from fileparser import FileParser
from machine import Machine
from ankiwriter import AnkiWriter

if __name__ == "__main__":
    word_list = FileParser("../words").read_file()
    
    chrome_driver = ChromeDriver("/home/nathan/projects/ankicards-automation/files")
    driver = chrome_driver.setup()
    
    #TODO: Make the request here
    machine = Machine(driver, word_list)
    machine.download("https://pt.forvo.com/word/")

    #TODO: 
    writer = AnkiWriter(word_list)
    writer.execute()