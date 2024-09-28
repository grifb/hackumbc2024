import subprocess
import os
from queue import Queue


class SongQueue:
    def __init__(self, max_size = 100):
        self.queue = []
    
    def add_song(self, song):
        self.queue.append(song)

    def play_song(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return ""

    def is_empty(self):
        return len(self.queue) == 0

