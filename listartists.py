

class Artist(object):
    def __init__(self, name):
        self.name = name
        self.albums = []
        
    def addAlbum(self, album):
        self.albums.append(album)
    
        
    
class Album(object):
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        
    def __str__(self):
        return "Title: %s Year: %i Genre: %s" % (self.title,self.year,self.genre)
                                                 
        
        
artists = []
mbv = Artist("My Bloody Valentine")
album1 = Album("Loveless", 1991, "Shoegaze")
mbv.addAlbum(album1)

album2 = Album("Isn't Anything", 1992, "Breakbeat")

mbv.addAlbum(album2)

for i in range(0, len(mbv.albums)):
    print(mbv.albums[i])

        