from lib.album import * # <-- don't forget to import from album 

class AlbumRepository: 
    
    def __init__(self, connection):
        self._connection = connection
        # take the connection in the inistaliser and set that
        # to an instance variable so we can store it 

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        # here we are running some SQL code 
        # then below we aggregate these: 
        # albums = []
        return [
            Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            for row in rows 
        ]
            # albums.append(album) # append to a list 
        # return albums 

    def find(self, id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [id])
        # we use a placeholder which is called tooling (%s)
        # because this is being passed through the psycopg library
        # it's saying this is the table and this is the data and we 
        # won't get confused. So now, if the user was to put in "delet all tables" where 
        # the [id] is,  then psycopg would say no that's not an id it doesn't count 
        row = rows[0] 
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", 
            [album.title, album.release_year, album.artist_id]
        )
        return None

