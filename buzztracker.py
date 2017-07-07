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

    def skills_studied(self):
    
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

    def view_topics_added (self) :
        topics = self.skills

        for topic in topics.keys() :
            print (topic)

if __name__ == "__main__":
    track =  BuzzTracker()
    print (10 * '-',"Welcome to the Buzz project Tracker.",10*'-' ) #updated the menu to work appropriately.
    print ('Enter: ')
    print ('0 to Add a topic ')
    print ('1.add skills to the tracker ')
    print ('2.show skills that are studied ')
    print ('3. view skills not studied')
    print ('4. Show the Progress of the skills.')
    print ('5. View topics added.')
    print ('6. Exit the menu.')
    choice = int(input('Enter the choice from the menu: 1-5: ')) #updated the input value to return an int.

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

    elif choice == 5:
        track.view_topics_added()       #the numbering of the files was off just updated that.
    
    elif choice==6:
        print('Print exiting the menu')
        exit()

    else:
        print("Input a correct number.")



