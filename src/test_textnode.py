import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.assertEqual(node.url, node2.url)

    def test_not_eq(self):
        node = TextNode("This is a text node diff", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.assertNotEqual(node, node2)

    def type_not_eq(self):
        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "semi-bold", "test.com")
        self.assertNotEqual(node, node2)

    def url_not_eq(self):
        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
