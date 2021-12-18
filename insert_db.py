from lib.db_class import music_shop
# инициализирую подключениe к БД в другом файле через класс
connection = music_shop.connection()

authors_arr = [
    {'author_name': 'Behemoth'},
    {'author_name': 'Metallica'},
    {'author_name': 'Robert Leroy Jonson'},
    {'author_name': 'Eric Klepton'},
    {'author_name': 'Bono'},
    {'author_name': 'Mick Jagger'},
    {'author_name': '2pak'},
    {'author_name': 'Eminem'},
    {'author_name': 'Shakira'},
    {'author_name': 'Weeknd'}
]

genre_arr = [
    {'title': 'Metall'},
    {'title': 'Blues'},
    {'title': 'Rock'},
    {'title': 'Rap'},
    {'title': 'Pop'}
]

albums_arr = [
    {'title': 'Demigod', 'author_name': 'Behemoth', 'year': '2004'},
    {'title': 'Death Magnetic', 'author_name': 'Metallica', 'year': '2008'},
    {'title': 'His Recorded Legacy', 'author_name': 'Robert Leroy Jonson', 'year': '2011'},
    {'title': 'Unplugged', 'author_name': 'Eric Klepton', 'year': '1992'},
    {'title': 'War', 'author_name': 'Bono', 'year': '1983'},
    {'title': 'Goddess in the Doorway', 'author_name': 'Mick Jagger', 'year': '2001'},
    {'title': 'R U Still Down?', 'author_name': '2pak', 'year': '1997'},
    {'title': 'Revival', 'author_name': 'Eminem', 'year': '2018'},
    {'title': 'El Dorado', 'author_name': 'Shakira', 'year': '2017'},
    {'title': 'After Hours', 'author_name': 'Weeknd', 'year': '2020'}
]

tracks_arr = [
    {'title': 'Behemoth sculpting the throne ov seth', 'album': 'Demigod', 'length': '4.42', 'album_id': 1},
    {'title': 'Demigod', 'album': 'Demigod', 'length': '3.34', 'album_id': 1},
    {'title': 'That Was Just Your Life', 'album': 'Death Magnetic', 'length': '7.08', 'album_id': 2},
    {'title': 'The End Of The Line', 'album': 'Death Magnetic', 'length': '7.52', 'album_id': 2},
    {'title': 'Walking Blues', 'album': 'His Recorded Legacy', 'length': '2.32', 'album_id': 3},
    {'title': 'Rambling on My Mind', 'album': 'His Recorded Legacy', 'length': '2.53', 'album_id': 3},
    {'title': 'Signe', 'album': 'Unplugged', 'length': '3.13', 'album_id': 4},
    {'title': 'Before You Accuse Me', 'album': 'Unplugged', 'length': '3.44', 'album_id': 4},
    {'title': 'Sunday Bloody Sunday', 'album': 'War', 'length': '4.40', 'album_id': 5},
    {'title': 'Seconds', 'album': 'War', 'length': '3.11', 'album_id': 5},
    {'title': 'Visions Of Paradise', 'album': 'Goddess in the Doorway', 'length': '4.01', 'album_id': 6},
    {'title': 'Joy', 'album': 'Goddess in the Doorway', 'length': '4.41', 'album_id': 6},
    {'title': 'Redemption', 'album': 'R U Still Down?', 'length': '1.48', 'album_id': 7},
    {'title': 'Open Fire', 'album': 'R U Still Down?', 'length': '2.53', 'album_id': 7},
    {'title': 'Walk on Water', 'album': 'Revival', 'length': '5.04', 'album_id': 8},
    {'title': 'Believe', 'album': 'Revival', 'length': '5.15', 'album_id': 8},
    {'title': 'Me Enamore', 'album': 'El Dorado', 'length': '3.47', 'album_id': 9},
    {'title': 'Nada', 'album': 'El Dorado', 'length': '3.10', 'album_id': 9},
    {'title': 'Alone Again', 'album': 'After Hours', 'length': '4.10', 'album_id': 10},
    {'title': 'Hardest to Love', 'album': 'After Hours', 'length': '3.31', 'album_id': 10}
]

collections_arr = [
    {'title': 'Collections №1', 'year': '2004'},
    {'title': 'Collections №2', 'year': '2008'},
    {'title': 'Collections №3', 'year': '2010'},
    {'title': 'Collections №4', 'year': '2017'},
    {'title': 'Collections №5', 'year': '2008'},
    {'title': 'Collections №6', 'year': '2018'},
    {'title': 'Collections №7', 'year': '2019'},
    {'title': 'Collections №8', 'year': '2020'},
    {'title': 'Collections №9', 'year': '2020'},
    {'title': 'Collections №10', 'year': '2021'}
]


# added authors
for author in authors_arr:
    connection.execute(f"""
        INSERT INTO authors(author_name) 
        VALUES('{author['author_name']}');
    """)

# added genre
for genre in genre_arr:
    connection.execute(f"""
        INSERT INTO genre(title) 
        VALUES('{genre['title']}');
    """)


# added genre and authors
connection.execute("""
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(1, 1);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(1, 2);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(2, 3);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(2, 4);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(3, 5);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(3, 6);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(4, 7);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(4, 8);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(5, 9);
    INSERT INTO genreandauthors(genre_id, author_id) VALUES(5, 10);
""")


# added albums
for album in albums_arr:
    connection.execute(f"""
        INSERT INTO albums(title, album_year) 
        VALUES('{album['title']}', '{album['year']}');
    """)


# added autors and albums
connection.execute("""
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(1, 1);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(2, 2);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(3, 3);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(4, 4);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(5, 5);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(6, 6);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(7, 7);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(8, 8);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(9, 9);
    INSERT INTO autorsandalbums(author_id, album_id) VALUES(10, 10);
""")


# added tracks
for track in tracks_arr:
    connection.execute(f"""
        INSERT INTO tracks(title, album_id, track_length) 
        VALUES('{track['title']}', {track['album_id']}, '{track['length']}');
    """)


# added collcetions
for collection in collections_arr:
    connection.execute(f"""
        INSERT INTO collections(title, collection_year) 
        VALUES('{collection['title']}', '{collection['year']}');
    """)


# added collect and tracks
connection.execute("""
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(1, 20);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(1, 19);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(2, 18);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(2, 17);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(3, 16);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(3, 15);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(4, 14);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(4, 13);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(5, 12);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(5, 11);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(6, 10);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(6, 9);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(7, 8);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(7, 7);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(8, 6);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(8, 5);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(9, 4);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(9, 3);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(10, 2);
    INSERT INTO collectandtracks(collection_id, track_id) VALUES(10, 1);
""")