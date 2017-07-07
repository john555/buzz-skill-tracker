class BuzzTracker(object):

    def __init__(self):
        self.skills = {} #skills is a dictionary which contains topics as keys and skills as values
        self.skills_studied = {}

    def add_skills(self):
        topic=input("Enter the name of topic") #eg python
        skill=input("Enter the subsection of that topic") #dictionaries, lists, TDD

        self.skills = {}#the empty dictionary is populated by the topic and subsections

        # eg, skills['python] = ['TDD', 'dictionaries', 'lists']
        #skills becomes skills = {'python': ['TDD', 'dictionaries', 'lists'], .... and others}

<<<<<<< HEAD
    def skills_completed(self,skills):
        """ Function to check and mark completed skills """
        print('Please enter Yes/No for skills you have studied:')
        for topics, skill in skills.items:
            for value in skill:
                user_input = input(value)
                if user_input == 'Yes': 
                    self.skills_studied[topics] = value
                else:
                    pass
        
        return skills_studied

       

    def view_skills_studied(self,skills):
        pass

    def view_skills_not_studied(self,skills):
        pass
=======
    def skills_studied(self):
>>>>>>> 219d9f417bec1c8d778c7ad36399168f8bc7df0b

        pass

    def view_skills_studied(self):
        pass

    def view_skills_not_studied(self):
        pass

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

    def add_topic(self):
        topic = input("Enter a topic: ")

        # Checking whether the input is not blank
        if topic.strip() == '':
            print("The topic cannot be blank")

        # Checking whether the topic already exists
        if topic in self.skills.keys():
            print("This topic already exists")
        else:
            self.skills[topic] = []

<<<<<<< HEAD
=======
    def view_topics_added (self) :
        topics = self.skills

        for topic in topics.keys() :
            print (topic)

if __name__ == "__main__":
    track =  BuzzTracker()
    print (30 * '-')
    print ('Enter: ')
    print ('0 to Add a topic ')
    print ('1.add skills to the tracker ')
    print ('2.show skills that are studied ')
    print ('3. view skills not studied')
    print ('4. Show the Progress of the skills.')
    print ('5. Exit the menu.')
    choice = input('Enter the choice from the menu: 1-5')
>>>>>>> 219d9f417bec1c8d778c7ad36399168f8bc7df0b

    if choice == 0:
        track.add_topic()
    elif choice == 1:
        track.add_skills()

    elif choice == 2:
        track.view_skills_studied()

    elif choice == 3:
        track.view_skills_not_studied()

    elif choice == 4:
        track.progress()

    elif choice == 6:
        print('To exit, press ctr + c ')
    else:
        print ("Wrong input. Enter one of the options to try again.")



