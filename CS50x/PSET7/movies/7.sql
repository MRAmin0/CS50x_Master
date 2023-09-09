SELECT
  title,
  raitng
FROM
  movies
  JOIN ratings ON movies.id = rating.movie_id
WHERE
  YEAR = "2010"
ORDER BY
  rating desc,
  title