from lib.album import Album 

"""
test to check album constructs with 
id, title, release_year, artist_id
"""

def test_constructs_with_correct_feilds():
    album = Album(1,"OK Computer", 1978,2)
    assert album.id == 1
    assert album.title == "OK Computer"
    assert album.release_year == 1978
    assert album.artist_id == 2

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1,"OK Computer", 1978,2)
    assert str(album) == "Album(1, OK Computer, 1978, 2)"
    # Try commenting out the `__repr__` method in lib/album.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1,"OK Computer", 1978,2)
    album2 = Album(1,"OK Computer", 1978,2)
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.
