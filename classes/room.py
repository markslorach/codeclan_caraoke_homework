class Room:
    def __init__ (self, room_number, room_capacity, entry_fee):
        self.room_number = room_number
        self.guests = []
        self.songs = []
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee

    
    # when checking in a guest
    # if the amount of guests (len) is less than or equal to the room capacity (True)
    # if a guests money is equal to or above the entry fee (True)
    # append guest to the guest list
    # take away the entry fee from guests money
    
    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
    


    