""" SpellChecker module """

import sys
import inspect
from trie import Trie
from errors import SearchMiss

class SpellChecker:
    """ Handler class """

    options = {
        "1": "check_word",
        "2": "get_word_suggestion",
        "3": "change_dictionary",
        "4": "print_all",
        "5": "remove_word",
        "q": "quit"
    }

    def __init__(self):
        """ Initialize class """
        self.trie = Trie()
        self.filename = "tiny_dictionary.txt"
        self.load()
        self.start()

    def load(self):
        """ Load text file """
        try:
            self.trie = Trie()
            with open(self.filename, 'r') as fn:
                for word in fn:
                    self.trie.add(word)
        except FileNotFoundError:
            print('file does not exist')

    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self.options[method_name])


    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in sorted(self.options):
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def check_word(self):
        """ Check a word """
        value = input("enter a word: ")
        try:
            self.trie.find(value.lower())
            print("The word was spelled correctly!")
        except SearchMiss as e:
            print(f"Error: {e}")

    def get_word_suggestion(self):
        """ Get word suggestion"""
        value = input("Enter a prefix with 3 letters: ")
        if len(value) == 3:
            try:
                self.trie.words_with_prefix(value)
            except SearchMiss as e:
                print(f"Error: {e}")
        else:
            print("Invalid prefix")

    def change_dictionary(self):
        """ Change the dictionary """
        self.filename = input("Choose file: ")
        self.load()

    def print_all(self):
        """ Print all words in dictionary """
        word_list = self.trie.all_words()
        if len(word_list) == 0:
            print("There are no words in the dictionary")
        merge_sort(word_list)
        for w in word_list:
            print(w)

    def remove_word(self):
        """ Remove a word from dictionary """
        value = input("enter a word: ")
        try:
            print(self.trie.remove(value.lower()) + " was removed from dictionary")
        except SearchMiss as e:
            print(f"Error: {e}")

    @staticmethod
    def quit():
        """ Quit the program """
        sys.exit()

    def start(self):
        """ Start method """

        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")

            input("\nPress any key to continue ...")

def merge_sort(unsorted):
    """ Sort list """
    if len(unsorted) > 1:
        middle = len(unsorted) // 2
        left = unsorted[:middle]
        right = unsorted[middle:]

        merge_sort(left)
        merge_sort(right)
        (m, i, j) = (0, 0, 0)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted[m] = left[i]
                i += 1
            else:
                unsorted[m] = right[j]
                j += 1
            m += 1

        while i < len(left):
            unsorted[m] = left[i]
            i += 1
            m += 1

        while j < len(right):
            unsorted[m] = right[j]
            j += 1
            m += 1

if __name__ == "__main__":
    SpellChecker()
