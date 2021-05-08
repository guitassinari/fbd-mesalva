SELECT studentId, name_ FROM Student s
  WHERE NOT EXISTS (SELECT 1 FROM Consumption c WHERE c.studentId = s.studentId);