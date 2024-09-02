from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, children=children)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")
        if not self.children:
            raise ValueError("children is required")
    
        html = ""
        for child in self.children:
            html += f"{child.to_html()}"

        return f"<{self.tag}>{html}</{self.tag}>"
