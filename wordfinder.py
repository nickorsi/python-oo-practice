from random import choice as pick_a_word


class WordFinder:
    """WordFinder class finds random words from a list made from a file
    containing only words.
    """
    def __init__(self,file_path):
        """Constructor for WordFinder class, accepts a string representing the
        file path of a given file that should only contains words on each line.
        Creates a attritbute for the file path string and a list of the words
        from the file path. Also invokes the print_word_count function.
        """
        self.file_path = file_path
        self.word_list = self.file_lines_to_list(self.file_path)
        self.print_word_count()

    #TODO: Below may blow up if there's a huge data set, so summarize below without actual list, maybe just length of list
    def __repr__(self):
        return f"<WordFinder file_path={self.file_path} word_list={self.word_list}>"


    #read the file

    #attribute which contains the entire list of words

    #read out number of words read

    def file_lines_to_list(self, file_path):
        """accepts a file path as string; reads file and iterates line-by-line,
        adding each line to a list, removing line breaks, and returns the list
        """
        with open(file_path, "r") as file:
            #TODO: Look at strip() method on word
            word_list = [word.replace("\n", "") for word in file]
            return word_list
    #TODO: May not need an entire new function for the print, could print on the constructor
    def print_word_count(self):
        """Prints a message containing the self.word_list length"""

        print(f"{len(self.word_list)} words read")

    def random(self):
        """picks a random item from word_list property"""
        #TODO: May not want to add an alias to the choice
        return pick_a_word(self.word_list)


wf = WordFinder("words.txt")

print(wf.random())

print(wf.random())

print(wf.random())

print(wf.random())



class RandomWordFinder(WordFinder):
    """RandomWordFinder class, a subclass of WordFinder class that finds random
    words from a list made from a file containing words, whitespace, and
    comments.
    """
    # #TODO: Don't need a constructor UNLESS there is another unique property/input specific to this subclass
    # def __init__(self, file_path):
    #     """Constructor for RandomWordFinder class, accepts a string
    #     representing the file path of a given file that contains words, blank
    #     spaces, and comments. Creates an attritbute for the file path string
    #     and a list of the words from the file path. Also invokes the
    #     print_word_count function.
    #     """
    #     super().__init__(file_path)


    def file_lines_to_list(self, file_path):
        """Method inherited from WordFinder class that accepts a file path as
        string; reads file and iterates line-by-line, adding each line to a
        list, removing line breaks, and returns the list.
        Modified to also ignore words that contain "#" and are empty.
        """
        #TODO: Could get rid of unfilter_list and put the super function directly into the comprehension
        unfilterd_list = super().file_lines_to_list(file_path)
        filterd_list = [word for word in unfilterd_list
                        if "#" not in word and word != ""]
        return filterd_list


rwf = RandomWordFinder("words.txt")

print(rwf.random())

print(rwf.random())

print(rwf.random())

print(rwf.random())