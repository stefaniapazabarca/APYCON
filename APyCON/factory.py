import factory
from django.contrib.auth.models import User
from front.models import Field
from django.models import Speaker

class UserFactory(factory.Factory):
    class Meta:
        model = Speaker
        twiter = factory.Sequence(lambda n: '@person{0}'.format(n))
        biografia = factory.Sequence(lambda n: 'bigrafic person{0}'.format(n))
        idnum= factory.Faker(@person{0})
class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field
        user = factory.SubFactory(UserFactory)
        name = factory.Sequence(lambda n: 'A_Field_Name_%d' % n)

#class Talkfactory(factory.Factory):
#	title= factory.Sequence(lambda n: 'cualquier cosa')
