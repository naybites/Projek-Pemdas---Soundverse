class MusicLibrary:
    def __init__(self, songs_file='songs.txt'):
        self.songs_file = songs_file
        self.songs = []

    def load_songs(self):
        try:
            with open(self.songs_file, 'r') as file:
                self.songs = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.songs_file} not found.")
        except Exception as e:
            print(f"An error occurred while loading songs: {e}")

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            with open(self.songs_file, 'a') as file:
                file.write(song + '\n')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            with open(self.songs_file, 'w') as file:
                for s in self.songs:
                    file.write(s + '\n')

    def get_song_list(self):
        return self.songs.copy()