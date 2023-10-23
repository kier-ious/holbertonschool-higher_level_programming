-- Script that lists all the Comedy shows in the db
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
