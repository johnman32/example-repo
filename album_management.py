# Define album Class 
class Album():
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs
    
# Method that prints album name, artist and number of songs
    def __str__(self):
        return (f"Album name: {self.album_name}\n"
                f"Album artist: {self.album_artist}\n"
                f"Number of songs: {self.number_of_songs}\n")

# Returns the amount of songs
def sort_by_song(album):
    return album.number_of_songs



def sort_by_album_name(album):
    return album.album_name




# Assign variables to the album class
echoes_of_tomorrow = Album(album_name = "Echoes of Tomorrow",
                           album_artist = "John",
                           number_of_songs = 5
                           )

blood_of_heroes = Album(album_name = "Blood of heroes",
                           album_artist = "Sally",
                           number_of_songs = 10
                           )

neon_reveriem = Album(album_name = "Neon Reveriem",
                           album_artist = "Chris",
                           number_of_songs = 11
                           )


wave_and_wounds = Album(album_name = "Waves and wounds",
                           album_artist = "Michael",
                           number_of_songs = 7
                           )

gravity_in_blood = Album(album_name = "Gravity in Bloom",
                           album_artist = "Alice",
                           number_of_songs = 9
                           )

thriller = Album(album_name = "Thriller",
                 album_artist = "Michael Jackson",
                 number_of_songs = 9)

back_in_black = Album(album_name = "Back in Black",
                 album_artist = "AC/DC",
                 number_of_songs = 10)

ye = Album(album_name = "Ye",
                 album_artist = "Kanye West",
                 number_of_songs = 7)

animals = Album(album_name = "Animals",
                 album_artist = "Pink Floyd",
                 number_of_songs = 5)

abbey_road = Album(album_name = "Abbey Road",
                 album_artist = "The Beatles",
                 number_of_songs = 17)

dark_side_of_the_moon = Album(album_name = "Dark side of the moon",
                 album_artist = "Pink Floyd",
                 number_of_songs = 9)

oops_i_did_it_again = Album(album_name = "Oops!...I Did It Again",
                 album_artist = "Britney Spears",
                 number_of_songs = 16)


# List containing the albums 
albums1 = [echoes_of_tomorrow, blood_of_heroes, neon_reveriem, wave_and_wounds, gravity_in_blood]

# List containing albums
albums2 = [thriller, back_in_black, animals, ye, abbey_road, oops_i_did_it_again, dark_side_of_the_moon]

# Sorts the albums by number of songs
albums1.sort(key=sort_by_song)

# Prints the sorted list
for album in albums1:
    print(album)
    

# Swap album index 0 and 1 positions
albums1[0], albums1[1] = albums1 [1], albums1[0]

print("---------------------------------------\n")

# Prints list with swapped album index
for album in albums1:
    print(album)

print("-------------------------\n")

# Prints out albums in album2
for album in albums2:
    print(album)

# Add albums1 to the albums2 list 
albums2.extend(albums1)

print("-------------------------\n")

for album in albums2:
    print(album)


print("------Sorted By Album Name--------")

# Sorts albums alphabetically
albums2.sort(key=sort_by_album_name)

for album in albums2:
    print (album)


print("-----Song Search-----")

# Finds the index of song dark side of the moon
for index, album in enumerate(albums2):
    if album.album_name.lower() == "dark side of the moon":
        print(f"Found at index: {index}")
    








