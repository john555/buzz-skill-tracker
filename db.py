"""
This module is for storing and manipulating data
"""

class Db():
    def __init__(self):
        self.__data = dict()
    
    def add_topic(self, slug, name):
        self.__data[slug] = dict(name=name, skills=list())
    
    def add_skill(self, slug, name):
        skill = dict(name=name, is_complete=False)
        self.__data[slug]["skills"].append(skill)
    
    def total(self):
        return len(self.__data)
    