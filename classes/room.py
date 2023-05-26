class Room:
    def __init__ (self, room_number):
        self.room_number = room_number
        self.guests = []
        self.songs = []

    def check_in_guest(self, add_guest):
        self.guests.append(add_guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song(self, add_song):
        self.songs.append(add_song)