from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# file: app.py

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()

        print('Welcome to music library manager!\n')
        print('What would you like to do?\n 1 - List all artists\n 2 - List all albums\n')
        choice = input('Enter your choice: ')

        if choice == '1':
            print('\nHere is the list of artists:/n')
            for artist in artists: #output example: * 1 - Doolittle
                print(f' * - {artist.name}')

        elif choice == '2':
            print('\nHere is the albums:\n')
            for album in albums:
                print(f' * - {album.title}')
        
        # elif choice == '3':
        #     artist = input('Which artist? ')
        #     print('\nHere are the albums by that artist:\n')
        #     album_repository.find(int(artist))
        
        else:
            print('Please enter a 1 or a 2')

if __name__ == '__main__':
    app = Application()
    app.run()



# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library2.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)