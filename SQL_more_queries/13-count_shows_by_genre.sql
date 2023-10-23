-- Script that lists all genres from database and shows # of shows linked to it
SELECT tv_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING COUNT(tv_shows_genres.show_id) > 0
ORDER BY number_of_shows DESC;
