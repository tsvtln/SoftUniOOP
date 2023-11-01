from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = [song for song in self.songs if song.name == song_name]
        if not song:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        song = song[0]
        self.songs.remove(song)
        return f"Removed song {song.name} from the album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        details_info = '\n'.join(f"== {song.get_info()}" for song in self.songs)
        return f"""Album {self.name}\n{details_info}\n"""


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
