SELECT
  title
FROM movies join ratings on movie.id = ratings.movie_id
where id in (select stars.movie_id from stars where person_id in (select id from  people ) )
