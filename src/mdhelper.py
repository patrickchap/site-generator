from enums.textenum import TextType
from textnode import TextNode

'''
class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    LINK = 4
    CODE = 5
    IMAGE = 6

'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split the nodes using the delimiter and return the new nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(split_text_node(node, delimiter))
        else:
            new_nodes.append(node)
    return new_nodes

def split_text_node(node, delimiter):
    """
    Split the text node using the delimiter and return the new nodes.
    Example: "This is text with a `code block` word"
    delimiter = "`"
    should find an open and closed delimiter and split the text node into three nodes. If matching delimiter is not found, raise exception.
    return 
    [
        TextNode("This is text with a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" word", text_type_text),
    ]
    """
    new_nodes = []
    count = node.text.count(delimiter)
    if count % 2 != 0:
        raise Exception("Delimiter count is not even")
    if count == 2:
        open_delimiter = node.text.find(delimiter)
        close_delimiter = node.text.find(delimiter, open_delimiter + 1)

        new_nodes.append(TextNode(node.text[:open_delimiter], TextType.TEXT))
        new_nodes.append(TextNode(node.text[open_delimiter + 1:close_delimiter], TextType.CODE))
        new_nodes.append(TextNode(node.text[close_delimiter + 1:], TextType.TEXT))

    return new_nodes

