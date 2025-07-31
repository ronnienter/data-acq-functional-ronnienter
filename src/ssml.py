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
    # TODO: implement this function
    raise NotImplementedError()


def ssmlNodeToText(node: SSMLNode) -> str:
    # TODO: implement this function
    raise NotImplementedError()


def unescapeXMLChars(text: str) -> str:
    return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def escapeXMLChars(text: str) -> str:
    return text.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

# Example usage:
# ssml_string = '<speak>Hello, <break time="500ms"/>world!</speak>'
# parsed_ssml = parseSSML(ssml_string)
# text = ssmlNodeToText(parsed_ssml)
# print(text)