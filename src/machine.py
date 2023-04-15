class Machine:
    def __init__(self, driver, word_list) -> None:
        self.driver = driver
        self.word_list = word_list

    def download(self, url):
        suffix = "ADD_WORD_HERE/#ja"
        try:
            pass
        except:
            print("Error trying to download file from URL: " + url)