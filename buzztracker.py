class BuzzTracker(object):
    
    def __init__(self):
        self.skills = {} #skills is a dictionary which contains topics as keys and skills as values
        self.skills_studied = {}

    def add_skills(self):
        add_Topic = True
        while add_Topic:
            topic = input("Please enter the name of topic you would like to learn. press, No if there are no more"
                          "Topics you want to add: ")  # eg python
            if topic == 'No':
                add_Topic = False
            else:
                self.skills[topic] = []
                loop = True
                while loop:
                    skill = input("Please enter a subtopic of the topic you would like to learn. press, No if there are no more"
                                  "subtopics to be added:  ") #dictionaries, lists, TDD
                    if skill == 'No':
                        loop = False
                    else:
                        self.skills[topic].append(skill)
                        print (self.skills)

        return self.skills #self.skills = {'python': ['TDD', 'dictionaries', 'lists'], .... and others}

    def skills_completed(self):

        print('Please enter Y/N for skills you have studied: ')
        for topic, skill in self.skills.items():
            if topic not in self.skills_studied:
                self.skills_studied[topic] = []
                #print (topic, skill)
                for value in skill:
                    user_input = input(topic + ', '+ value + ': ' )
                    if user_input == 'Y':
                        self.skills_studied[topic].append(value)
                    else:
                        pass
        print (self.skills_studied)
        
        return self.skills_studied


    def progress(self):
        for item in self.skills:
            if item in self.skills_studied:
                if len(self.skills_studied[item]) == len(self.skills[item]):
                    print  ('Congratulations!! ' + item + ' is complete! ')

                    print ('skills covered: ')
                    for i in self.skills_studied[item]:
                        print (i)
                else:
                    print (item + ' is Incomplete\n')
                    print ('skills covered: ')
                    for i in self.skills_studied[item]:
                        print (i)
                    print ('\n' + 'skills yet to be covered:')
                    for i in self.skills[item]:
                        if i not in self.skills_studied[item]:
                            print (i)

if __name__ == "__main__":
    track =  BuzzTracker()
    print (30 * '-')

    track.add_skills()
    print (30 * '-')
    track.skills_completed()
    print (30 * '-')
    track.progress()




