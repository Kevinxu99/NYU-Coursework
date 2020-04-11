class Empty(Exception):
    pass


class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class PlayList:

    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return self.data.num_of_elems

    def is_empty(self):
        return self.data.num_of_elems == 0

    def add_to_palylist(self, str_title):
        self.data.enqueue(str_title)

    def print_playlist(self):
        pl = ""
        curr_ind = self.data.front_ind
        for i in range(self.data.num_of_elems):
            if(curr_ind == len(self.data.data)):
                curr_ind = 0
            pl = pl + "Track "+str(i+1)+": "+self.data.data[curr_ind]+"\n"
            curr_ind += 1
        return pl

    def play(self, track_no):
        if self.is_empty():
            raise Empty("Queue is empty")
        track_ind = (self.data.front_ind + track_no - 1) % len(self.data.data)
        if(self.data.data[track_ind] == None):
            raise Empty("No song found")
        else:
            return self.data.data[track_ind]

    def move_up(self, track_no):
        if self.is_empty():
            raise Empty("Queue is empty")
        track_ind = (self.data.front_ind + track_no - 1) % len(self.data.data)
        if (self.data.data[track_ind] == None):
            raise Empty("No song found")
        if (track_no == 1):
            raise Empty("The song is already first in the playlist")
        if (track_ind == 0):
            move_ind = len(self.data.data)
        else:
            move_ind = track_ind - 1
        temp_title = self.data.data[move_ind]
        self.data.data[move_ind] = self.data.data[track_ind]
        self.data.data[track_ind] = temp_title

    def move_down(self, track_no):
        if self.is_empty():
            raise Empty("Queue is empty")
        track_ind = (self.data.front_ind + track_no - 1) % len(self.data.data)
        if (self.data.data[track_ind] == None):
            raise Empty("No song found")
        if (track_no == self.data.num_of_elems):
            raise Empty("The song is already last in the playlist")
        move_ind = (track_ind + 1) % len(self.data.data)
        temp_title = self.data.data[move_ind]
        self.data.data[move_ind] = self.data.data[track_ind]
        self.data.data[track_ind] = temp_title

    def remove_song(self, track_no):
        if self.is_empty():
            raise Empty("Queue is empty")
        track_ind = (self.data.front_ind + track_no - 1) % len(self.data.data)
        if (self.data.data[track_ind] == None):
            raise Empty("No song found")
        for i in range(track_no-1,-1,-1):
            curr_ind = (self.data.front_ind + i) % len(self.data.data)
            self.data.data[(curr_ind+1)%len(self.data.data)] = self.data.data[curr_ind]
        self.data.data[self.data.front_ind] = None
        self.data.front_ind = (self.data.front_ind + 1) % len(self.data.data)
        self.data.num_of_elems -= 1



p = PlayList()
p.add_to_palylist("Help")
p.add_to_palylist("h")
print(p.print_playlist())
