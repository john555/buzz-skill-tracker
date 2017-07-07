import unittest, store

class Test(unittest.TestCase):

    def test_add_topic(self):
        _store = store.Store()

        slug = "java-programming"
        name = "Java programming"
        _store.add_topic(slug, name)

        self.assertEqual(1, _store.total())

        slug = "css-flexbox"
        name = "CSS flexbox"
        _store.add_topic(slug, name)

        self.assertEqual(2, _store.total())
        _store.print()

    def test_add_skill(self):
         slug = "java-programming"
         name = "Hibernate"

if __name__ == '__main__':
    unittest.main()