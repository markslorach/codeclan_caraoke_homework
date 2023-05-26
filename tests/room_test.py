import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("1")
        self.guest = Guest("Ellen Shand")
        self.song = Song("Tina Turner", "Proud Mary")


    def test_check_room_number(self):
        self.assertEqual("1", self.room.room_number)
    
    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual([self.guest], self.room.guests)

    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest)
        self.assertEqual([], self.room.guests)

    def test_add_a_song(self):
        self.room.add_song(self.song)
        self.assertEqual([self.song], self.room.songs)
gi