from django.test import TestCase
from factories import UserFactory, FieldFactory
class FieldTestCase(TestCase):
    """Class test Field """
    def setUp(self):
        self.user = UserFactory()
        self.field = FieldFactory.create(user=self.user)
    def test_field_user(self):
        createuser = self.field.name_user()
        self.assertEqual(createuser, (' el usuario: ' + self.twitter + ' del campo ' + self.field.name))

    #def test_talk(self):
        
