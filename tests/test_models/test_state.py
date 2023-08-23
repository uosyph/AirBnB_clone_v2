#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_table(self):
        """ """
        new = self.value()
        self.assertEqual("states", new.__tablename__)

    def test_name(self):
        """ Checks for the table name """
        new = self.value()
        new.name = "California"
        self.assertEqual("California", new.name)
