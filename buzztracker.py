import store

def main():
    _store = store.Store()
    
    print(15 * '-', "-MENU" ,15 * '-')
    print('0. Add a topic')
    print ('1.add skills to the tracker ')
    print ('2.show skills that are studied ')
    print ('3.view skills studied. ')
    print ('4. view skills not studied')
    print ('5. Show the Progress of the skills.')
    print ('6. Exit the menu.')

    while True:

        choice = input('What you like to do?\nSelect(0-5):')
        
        if choice == 0:
            # add a new topic
            pass
        if choice==1:
            # add a new skill to a topic
            pass

        if choice==2:
            # add show skills that are studied
            pass
        if choice==3:
            # view skills studied
            pass

        # you get the idea

if __name__ == "__main__":
    main()