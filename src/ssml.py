#!/usr/bin/env python3
"""
SSML (Speech Synthesis Markup Language) is a subset of XML specifically
designed for controlling synthesis. You can see examples of how the SSML
should be parsed in the unit tests below.
"""

#
# DO NOT USE CHATGPT, COPILOT, OR ANY AI CODING ASSISTANTS.
# Conventional auto-complete and Intellisense are allowed.
#
# DO NOT USE ANY PRE-EXISTING XML PARSERS FOR THIS TASK - lxml, ElementTree, etc.
# You may use online references to understand the SSML specification, but DO NOT read
# online references for implementing an XML/SSML parser.
#


from dataclasses import dataclass
from typing import List, Union, Dict
import re

SSMLNode = Union["SSMLText", "SSMLTag"]


@dataclass
class SSMLTag:
    name: str
    attributes: dict[str, str]
    children: list[SSMLNode]

    def __init__(
        self, name: str, attributes: Dict[str, str] = {}, children: List[SSMLNode] = []
    ):
        self.name = name
        self.attributes = attributes
        self.children = children


@dataclass
class SSMLText:
    text: str

    def __init__(self, text: str):
        self.text = text


def parseSSML(ssml: str) -> SSMLNode:
    tag_regex = re.compile(r'<\s*(/?)\s*(\w+)([^>]*)>|([^<]+)')
    stack = []
    root = SSMLTag("root", {}, [])
    stack.append(root)

    for match in tag_regex.finditer(ssml):
        if match.group(4):  # Text
            text = match.group(4)  # no .strip()
            if text:
                stack[-1].children.append(SSMLText(unescapeXMLChars(text)))
        else:
            closing, tag_name, attr_st = match.group(1), match.group(2), match.group(3)
            if "'" in attr_st:
                raise Exception("Invalid attribute format")

            if closing:
                if stack[-1].name == tag_name:
                    node = stack.pop()
                    stack[-1].children.append(node)
            else:
                attrs = dict(re.findall(r'([:\w]+)="(.*?)"', attr_st))
                is_self_closing = attr_st.strip().endswith('/')
                tag = SSMLTag(tag_name, attrs, [])
                if is_self_closing:
                    stack[-1].children.append(tag)
                else:
                    stack.append(tag)

    if len(root.children) != 1 or not isinstance(root.children[0], SSMLTag) or root.children[0].name != "speak":
        raise Exception("Must have one top-level <speak> tag")
    else:
        return root.children[0]




def ssmlNodeToText(node: SSMLNode) -> str:
    if isinstance(node, SSMLText):
        return escapeXMLChars(node.text)
    return f"<{node.name}>{''.join(ssmlNodeToText(c) for c in node.children)}</{node.name}>"



def unescapeXMLChars(text: str) -> str:
    return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def escapeXMLChars(text: str) -> str:
    return text.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

# Example usage:
# ssml_string = '<speak>Hello, <break time="500ms"/>world!</speak>'
# parsed_ssml = parseSSML(ssml_string)
# text = ssmlNodeToText(parsed_ssml)
# print(text)