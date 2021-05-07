CREATE VIEW ContentPerception AS 
  SELECT Content_.contentId, title, consumedAt, evaluatedAt, avg(rate), count(Comment_) FROM Content_
  INNER JOIN Consumption
  ON Content_.contentId = Consumption.contentId
  JOIN Evaluation
  ON Content_.contentId = Evaluation.contentId
  JOIN Comment_
  ON Comment_.contentId = Content_.contentId
  GROUP BY Content_.contentId, consumedAt, evaluatedAt, title;