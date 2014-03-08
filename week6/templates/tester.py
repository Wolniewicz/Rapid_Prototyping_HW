import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///mymusic.db', echo=True)

from table_def import Album, Artist
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Loreena Mckinnet")
new_artist.albums = [Album("Mystic Dream", 
                           "folk",
                           "star", "CD")]
 
# add more albums
more_albums = [Album("Singer",
                     "folk",
                     "Star", "CD"),
               Album("Dancer", 
                     "celtic",
                     "Sparrow", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("Daft Punk"),
    Artist("Tom Yeh")
    ])
session.commit()