#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        new.place_id = "1"
        self.assertIsInstance(new.place_id, str)

    def test_user_id(self):
        """ """
        new = self.value()
        new.user_id = "id"
        self.assertIsInstance(new.user_id, str)

    def test_text(self):
        """ """
        new = self.value()
        new.text = "text"
        self.assertIsInstance(new.text, str)
