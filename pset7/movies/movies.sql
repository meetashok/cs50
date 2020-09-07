-- q1
SELECT title FROM movies WHERE year = 2008;

-- q2
SELECT birth FROM people WHERE name = "Emma Stone";

-- q3
SELECT title FROM movies 
WHERE year >= 2018 
ORDER BY title;

-- q4
SELECT count(1) AS rating_10 FROM ratings
WHERE rating = 10;

-- q5
SELECT title, year FROM movies
WHERE title LIKE "Harry Potter%"
ORDER BY year;

-- q6
SELECT avg(rating) AS rating_avg_2012 FROM ratings
WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);

-- q7
SELECT title, rating FROM movies
JOIN ratings
ON movies.id = ratings.movie_id
WHERE year = 2010 AND
rating IS NOT NULL
ORDER BY rating DESC, title;

-- q8
SELECT name FROM people 
WHERE id IN (SELECT person_id FROM stars 
	WHERE movie_id IN (SELECT id FROM movies 
		WHERE title = "Toy Story"))
		
-- q9
SELECT name FROM people
WHERE id IN 
	(SELECT person_id FROM stars WHERE movie_id IN 
		(SELECT id FROM movies WHERE year = 2004))
ORDER BY birth;

-- q10
SELECT DISTINCT name from people
WHERE id in 
	(SELECT person_id FROM directors where movie_id IN
		(SELECT movie_id FROM ratings where rating >= 9.0));
		
-- q11
SELECT title FROM movies
JOIN ratings
ON movies.id = ratings.movie_id
JOIN stars
ON movies.id = stars.movie_id
JOIN people
ON people.id = stars.person_id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC
LIMIT 5;

-- q12

SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM
(SELECT movie_id FROM stars where person_id IN
(SELECT id FROM people WHERE name IN ("Helena Bonham Carter"))

UNION ALL

SELECT movie_id FROM stars where person_id IN
(SELECT id FROM people WHERE name IN ("Johnny Depp"))) a
GROUP BY movie_id
HAVING count(1) = 2);

-- q13
SELECT name FROM people WHERE id IN 
	(SELECT person_id FROM stars WHERE movie_id in 
		(SELECT movie_id FROM stars WHERE person_id in 
			(SELECT id FROM people WHERE name = "Kevin Bacon" AND birth = 1958)))
AND name <> "Kevin Bacon";