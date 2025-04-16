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
    

if __name__ == '__main__':
    manager = MovieManager('Film.json')

    # print("Filmek James Cameron-tól:")
    # for movie in manager.search_by_director("James Cameron"):
    #     print(" -", movie)

    # print("Filmek 2007-ből.")
    # for movie in manager.search_by_year(2007):
    #     print(" -", movie)


    for movie in manager.search_by_title("Game"):
        print(" -", movie)