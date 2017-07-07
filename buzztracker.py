class buzztracker(object):
    def __init__(self):
        self.skills #skills is a dictionary which contains topics as keys and skills as values
        self.skills_completed # Dictionary containing skills completed

    def add_skills(self):
        topic=input("Enter the name of topic") #eg python
        skill=input("Enter the subsection of that topic") #dictionaries, lists, TDD

        skills = {}#the empty dictionary is populated by the topic and subsections
        # eg, skills['python] = ['TDD', 'dictionaries', 'lists']
        #skills becomes skills = {'python': ['TDD', 'dictionaries', 'lists'], .... and others}

    def skills_studied(self,skills):

    def view_skills_studied(self,skills):

    def view_skills_not_studied(self,skills):

    def progress(self,skills):

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


    def display_menu():
        print 30*'-',MENU ,30 * '-'
        print '0. Add a topic'
        print '1.add skills to the tracker '
        print '2.show skills that are studied '
        print '3.view skills studied. '
        print '4. view skills not studied'
        print '5. Show the Progress of the skills.'
        print '6. Exit the menu.'

        loop=True

        while loop:
            display_menu()
            choice=input('Enter the choice from the menu: 1-5')

            if choice==0:
                add_topic()
            if choice==1:
                add_skills()

            if choice==2:
                skills_studied()

            if choice==3:
                view_skills_studied()

            if choice==4:
                view_skills_not_studied()
                
            if choice==5:
                progress()

            if choice==6:
                print('Exiting the menu')
                return
            else:
                raw_input=("Wrong input. Enter one of the options to try again.")
