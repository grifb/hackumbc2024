import subprocess as sub
import os
from pathlib import Path
import wave
import contextlib

directory = "/home/user/hackumbc2024/backend/songs/"


class SongQueue:
    def __init__(self, max_size=100):
        self.queue = []

    def add_song(self, song):
        self.queue.append(song)
        # ['human.wav', 'snailtime.wav', 'ihatemyself.wav']
        print(self.queue)

    def play_song(self):
        if not self.is_empty():
            currentSong = self.queue.pop(0)
            sub.run([
                "mpv",
                "--audio-device=alsa/bluealsa",
                f"{directory}{currentSong}"
            ])
            return currentSong
        else:
            return "Empty"

    def is_empty(self):
        return len(self.queue) == 0

    def is_in(self, checked):
        if checked in self.queue:
            return True
        else:
            return False

    def get_queue(self):
        return self.queue[0]


def get_song_duration(file):
    with contextlib.closing(wave.open(file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def main():
    os.system("bluetoothctl connect 68:59:32:72:4D:25")

    queue = SongQueue()

    # constantly checking for new files to add to queue
    while True:
        for filename in os.scandir(directory):
            if queue.is_in(filename.name):
                continue
            elif Path(filename).suffix != '.wav':
                queue.add_song(filename.name)

        if queue.is_empty():
            continue
        else:
            # ONLY RUN THIS PART RIGHT BEFORE PLAYING A NEW SONG
            currentSong = queue.play_song()
            # pops current file
            files = os.listdir(directory)
            for file in files:
                print(f"File: {file}")
                print(f"Current Song: {currentSong}")
                if (Path(file).name == Path(currentSong).name):
                    os.remove(os.path.join(directory, currentSong))
            currentSong = ''


if __name__ == '__main__':
    main()
