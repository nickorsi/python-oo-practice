from random import choice as pick_a_word


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        self.file_path = file_path
        self.word_list = self.file_lines_to_list(self.file_path)
        self.print_word_count()


    def __repr__(self):


    #read the file

    #attribute which contains the entire list of words

    #read out number of words read

    def file_lines_to_list(self, file):
        """accepts a file path as string; reads file and iterates line-by-line,
        adding each line to a list and returns the list"""

        with open(file,"r") as word_file

        word_list = [word for word in word_file]

        return word_list

    def print_word_count(self,list):
        """accepts a list, prints a message containing the list length"""

        print(f"{len(list)}" words read)

    def random(self):
        """picks a random item from word_list property"""
        return pick_a_word(self.word_list)







