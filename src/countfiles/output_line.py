from typing import Dict, Optional

from colorama import Style


class OutputLine:
    text: str = ""
    colors: Dict[int, str]

    def __init__(self, text: str = "", colors: Optional[Dict[int, str]] = None):
        self.text = text
        self.colors = colors or {}
        self.append_color(Style.RESET_ALL)

    @property
    def colored(self):
        text = self.text
        for pos in sorted(self.colors, reverse=True):
            text = text[:pos] + self.colors[pos] + text[pos:]
        return text

    @property
    def length(self):
        return len(self.text)

    def append(self, text: str, color: str = ""):
        if color:
            self.append_color(color)
        self.text += text
        if color:
            self.append_color(Style.RESET_ALL)

    def append_color(self, color: str):
        pos = len(self.text)
        if pos in self.colors:
            self.colors[pos] += color
        else:
            self.colors[pos] = color

    def clone(self):
        return OutputLine(text=self.text, colors=self.colors.copy())

    def truncate(self, max_length: int):
        if max_length >= len(self.text):
            return self
        return OutputLine(
            text=self.text[:max_length - 3] + "...",
            colors={k: v for k, v in self.colors.items() if k <= max_length - 3},
        )
