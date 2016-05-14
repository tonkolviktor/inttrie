from inttrie import *
import unittest

class TestIntTrieMethods(unittest.TestCase):

    def test_contains(self):
        # given
        a = IntDecimalStorage(12345)
        trie = IntDecimalTrie()
        # when
        trie.insert(a, 1)
        # then
        self.assertTrue(trie.contains(a))

    def test_not_contains(self):
        # given
        a = IntDecimalStorage(12345)
        trie = IntDecimalTrie()
        # when
        trie.insert(a, 1)
        # then
        self.assertFalse(trie.contains(IntDecimalStorage(12346)))
        self.assertFalse(trie.contains(IntDecimalStorage(1234)))
        self.assertFalse(trie.contains(IntDecimalStorage(123456)))
        self.assertFalse(trie.contains(IntDecimalStorage(23456)))

if __name__ == '__main__':
    unittest.main()