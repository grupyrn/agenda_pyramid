import unittest
import transaction

from pyramid import testing

from .models import *

"""
class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_home(self):
        from agenda.views import home
        resp = home(self.request)
        self.assertEqual(resp.status_int, 200)


        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = Agenda(name='one')
            DBSession.add(model)
"""
