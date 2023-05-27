import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guests = [Guest("Mark Slorach", 80.00), Guest("Ellen Shand", 80.00)]

    def test_guest_has_name(self):
        self.assertEqual("Ellen Shand", self.guests[1].guest_name)

    def test_guest_has_money(self):
        self.assertEqual(80, self.guests[0].guest_money)
        

    
