-- Script that lists all tv shows in database that are in the same genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id IN (
  SELECT DISTINCT show_id
  FROM tv_show_genres
)
ORDER BY tv_show.title, tv_show_genres.genre_id ASC;
