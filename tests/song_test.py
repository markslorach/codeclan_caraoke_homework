import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
        
        self.songs = [
            Song("Placebo", "The Bitter End"),
            Song("Bonobo", "Defender"),
            Song("Caribou", "Our Love")
        ]

    def test_song_has_artist(self):
        self.assertEqual("Caribou", self.songs[2].artist)

    def test_song_has_title(self):
        self.assertEqual("Our Love", self.songs[2].title)

    


     