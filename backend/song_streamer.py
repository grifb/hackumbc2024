import subprocess as sub
import os
from pathlib import Path
import wave
import contextlib
import time

directory = "/home/asher/hackumbc2024/backend/songs/"
startup = "/home/asher/hackumbc2024/backend/startup/"

MPV_COMMAND = []




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
            sub.run(MPV_COMMAND + [f"{directory}{currentSong}"])
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


def set_mpv_command():
    global MPV_COMMAND
    if sub.check_output(["sudo bluetoothctl info 68:59:32:72:4D:25 | grep Connected"], shell=True, text=True).find("yes") == -1:
        print("Using audio jack...")
        MPV_COMMAND = [
                "mpv",
                ]
    else:
        print("Using bluetooth")
        MPV_COMMAND = [
                "mpv",
                "--audio-device=alsa/bluealsa",
                ]


def get_song_duration(file):
    with contextlib.closing(wave.open(file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def main():
    os.system("bluetoothctl connect 68:59:32:72:4D:25")

    set_mpv_command()

    sub.run(MPV_COMMAND + [f"{startup}startup.wav"])

    time.sleep(2)

    for filename in os.scandir("/home/asher/hackumbc2024/backend/songs"):
        os.remove(filename)

    queue = SongQueue()

    # constantly checking for new files to add to queue
    while True:
        for filename in os.scandir(directory):
            if queue.is_in(filename.name):
                print("Waiting for song...")
                continue
            #If file type is a wav then add the song
            elif Path(filename).suffix == '.wav':
                queue.add_song(filename.name)

        if queue.is_empty():
            continue
        else:
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
