import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = { "href": "https://www.google.com", "target": "_blank" })
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(tag = "a", value = "click", props = { "href": "https://www.google.com", "target": "_blank" })
        expected = "HTMLNode(a, click, [], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()