import os
import json
import logging


CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")
print(DATA_FILE)


def get_movies():
    with open(DATA_FILE, "r") as target:
        movies_title = json.load(target)
    # VOir comprehension de liste : on cree une liste (movies)  en creeeant des instances de Movie avec les titre qui sont presnt dans notre json
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return f"{self.title}"

    def _get_movies(self):
        with open(DATA_FILE, "r") as target:
            return json.load(target)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as target:
            json.dump(movies, target, indent=4)

    def add_to_movies(self):
        # On va chercher les film dan le json avec la metjode _get_movies on l'assigne dasn la var liste_movies
        liste_movies = self._get_movies()

        if self.title in liste_movies:
            logging.warning(f"Le film {self.title} existe deja !!")
            return False
        else:
            liste_movies.append(self.title)
            # ON ajoute/supprime notre film avec _write_movies avec notre var liste movies en param
            self._write_movies(liste_movies)
            return True

    def remove_from_movies(self):
        # On va chercher les film dan le json avec la metjode _get_movies on l'assigne dasn la var liste_movies
        liste_movies = self._get_movies()

        if self.title in liste_movies:
            liste_movies.remove(self.title)
            # ON ajoute/supprime notre film avec _write_movies avec notre var liste movies en param
            self._write_movies(liste_movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas dans la liste")
            return False
    
    
        


# On exexute ce code que si c'est le fichier principal, si il est importe dans un autre fichier on ne l'importe pas
if __name__ == "__main__":
    movies = get_movies()
    print(movies)
