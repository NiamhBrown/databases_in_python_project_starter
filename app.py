
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        artist_repository = ArtistRepository(self._connection)
        album_repository = AlbumRepository(self._connection)
        artists = artist_repository.all()
        albums = album_repository.all()
        
        print("What would you like to do?")
        print("1 - List all albums")
        print("2 - List all artists")
        user_input = input("Enter your choice:")
        if user_input == "2":
            print("Here is the list of artists:")
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        elif user_input == "1":
            print("Here is the list of albums:")
            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year})")
        else:
            print("Invalid input :(")

if __name__ == '__main__':
    app = Application()
    app.run()


