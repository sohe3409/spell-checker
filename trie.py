""" Trie module """

from node import Node
from errors import SearchMiss

class Trie():
    """ Trie class """
    def __init__(self):
        self.root = Node()
        self.print_list = []

    def add(self, word):
        """ Add dictionary """
        word = word.strip()
        node = self.root
        for l in word:
            next_node = node[l]
            if next_node is not None:
                node = next_node
            else:
                node[l] = Node(l)
                node = node[l]
        node.stop = True

    def find(self, word):
        """ find word """
        node = self.root
        for l in word:
            if l not in node:
                raise SearchMiss
            node = node[l]
        if node.stop:
            return True
        raise SearchMiss

    def all_words(self):
        """ Print all words """
        self.print_list = []
        node = self.root
        self.words_(node)
        return self.print_list

    def words_(self, node, word=""):
        """ Print all words """
        if node.stop:
            self.print_list.append(word + node.value)
        for child in node.children.values():
            if node.value is None:
                self.words_(child)
            else:
                self.words_(child, (word + node.value))

    def words_with_prefix(self, prefix):
        """ Print maximum 10 words that starts with prefix """
        self.print_list = []
        node = self.root
        for l in prefix:
            if l not in node:
                raise SearchMiss
            node = node[l]
        self.prefix_(node, prefix[:-1])

        for word in self.print_list[:10]:
            print(word)
        self.print_list = []

        inp = input("Add another letter to prefix or type quit to exit: " + prefix)
        if inp == "quit":
            print("Done")
        elif len(inp) != 1:
            print("Too few or many letters were added")
        else:
            self.words_with_prefix(prefix + inp)

    def prefix_(self, node, prefix):
        """ Add words to list """
        if node.stop:
            self.print_list.append(prefix + node.value)
        for child in node.children.values():
            self.prefix_(child, (prefix + node.value))


    def remove(self, word):
        """ remove word """
        if self.find(word):
            return self.remove_(word)
        raise SearchMiss

    def remove_(self, word):
        """ remove word """
        node = self.root
        last = word[-1]
        if word == last:
            if node[last].children:
                node[last].stop = False
            else:
                del node.children[last]
            return word

        for l in word[:-1]:
            node = node[l]

        if last in node.children and node[last].stop is True:
            node[last].stop = False

        if len(node.children) == 1:
            if node[last].no_children():
                del node.children[last]
            if len(word) >= 1 and node.stop is False:
                self.remove_(word[:-1])

        if len(node.children) > 1:
            if len(node[last].children) >= 1:
                node[last].stop = False
            else:
                del node.children[last]
        return word
