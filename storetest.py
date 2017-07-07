import unittest, store

class Test(unittest.TestCase):

    def test_add_topic(self):
        _store = store.Store()
        name = "Java programming"
        _store.add_topic(name)

        self.assertEqual(1, _store.total())

        name = "CSS"
        _store.add_topic(name)

        self.assertEqual(2, _store.total())

        _store.add_skill("CSS", "Flex box")
        
        _store.print()
        _store.set_complete("CSS", 0)
        _store.print()

    def test_add_skill(self):
         slug = "java-programming"
         name = "Hibernate"

if __name__ == '__main__':
    unittest.main()