SELECT title, commentCount FROM ContentPerception
  WHERE avgRate = (
    SELECT MAX(commentCount) FROM ContentPerception
  )
  LIMIT 1;