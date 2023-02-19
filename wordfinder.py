"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:

    def __init__(self, path):
        '''Read word file, add words to word list, and print number of words'''
        file = open(path, "r")
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, word_file):
        return [w.strip() for w in word_file]

    def random(self):
        '''Return random word'''
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale", "parsnips"]
    True

    >>> swf.random() in ["pear", "carrot", "kale", "parsnips"]
    True

    >>> swf.random() in ["pear", "carrot", "kale", "parsnips"]
    True
    """

    def parse(self, word_file):
        return [w.strip() for w in word_file if w.strip() and not w.startswith("#")]
