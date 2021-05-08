from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render


def index(request):
  return render(request, 'base.html', {})

def inactive_users(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT studentId, name_ FROM Student s
                      WHERE NOT EXISTS (SELECT 1 FROM Consumption c WHERE c.studentId = s.studentId);''')
  rows = cursor.fetchall()
  return HttpResponse(rows)

def top_commented_contents(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title, commentCount FROM ContentPerception
                      WHERE commentCount = (
                        SELECT MAX(commentCount) FROM ContentPerception
                      )
                      LIMIT 1;''')
  rows = cursor.fetchone()
  return HttpResponse(rows)


def top_rated_content(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title, avgRate FROM ContentPerception
                      WHERE avgRate = (
                        SELECT MAX(avgRate) FROM ContentPerception
                      )
                      LIMIT 1;''')
  rows = cursor.fetchall()
  return HttpResponse(rows)