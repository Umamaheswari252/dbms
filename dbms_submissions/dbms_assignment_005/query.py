Q1="SELECT pid as actor_id,COUNT(mid) as no_of_movies FROM Cast GROUP BY pid;"
Q2="SELECT year,COUNT(id) FROM Movie GROUP BY year;"
Q3="SELECT year,AVG(rank) as avg_rank FROM Movie GROUP BY year HAVING COUNT(id)>=10 ORDER BY year DESC;"
Q4="SELECT year,MAX(rank) as max_rank FROM Movie GROUP BY year;"
Q5="SELECT rank,COUNT(id) as no_of_movies FROM Movie WHERE name LIKE 'a%' GROUP BY rank;"
