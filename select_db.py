from lib.db_class import music_shop
# инициализирую подключениe к БД в другом файле через класс
connection = music_shop.connection()


# Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
# Внимание! Результаты запросов не должны быть пустыми (при необходимости добавьте данные в таблицы).

# количество исполнителей в каждом жанре;
quantity_autors_genre_query = connection.execute("""
    SELECT DISTINCT genre.title, COUNT(autgen.author_id), autgen.genre_id, genre.id
    FROM genreandauthors autgen
    LEFT JOIN genre ON autgen.genre_id = genre.id
    GROUP BY autgen.genre_id, genre.id
    ORDER BY autgen.genre_id;
""").fetchall()

print(quantity_autors_genre_query)


# количество треков, вошедших в альбомы 2019-2020 годов;
quantity_tracks_in_years = connection.execute("""
    SELECT DISTINCT COUNT(tracks.id), albums.album_year, albums.id, tracks.album_id 
    FROM albums
    LEFT JOIN tracks ON tracks.album_id = albums.id
    WHERE albums.id = tracks.album_id AND albums.album_year BETWEEN '2019' AND '2020'
    GROUP BY albums.id, tracks.album_id;
""").fetchall()

print(quantity_tracks_in_years)

# средняя продолжительность треков по каждому альбому;
middle_track_length = connection.execute("""
    SELECT AVG(CAST(tracks.track_length AS FLOAT)), tracks.album_id, albums.id
    FROM tracks
    LEFT JOIN albums ON albums.id = tracks.album_id
    GROUP BY albums.id, tracks.album_id;
""").fetchall()

print(middle_track_length)


# все исполнители, которые не выпустили альбомы в 2020 году;
authors_not_year = connection.execute("""
    SELECT DISTINCT authors.author_name, albums.album_year, autalbum.author_id, autalbum.album_id
    FROM authors, albums, autorsandalbums autalbum
    WHERE albums.album_year != '2020' AND autalbum.author_id = authors.id AND autalbum.album_id = albums.id
    GROUP BY authors.author_name, albums.album_year, autalbum.author_id, autalbum.album_id
""").fetchall()

print(authors_not_year)


# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
author_in_collections = connection.execute("""
    SELECT DISTINCT tracks.title, authors.author_name
    FROM collections, collectandtracks colltracks, tracks, authors, autorsandalbums autralbum, albums
    WHERE authors.author_name = '2pac' AND autralbum.album_id = tracks.album_id AND colltracks.track_id = tracks.id; 
""").fetchall()

# !!!!(пожалуйста подскажите почему не работает(хотя бы намекните в какую сторону воевать),я в творческом тупике, два дня ковыряю. Совершенно не понимаю почему приходит пустой результат, дальше не стал делать потому что просто не успел)!!!
print(author_in_collections)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
# наименование треков, которые не входят в сборники;
# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
# название альбомов, содержащих наименьшее количество треков.


