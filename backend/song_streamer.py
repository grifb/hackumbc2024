import subprocess
import os
from queue import Queue
import time
from pathlib import Path
import playsound

directory = "C:\\Users\\canna\\Downloads\\test\\"

class SongQueue:
    def __init__(self, max_size = 100):
        self.queue = []
        
    
    def add_song(self, song):
        self.queue.append(song)
        print(self.queue)

    def play_song(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Empty"

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_in(self,checked):
        if checked in self.queue:
            return True
        else:
            return False
    def get_queue(self):
        return self.queue[0]
        
    
queue = SongQueue()
files = os.listdir(directory)
#constantly checking for new files to add to queue
while True:
    for filename in os.scandir(directory):
        if queue.is_in(filename):
            continue
        else: 
            queue.add_song(filename.name)
    # ONLY RUN THIS PART RIGHT BEFORE PLAYIGN A NEW SONG 
    #add the if statement from mpv here
    time.sleep(1)
    currentSong = queue.play_song()
    print(currentSong)
    print(f"{directory}{currentSong}")
    playsound.playsound(f"{directory}{currentSong}")
    #pops current file
    for file in files:
        if (Path(file.name) == currentSong):
            os.remove(os.path.join(directory,currentSong))
        #comment
    






