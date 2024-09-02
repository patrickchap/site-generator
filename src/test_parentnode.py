import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        p = ParentNode('p', [LeafNode("p", "hello")])
        self.assertEqual(p.tag, 'p')
    
    def test_to_html(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_nested_parents(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),])
        node2 = ParentNode("div",[node])
        self.assertEqual(node2.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")

