import json

class Movie:
    def __init__(self, data):
        self.title = data.get("Title", "")
        self.year = data.get("Year", "")
        self.director = data.get("Director", "")
        self.language = data.get("Language", "")
        self.genre = data.get("Genre", "")
        self.rating = data.get("imdbRating", "")

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.director} [{self.language}] - {self.rating} pont az IMDB-n"

class MovieManager:
    def __init__(self, json_file):
        with open(json_file, "r", encoding="utf-8") as f:
            self.movies_data = json.load(f)
        self.movies = [Movie(data) for data in self.movies_data]

    def search_by_title(self, keyword):
        return [m for m in self.movies if keyword.lower() in m.title.lower()]
    
    def search_by_director(self, director_name):
        return [m for m in self.movies if director_name.lower() in m.director.lower()]
    
    def search_by_year(self, year):
        return [m for m in self.movies if m.year == str(year)]
    
    def search_by_language(self, language):
        return [m for m in self.movies if language.lower() in m.language.lower()]
    



class Song:
    def __init__(self, data):
        self.title = data.get("title")
        self.length = data.get("length")

    def __str__(self):
        return f"{self.title} ({self.length})"

class Album:
    def __init__(self, data):
        self.title = data.get("title")
        self.description = data.get("description")
        self.songs = [Song(song) for song in data.get("song", [])]
    
    def __str__(self):
        return f"Album: {self.title} ({len(self.songs)} szám)"
    
class Artist:
    def __init__(self, data):
        self.name = data.get("name")
        self.albums = [Album(album) for album in data.get("albums", [])]

    def __str__(self):
        return f"{self.name} ({len(self.albums)} album)"
    
class MusicLibrary:
    def __init__(self, json_file):
        with open(json_file, "r", encoding="utf-8") as f:
            self.raw_data = json.load(f)
        self.artists = [Artist(artist) for artist in self.raw_data]

    def list_all_artists(self):
        for artist in self.artists:
            print(artist)

    def search_song(self, keyword):
        result = []
        for artist in self.artists:
            for album in artist.albums:
                for song in album.songs:
                    if keyword.lower() in song.title.lower():
                        result.append(artist.name, album.title, song)
        return result
    
    def get_album_songs(self, artist_name, album_title):
        for artist in self.artists:
            if artist.name.lower() == artist_name.lower():
                for album in artist.albums:
                    if album.title.lower() == album_title.lower():
                        return album.songs

        return []
    

if __name__ == '__main__':
    # manager = MovieManager('Film.json')

    # print("Filmek James Cameron-tól:")
    # for movie in manager.search_by_director("James Cameron"):
    #     print(" -", movie)

    # print("Filmek 2007-ből.")
    # for movie in manager.search_by_year(2007):
    #     print(" -", movie)

    # for movie in manager.search_by_title("Game"):
    #     print(" -", movie)

    lib = MusicLibrary("music.json")

    print("Előadók:")
    lib.list_all_artists()

    print("Dalcímek keresése 'Ghost' kulcsszóra:")
    results = lib.search_song("Ghost")
    for artist, album, song in results:
        print(f"{artist} - {album} - {song}")