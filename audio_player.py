class AudioPlayer:
    def __init__(self):
        self.current_song = None
        self.is_playing = False
        self.volume = 50  # Volume level from 0 to 100

    def play(self, song):
        self.current_song = song
        self.is_playing = True
        print(f"Playing: {song}")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print("Paused")

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            self.current_song = None
            print("Stopped")

    def set_volume(self, level):
        if 0 <= level <= 100:
            self.volume = level
            print(f"Volume set to: {level}")
        else:
            print("Volume level must be between 0 and 100")