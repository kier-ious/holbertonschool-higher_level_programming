-- Script that lists all shows, and all genres linked to that show, from the db
SELECT tv_show_title AS show_title IFNULL(tv_genres.name, 'NULL') AS genre_name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY show_title ASC, genre_name ASC;
