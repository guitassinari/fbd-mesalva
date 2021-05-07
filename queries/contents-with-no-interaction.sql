SELECT title, contentId FROM Content_ c
  WHERE NOT EXISTS (SELECT 1 FROM ContentPerception p WHERE p.contentId = c.contentId);