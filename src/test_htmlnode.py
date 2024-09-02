import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    #test tags
    def test_tags(self):
        node = HTMLNode('div')
        self.assertEqual(node.tag, 'div')
    #test value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    def test_value(self):
        node = HTMLNode('div', value='Hello World')
        self.assertEqual(node.value, 'Hello World')

    #test children - A list of HTMLNode objects representing the children of this node
    def test_children(self):
        node = HTMLNode('div', children=[HTMLNode('p')])
        self.assertNotEqual(node.children, None)
        self.assertEqual(len(node.children), 1)

    #test props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def test_props(self):
        node = HTMLNode('a', props={'href': 'https://www.google.com'})
        self.assertEqual(node.props['href'], 'https://www.google.com')

    # test props_to_html
    def test_props_to_html(self):
        node = HTMLNode('a', props={'href': 'https://www.google.com'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_two(self):
        node = HTMLNode('a', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

