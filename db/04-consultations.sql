------FALTA:
---GROUP BY com HAVING
---NOT EXISTS para responder questões do tipo TODOS ou NENHUM que < referencia >
---utilizar visão

-- avaliações de redação
SELECT name_, title, theme, comment_, rate, teachername
FROM Student NATURAL JOIN Essay NATURAL JOIN EssayEvaluation;

-- média de redação para cada aluno
SELECT name_, AVG(rate) AS avg_rate
FROM Student NATURAL JOIN Essay NATURAL JOIN EssayEvaluation
GROUP BY name_;

--alunos sem redações avaliadas
SELECT name_
FROM Student
WHERE studentId NOT IN (SELECT studentId FROM Essay NATURAL JOIN EssayEvaluation);

--alunos que não enviaram redações, podem ser usuários q não conhecem essa função, daí pode mandar um email explicando como funciona
--SELECT name_
--FROM Student
--WHERE studentId NOT IN (SELECT studentId FROM Essay); 

--SELECT *
--FROM Plan NATURAL JOIN Product JOIN Course USING (courseId) JOIN CourseModule USING (courseId) JOIN Module_ USING (moduleId) NATURAL JOIN --ModuleContent JOIN Content_ USING (contentId)
--WHERE free_='true';

--Produtos com content_ pago
SELECT Product.name_
FROM Plan NATURAL JOIN Product JOIN Course USING (courseId) JOIN CourseModule USING (courseId) JOIN Module_ USING (moduleId) NATURAL JOIN ModuleContent JOIN Content_ USING (contentId)
WHERE free_='false'
GROUP BY Product.name_;

--Conteúdos gratuitos
--SELECT title, description FROM Content_ WHERE free_='true';

-- exercicios disponíveis
SELECT exerciseId, difficulty, Question.name_, Option_.name_
FROM Exercise JOIN Question USING (exerciseId) JOIN Option_ USING (questionId);

-- exercicios não respondidos pelo Estudante 1
SELECT exerciseId, difficulty, Question.name_ AS questao FROM Exercise JOIN Question USING (exerciseId)
WHERE questionId NOT IN (
    SELECT questionId
    FROM Student NATURAL JOIN QuestionAnswer JOIN Option_ USING (optionId)
    WHERE Student.name_='Estudante 1');

-- gabarito do exercicio 1
SELECT difficulty, Question.name_, Option_.name_ AS opcao_correta
FROM Exercise JOIN Question USING (exerciseId) JOIN Option_ USING (questionId)
WHERE exerciseId=1 AND correct='true';

-- numero respostas corretas de cada aluno
--SELECT Student.name_, COUNT(DISTINCT questionId) AS acertos
--FROM Student NATURAL JOIN QuestionAnswer JOIN Option_ USING (optionId)
--WHERE correct='true'
--GROUP BY Student.name_
--ORDER BY Student.name_;

--numero de questões distintas respondidas por cada aluno
--SELECT Student.name_, COUNT(DISTINCT questionId) AS questoes_respondidas
--FROM Student LEFT JOIN QuestionAnswer USING (studentId) LEFT JOIN Option_ USING (optionId)
--GROUP BY Student.name_
--ORDER BY Student.name_;

--numero de questões distintas respondidas e acertos por cada aluno
SELECT Student.name_, COUNT(DISTINCT questionId) AS questoes_respondidas, COUNT(*) FILTER (WHERE correct) AS acertos
FROM Student LEFT JOIN QuestionAnswer USING (studentId) LEFT JOIN Option_ USING (optionId)
GROUP BY Student.name_
ORDER BY Student.name_;

--SELECT * FROM Exercise;
--SELECT * FROM Class_;
--SELECT * FROM ExtraMaterial;

-- conteudo e atividades
SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
GROUP BY title
ORDER BY title;

-- conteudos pagos
--SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
--FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
--GROUP BY title
--HAVING title = ANY (SELECT title FROM Content_ WHERE free_='false')
--ORDER BY title;

-- conteudos gratuitos
SELECT title AS Conteudo, COUNT(classId) AS Aulas, COUNT(exerciseId) AS Exercicios, COUNT(extramaterialId) AS MaterialExtra
FROM Content_ NATURAL LEFT JOIN Class_ NATURAL LEFT JOIN Exercise NATURAL LEFT JOIN ExtraMaterial
WHERE free_='true'
GROUP BY title
ORDER BY title;

--comentarios
SELECT title, commentedat, name_, text_
FROM Content_ NATURAL JOIN Comment_ NATURAL JOIN Student;

--atividade dos alunos
SELECT name_, consumedAt AS data, 'consumo' AS atividade
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
ORDER BY name_, data;

--pedidos
SELECT orderedAt, Student.name_ AS aluno, cardNumber, validThrough, Product.name_ AS produto
FROM Order_ JOIN Product USING (productId) JOIN Student USING (studentId) JOIN CreditCard USING (creditcardId)
ORDER BY orderedAt;

