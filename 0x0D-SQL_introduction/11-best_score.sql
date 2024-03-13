-- Lists all records in table second_table with score >= 10 in MySQL server.
-- Records are ordered by descending score.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
