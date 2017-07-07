"""
This module is for storing and manipulating data
"""

class Store():
    def __init__(self):
        self.__data = dict()
    
    def add_topic(self, topic):
        """adds a new topic"""
        self.__data[topic] = list()
    
    def add_skill(self, topic, skill_name):
        """adds a new skill """
        skill = dict(name=skill_name, is_complete=False)
        self.__data[topic].append(skill)
    
    def total(self):
        return len(self.__data)

    def print(self): # junk method
        """for debugging"""
        print(self.__data)

    
    def get_topics(self):
        """returns a list of topics"""
        topics = []

        for topic in self.__data:
            topics.append(topic.name)
        return topics;