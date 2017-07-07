import unittest, db

class Test(unittest.TestCase):

    def test_add_topic(self):
        _db = db.Db()

        slug = "java-programming"
        name = "Java programming"
        _db.add_topic(slug, name)

        self.assertEqual(1, _db.total())

        slug = "css-flexbox"
        name = "CSS flexbox"
        _db.add_topic(slug, name)

        self.assertEqual(3, _db.total())
    
    def test_add_skill(self):
         slug = "java-programming"
         name = "Hibernate"

if __name__ == '__main__':
    unittest.main()