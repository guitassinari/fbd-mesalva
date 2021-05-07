SELECT title, avgRate FROM ContentPerception
  WHERE avgRate = (
    SELECT MAX(avgRate) FROM ContentPerception
  )
  LIMIT 1;