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
        song = self.songs[2]
        self.assertEqual("Caribou", song.artist)

    def test_song_has_title(self):
        song = self.songs[2]
        self.assertEqual("Our Love", song.title)

      
     