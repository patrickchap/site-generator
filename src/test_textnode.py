import unittest
from textnode import TextNode
from leafnode import LeafNode
from textnode import TextNode, text_node_to_html_node
from enums.textenum import TextType


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


    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        expected_node = LeafNode("b", "This is a text node")
        self.assertEqual(html_node.to_html(), expected_node.to_html())

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        expected_node = LeafNode("i", "This is a text node")
        self.assertEqual(html_node.to_html(), expected_node.to_html())

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        expected_node = LeafNode("a", "This is a text node", {"href": "https://www.example.com"})
        self.assertEqual(html_node.to_html(), expected_node.to_html())

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        expected_node = LeafNode("code", "This is a text node")
        self.assertEqual(html_node.to_html(), expected_node.to_html())

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        print(html_node)
        expected_node = LeafNode("img", "This is a text node", {"src": "https://www.example.com", "alt": "This is a text node"})
        self.assertEqual(html_node.to_html(), expected_node.to_html())
if __name__ == "__main__":
    unittest.main()
