CREATE VIEW ContentPerception AS 
  SELECT Content_.contentId, title, consumedAt, evaluatedAt, avg(rate) as avgRate, count(Comment_) as commentCount FROM Content_
  INNER JOIN Consumption
  ON Content_.contentId = Consumption.contentId
  JOIN Evaluation
  ON Content_.contentId = Evaluation.contentId
  JOIN Comment_
  ON Comment_.contentId = Content_.contentId
  GROUP BY Content_.contentId, consumedAt, evaluatedAt, title;

CREATE VIEW Accesses AS  --atividade dos alunos
  SELECT name_, consumedAt AS data, 'consumo' AS atividade
  FROM Student NATURAL JOIN Consumption
  UNION
  SELECT name_, commentedAt AS data, 'comentario' AS atividade
  FROM Student NATURAL JOIN Comment_
  UNION
  SELECT name_, evaluatedAt AS data, 'avaliacao' AS atividade
  FROM Student NATURAL JOIN Evaluation
  UNION
  SELECT name_, submitedAt AS data, 'redacao' AS atividade
  FROM Student NATURAL JOIN Essay
  ORDER BY name_, data;