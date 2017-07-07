class buzztracker(object):
    def __init__(self,skills):
        #self.skills=skills
        #x=''
        #y=[]
        #self.skills={'name':x,'skills':y}

           
                




        def add_skills(self,skills):
            name=input("Enter the name of skill")
            topic=input("Enter topic to be done")


            skills={name:'',
                    status_completion:False
                            }
           data=[{
               "topic1":"",
               skills:[skills,skills,skills]

               "topic2":'',
               skills:[skills,skills,skills]
               "topic3":"",
               skills:[skills,skills,skills]
           }]

        def skills_studied(self,skills):

        def view_skills_studied(self,skills):

        def view_skills_not_studied(self,skills):

        def progress(self,skills):


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