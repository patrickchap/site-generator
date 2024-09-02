import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.value, "This is a paragraph of text.")
        self.assertEqual(leaf.tag, "p")
        self.assertEqual(leaf.props, None)

    def test_to_html(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        leaf = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://example.com">Click me</a>')
