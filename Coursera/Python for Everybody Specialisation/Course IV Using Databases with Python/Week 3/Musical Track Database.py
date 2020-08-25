import sqlite3
from xml.etree import ElementTree as ET

# set up the database
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# pass the sequence of queries
cur.executescript('''

DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

file_name = input("Enter file path: ", )
if len(file_name) < 1:
    file_name = 'tracks/Library.xml'

tree = ET.parse(file_name)
root = tree.getroot()
data = root.findall('./dict/dict/dict')
print('Dict count: ', len(data))


def lookup(parent, key):
    # mark the key when you encounter
    found = False

    for child in parent:

        # if the key's been marked, extract the next text which is the value and return
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True

    return None


# traverse through the dictionaries
for i, parent in enumerate(data):

    if lookup(parent, 'Track ID') is None:
        continue

    artist = lookup(parent, 'Artist')
    genre = lookup(parent, 'Genre')
    album = lookup(parent, 'Album')
    name = lookup(parent, 'Name')
    length = lookup(parent, 'Total Time')
    rating = lookup(parent, 'Rating')
    count = lookup(parent, 'Play Count')

    if name is None or artist is None or album is None or genre is None:
        continue

    print('Inserting into Artist Table: \n')
    print('Name of the Artist: ', artist)
    cur.execute('''
        INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )
    ''', (artist,))
    # extract artist id to be used in further tables
    cur.execute('''
        SELECT id FROM Artist
        WHERE name = ( ? )
    ''', (artist,))
    artist_id = cur.fetchone()[0]

    print('Inserting into Genre Table: \n')
    print('Genre: ', genre)
    cur.execute('''
        INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )
    ''', (genre,))
    # extract genre id to be used in further tables
    cur.execute('''
        SELECT id FROM Genre
        WHERE name = ( ? )
    ''', (genre,))
    genre_id = cur.fetchone()[0]

    print('Inserting into Album Table: \n')
    print('Album: ', album)
    cur.execute('''
        INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )
    ''', (album, artist_id))
    # extract genre id to be used in further tables
    cur.execute('''
        SELECT id FROM Album
        WHERE title = ( ? )
    ''', (album,))
    album_id = cur.fetchone()[0]

    print('Inserting into Track Table: \n')
    print('Track Name: ', name)
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id, genre_id, length, rating, count))
    conn.commit()

conn.close()
