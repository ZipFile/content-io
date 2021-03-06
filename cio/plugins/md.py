# coding=utf-8
from __future__ import unicode_literals

from .txt import TextPlugin


class MarkdownPlugin(TextPlugin):

    ext = 'md'

    def render(self, data):
        # TODO: Handle markdown import error
        import markdown
        if data:
            extensions = self.settings.get('EXTENSIONS', [])
            return markdown.markdown(data, extensions=extensions)
