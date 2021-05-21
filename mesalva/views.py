from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render


def index(request):
  return render(request, 'base.html', {})

def inactive_users(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT studentId, name_ FROM Student s
                      WHERE NOT EXISTS (SELECT 1 FROM Consumption c WHERE c.studentId = s.studentId);''')

  msg="<title>Usuários inativos</title><center><h1>Usuários inativos</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>studentId</th><th>name_ student</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+str(row[0])+"</td>"
    msg+="<td>"+row[1]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def top_commented_contents(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title, commentCount FROM ContentPerception
                      WHERE commentCount = (
                        SELECT MAX(commentCount) FROM ContentPerception
                      )
                      LIMIT 10;''')

  msg="<title>TOP 10 conteúdos mais comentados</title><center><h1>TOP 10 conteúdos mais comentados</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Título</th><th>Número de comentários</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)


def top_rated_content(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title, avgRate FROM ContentPerception
                      WHERE avgRate = (
                        SELECT MAX(avgRate) FROM ContentPerception
                      )
                      LIMIT 10;''')

  msg="<title>TOP 10 conteúdos melhor avaliados</title><center><h1>TOP 10 conteúdos melhor avaliados</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Título</th><th>Média de avaliação</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+"{0:.2f}".format(row[1])+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)