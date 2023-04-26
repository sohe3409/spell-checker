""" Node module """

class Node():
    """ Trie Node class """
    def __init__(self, value=""):
        self.value = value
        self.children = {}
        self.stop = False

    def no_children(self):
        """ Checks if node has any children """
        return len(self.children) == 0

    def __getitem__(self, key):
        if key in self.children:
            return self.children[key]
        return None

    def __setitem__(self, key, value):
        self.children[key] = value

    def __contains__(self, value):
        return value in self.children
