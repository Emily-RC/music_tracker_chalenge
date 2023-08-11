from lib.album import *

""" 
Constructs with id, title, release_year and artist_id  
"""

def test_constructs_wth_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2

    """
When I construct two Albums with th same fields 
They are equal 
"""
def test_albums_are_equal():
    album1 = Album(1, "Dark Side", 1995, 2)
    album2 = Album(1, "Dark Side", 1995, 2)
    assert album1 == album2

"""
# We can format artists to strings nicely
# """
def test_albums_format_nicely():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"
    
# def test_get_all_albums():
#     album = Album(1, "")
    

#     TEST EQ and REPR HERE 


#     albums[0].id # =>  1
#     albums[0].title # =>  'Doolittle'
#     albums[0].release_year# =>  '1989'
#     albums[1].artists_id# => '1'

#     albums[1].id # =>  2
#     albums[1].title # =>  'Surfer Rosa'
#     albums[1].release_year# =>  '1988'
#     albums[1].artists_id# => '1'