from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render


def users_activity(request):
  cursor = connection.cursor()
  cursor.execute('''  SELECT name_, consumedAt AS data, 'consumo' AS atividade
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
  UNION
  SELECT name_, orderedAt AS data, 'compra' AS atividade
  FROM Student NATURAL JOIN Order_
  ORDER BY name_, data;''')

  msg="<title>Atividade dos usuários</title><center><h1>Atividade dos usuários</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th><th>Data</th><th>Atividade</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def evaluation_essay(request):
  cursor = connection.cursor()
  cursor.execute(''' SELECT name_, title, theme, comment_, rate, teachername
  FROM Student NATURAL JOIN Essay NATURAL JOIN EssayEvaluation;''')

  msg="<title>Avaliações de redação</title><center><h1>Avaliações de redação</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th><th>Título</th><th>Tema</th><th>Comentário</th><th>Nota</th><th>Nome professor</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+row[1]+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="<td>"+row[3]+"</td>"
    msg+="<td>"+str(row[4])+"</td>"
    msg+="<td>"+row[5]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def evaluation_essay(request):
  cursor = connection.cursor()
  cursor.execute(''' SELECT name_, title, theme, comment_, rate, teachername
  FROM Student NATURAL JOIN Essay NATURAL JOIN EssayEvaluation;''')

  msg="<title>Avaliações de redação</title><center><h1>Avaliações de redação</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th><th>Título</th><th>Tema</th><th>Comentário</th><th>Nota</th><th>Nome professor</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+row[1]+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="<td>"+row[3]+"</td>"
    msg+="<td>"+str(row[4])+"</td>"
    msg+="<td>"+row[5]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def avg_essay(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT name_, AVG(rate) AS avg_rate
  FROM Student NATURAL JOIN Essay NATURAL JOIN EssayEvaluation
  GROUP BY name_;''')

  msg="<title>Média de redação</title><center><h1>Média de redação</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th><th>Média de redação</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def users_without_evaluation(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT name_
  FROM Student
  WHERE studentId NOT IN (SELECT studentId FROM Essay NATURAL JOIN EssayEvaluation);''')

  msg="<title>Usuários sem redações avaliadas</title><center><h1>Usuários sem redações avaliadas</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def exercises(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT exerciseId, difficulty, Question.name_, Option_.name_
  FROM Exercise JOIN Question USING (exerciseId) JOIN Option_ USING (questionId);''')

  msg="<title>Exercícios disponíveis</title><center><h1>Exercícios disponíveis</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>exerciseId</th><th>Dificuldade</th><th>Questão</th><th>Opções de resposta</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+str(row[0])+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="<td>"+row[3]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)


def not_answered_exercises(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT exerciseId, difficulty, Question.name_ AS questao FROM Exercise JOIN Question USING (exerciseId)
  WHERE questionId NOT IN (
  SELECT questionId
  FROM Student NATURAL JOIN QuestionAnswer JOIN Option_ USING (optionId)
  WHERE Student.name_='Estudante 1');''')

  msg="<title>Exercícios não respondidos pelo Estudante 1</title><center><h1>Exercícios não respondidos pelo Estudante 1</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>exerciseId</th><th>Dificuldade</th><th>Questão</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+str(row[0])+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def exercises_correct_answer(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT difficulty, Question.name_, Option_.name_ AS opcao_correta
  FROM Exercise JOIN Question USING (exerciseId) JOIN Option_ USING (questionId)
  WHERE exerciseId=1 AND correct='true';''')

  msg="<title>Gabarito do exercício 1</title><center><h1>Gabarito do exercício 1</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Dificuldade</th><th>Questão</th><th>Opção correta</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+str(row[0])+"</td>"
    msg+="<td>"+row[1]+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)


def user_hit_rate(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT Student.name_, COUNT(DISTINCT questionId) AS questoes_respondidas, COUNT(*) FILTER (WHERE correct) AS acertos
  FROM Student LEFT JOIN QuestionAnswer USING (studentId) LEFT JOIN Option_ USING (optionId)
  GROUP BY Student.name_
  ORDER BY Student.name_;''')

  msg="<title>Acertos de exercícios por cada usuário</title><center><h1>Acertos de exercícios por cada usuário</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Usuário</th><th>Questões respondidas</th><th>Acertos</th><th>Porcentagem de acertos</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+str(row[2])+"</td>"
    if row[1]==0:
      msg+="<td>---</td>"
    else:
      msg+="<td>"+"{0:.2f}".format(100.0*row[2]/row[1])+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)


def content_activity(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
  FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
  GROUP BY title
  ORDER BY title;''')

  msg="<title>Conteúdo e atividades</title><center><h1>Conteúdo e atividades</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Conteúdo</th><th>Aulas</th><th>Exercícios</th><th>Material extra</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+str(row[2])+"</td>"
    msg+="<td>"+str(row[3])+"</td>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)


def free_content(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
  FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
  WHERE free_='true'
  GROUP BY title
  ORDER BY title;''')

  msg="<title>Conteúdos gratuitos</title><center><h1>Conteúdos gratuitos</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Conteúdo</th><th>Aulas</th><th>Exercícios</th><th>Material extra</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+str(row[2])+"</td>"
    msg+="<td>"+str(row[3])+"</td>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def free_content(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
  FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
  WHERE free_='true'
  GROUP BY title
  ORDER BY title;''')

  msg="<title>Conteúdos gratuitos</title><center><h1>Conteúdos gratuitos</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Conteúdo</th><th>Aulas</th><th>Exercícios</th><th>Material extra</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+str(row[2])+"</td>"
    msg+="<td>"+str(row[3])+"</td>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def comments(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT title, commentedat, name_, text_
  FROM Content_ NATURAL JOIN Comment_ NATURAL JOIN Student;''')

  msg="<title>Cometários</title><center><h1>Cometários</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Conteúdo</th><th>Data</th><th>Usuário</th><th>Comentário</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+row[0]+"</td>"
    msg+="<td>"+str(row[1])+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="<td>"+row[3]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)

def orders(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT orderedAt, Student.name_ AS aluno, cardNumber, validThrough, Product.name_ AS produto
  FROM Order_ JOIN Product USING (productId) JOIN Student USING (studentId) JOIN CreditCard USING (creditcardId)
  ORDER BY orderedAt;''')

  msg="<title>Pedidos</title><center><h1>Pedidos</h1>"

  records = cursor.fetchall()
  
  msg+="<table border=1><tr><th>Data</th><th>Usuário</th><th>Número do cartão</th><th>Validade</th><th>Produto</th></tr>"
  for row in records:
    msg+="<tr>"
    msg+="<td>"+str(row[0])+"</td>"
    msg+="<td>"+row[1]+"</td>"
    msg+="<td>"+row[2]+"</td>"
    msg+="<td>"+str(row[3])+"</td>"
    msg+="<td>"+row[4]+"</td>"
    msg+="</tr>"

  msg+="</table>"

  msg+="<p>"+str(len(records))+" registros encontrados.</p><a href=\"/\">Home</a></center>"

  return HttpResponse(msg)