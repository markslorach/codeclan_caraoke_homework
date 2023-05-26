import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guests = [
            Guest("Mark Slorach"),
            Guest("Ellen Shand")
        ]

    def test_guest_has_name(self):
        guest = self.guests[1]
        self.assertEqual("Ellen Shand", guest.guest_name)

    
