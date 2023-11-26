from django.test import TestCase

class views(TestCase):

    @classmethod
    def setUpClass(cls):
        import django
        django.setup()

    def test_something(self,):
        from user.model import something
        ...
