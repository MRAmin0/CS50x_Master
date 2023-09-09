SELECT
  title,
  YEAR
FROM
  movies
WHERE
  title LIKE "harry Potter%"
ORDER BY
  YEAR