SELECT
  COUNT(title)
FROM
  movies
WHERE
  id IN (
    SELECT
      movie_id
    FROM
      ratings
    WHERE
      rating = "10.0"
  )