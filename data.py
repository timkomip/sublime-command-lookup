import pyjson5
from os import path
from flask import current_app, g

class CommandSearcher:
    def __init__(self, file_path):
        self.file_path = file_path
        self.commands = []

    def load_commands(self):
        with open(self.file_path, 'r',encoding='UTF-8') as f:
            new_commands = pyjson5.decode(f.read())
            self.commands = self.commands + new_commands
    
    def search(self, query):
        if not query:
            return 
        for command in self.commands:
            caption = command.get('caption','').lower()
            if query.lower() in caption:
                yield command

def get_searcher():
    if 'searcher' not in g:
        file_path = path.join(current_app.root_path, 'data', 'merge', 'Default.sublime-commands')
        g.searcher = CommandSearcher(file_path)
        g.searcher.load_commands()
    return g.searcher



