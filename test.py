""" Tests Trie """

import unittest
from errors import SearchMiss
from trie import Trie
from spellchecker import merge_sort

class TestTrie(unittest.TestCase):
    """ Test Module"""
    seq = ["a", "b", "c", "abc",
           "w", "wo", "wor", "word", "worm",
           "lett", "lette", "letter"]

    def setUp(self):
        """ Setup test """
        self.trie = Trie()

    def tearDown(self):
        """ Teardown test """
        self.trie = None

    def test_add_words(self):
        """ Test add method and words method """
        for w in TestTrie.seq:
            self.trie.add(w)

        self.trie.words_(self.trie.root)
        test_list = sorted(TestTrie.seq)
        i = 0
        for w in sorted(self.trie.print_list):
            self.assertEqual(w, test_list[i])
            i += 1

    def test_find(self):
        """ Test find method """
        for w in TestTrie.seq:
            self.trie.add(w)

        for w in TestTrie.seq:
            self.assertTrue(self.trie.find(w))

    def test_find_error(self):
        """ Test find method raise error if word not in list """
        for w in TestTrie.seq:
            self.trie.add(w)

        with self.assertRaises(SearchMiss) as _:
            for w in TestTrie.seq:
                self.trie.find(w[:-1])

    def test_prefix(self):
        """ Test prefix method """
        for w in TestTrie.seq:
            self.trie.add(w)

        prefix = "let"
        correct = ["lett", "lette", "letter"]
        node = self.trie.root

        for l in prefix:
            node = node[l]
        self.trie.prefix_(node, prefix[:-1])

        i = 0
        for w in sorted(self.trie.print_list):
            self.assertEqual(w, correct[i])
            i += 1

    def test_prefix_error(self):
        """ Test find method raise error if word not in list """
        for w in TestTrie.seq:
            self.trie.add(w)

        prefix = "ran"

        with self.assertRaises(SearchMiss) as _:
            self.trie.words_with_prefix(prefix)

    def test_merge_sort(self):
        """ Test merge_sort function to sort list """
        sorted_list = sorted(TestTrie.seq)
        merge_sort(TestTrie.seq)
        i = 0
        for w in TestTrie.seq:
            self.assertEqual(w, sorted_list[i])
            i += 1

    def test_remove(self):
        """ Test remove method """
        for w in TestTrie.seq:
            self.trie.add(w)

        for w in TestTrie.seq:
            self.assertTrue(self.trie.find(w))

        for w in TestTrie.seq:
            self.trie.remove(w)

        with self.assertRaises(SearchMiss) as _:
            for w in TestTrie.seq:
                self.trie.find(w)


if __name__ == '__main__':
    unittest.main(verbosity=3)
