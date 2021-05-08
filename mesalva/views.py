from django.http import HttpResponse
from django.db import connection


def index(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT studentId, name_ FROM Student s
                      WHERE NOT EXISTS (SELECT 1 FROM Consumption c WHERE c.studentId = s.studentId);''')
  rows = cursor.fetchall()
  return HttpResponse(rows)