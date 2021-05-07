SELECT Student.studentId, Student.name_, SUM(price) AS spentValue FROM Student
  JOIN Order_ ON Student.studentId = Order_.studentId
  JOIN Product ON Product.productId = Order_.productId
  GROUP BY Student.studentId, Student.name_
  ORDER BY spentValue DESC;