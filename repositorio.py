import json
import os


class RepositorioProfessionalProfile:
    def __init__(self):
        self.profiles = {}
        self.load()

    def save(self, profiles):
        self.profiles.append(profiles)

    def load(self):
        profiles_data = {}
        if os.path.exists('data.json'):
            with open('data.json') as f:
                profiles_data = json.load(f)
        self.profiles = profiles_data
