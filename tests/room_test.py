import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room = Room(1, 10, 15)
        self.guest = Guest("Paddington Bear", 50.00)
        self.song = Song("Tina Turner", "Proud Mary")


    def test_check_room_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_check_room_capacity(self):
        self.assertEqual(10, self.room.room_capacity)

    def test_check_entry_fee(self):
        self.assertEqual(15, self.room.entry_fee)
    
    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(True, len(self.room.guests) <= self.room.room_capacity)
        self.assertEqual(True, self.guest.guest_money >= self.room.entry_fee)
        self.assertEqual([self.guest], self.room.guests)
        self.assertEqual(35, self.guest.guest_money - self.room.entry_fee)
    
    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest)
        self.assertEqual([], self.room.guests)

    def test_add_a_song(self):
        self.room.add_song(self.song)
        self.assertEqual([self.song], self.room.songs)

