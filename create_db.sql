create table if not exists Genre (
	id serial primary key,
	title varchar(100) not null
);

create table if not exists Authors (
	id serial primary key,
	author_name varchar(100) not null
);

create table if not exists GenreAndAuthors (
	id serial primary key,
	genre_id integer references Genre(id),
	author_id integer references Authors(id)
);

create table if not exists Albums (
	id serial primary key,
	title varchar(100) not null,
	album_year varchar(20) not null
);

create table if not exists AutorsAndAlbums (
	id serial primary key,
	author_id integer references Authors(id),
	album_id integer references Albums(id)
);

create table if not exists Collections (
	id serial primary key,
	title varchar(100) not null,
	collection_year varchar(20) not null
);

create table if not exists Tracks (
	id serial primary key,
	title varchar(100) not null,
	album_id integer references Albums(id),
	track_length varchar(30) not null
);

create table if not exists CollectAndTracks (
	id serial primary key,
	collection_id integer references Collections(id),
	track_id integer references Tracks(id)
);