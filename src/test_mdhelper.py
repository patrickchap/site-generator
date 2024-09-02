import unittest
from textnode import TextNode
from leafnode import LeafNode
from convert import text_node_to_html_node
from enums.textenum import TextType
from mdhelper import split_nodes_delimiter

class TestMdHelper(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(len(new_nodes), 3)
