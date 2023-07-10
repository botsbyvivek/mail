from io import StringIO
from html.parser import HTMLParser
import re

class MLStripper(HTMLParser):
  def __init__(self):
    super().__init__()
    self.reset()
    self.strict = False
    self.convert_charrefs = True
    self.text = StringIO()

  def handle_data(self, d):
    self.text.write(d)

  def get_data(self):
    return self.text.getvalue()


def strip_tags(html):
  s = MLStripper()
  s.feed(html)
  return s.get_data()

def strip_script_tags(page_source: str) -> str:
    pattern = re.compile(r'\s?on\w+="[^"]+"\s?')
    result = re.sub(pattern, "", page_source)
    pattern2 = re.compile(r'<script[\s\S]+?/script>')
    result = re.sub(pattern2, "", result)
    return result