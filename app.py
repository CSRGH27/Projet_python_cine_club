from PySide2 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.fill_list_movies()
        self.setup_connection()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.add_movie_btn = QtWidgets.QPushButton("Ajouter Film")
        self.list_movie = QtWidgets.QListWidget()
        self.list_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.delete_movie_btn = QtWidgets.QPushButton("Supprimer Film(s)")

        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.add_movie_btn)
        self.layout.addWidget(self.list_movie)
        self.layout.addWidget(self.delete_movie_btn)
    
    def fill_list_movies(self): #On recupere les mobis dans le json avec get_movies() quon importe, on les stocke dans movies puis on ajoutesles 
        #difeerents film avec addItem dans le composant list_movie
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title) #On cree un ListWidget item avec les titres des films
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)

    def setup_connection(self):
        self.add_movie_btn.clicked.connect(self.add_movie)
        self.delete_movie_btn.clicked.connect(self.rm_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        
        new_movie = Movie(movie_title)
        resultat = new_movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(new_movie.title)  #On cree un ListWidget item avec le titre de film qu'on ajoute
            lw_item.setData(QtCore.Qt.UserRole, new_movie) #on lie l'instance new_movie a notre listWidget, grace setData ,on peu recuperer l'instance dasn remove_movie() 
            #grace a data(QtCore.Qt.UserRole)
            self.list_movie.addItem(lw_item)
        
        self.le_movieTitle.setText("") #On vide le input
    
    def rm_movie(self):
        for selected_item in self.list_movie.selectedItems(): #pour chaque item selectionne dans liste qu'on a selectionne (On recupere la liste avec la methode selectedItems())
            movie = selected_item.data(QtCore.Qt.UserRole) #Avec cette ligne on recuere nos instance , on peut donc ensuite utiliser les methode de la classe Movie
            movie.remove_from_movies() #suppprime du json
            self.list_movie.takeItem(self.list_movie.row(selected_item)) #on supprime du listwidget

        # ON evite de reccrer des insatnce car cela ralentit l'app   

    





app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()