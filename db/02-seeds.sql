-- Estudantes

INSERT INTO Student VALUES (
  '12345678',
  'Estudante 1',
  'estudante.1@email.com',
  1
);

INSERT INTO Student VALUES (
  '12345678',
  'Estudante 2',
  'estudante.2@email.com',
  2
);

INSERT INTO Student VALUES (
  '12345678',
  'Estudante 3',
  'estudante.4@email.com',
  3
);

INSERT INTO Student VALUES (
  '12345678',
  'Estudante 4',
  'estudante.4@email.com',
  4
);

----------------------------------------------------------------------------

INSERT INTO Product VALUES (
  'Standalone',
  25.99,
  'Um produto composto por um único curso',
  1
);

INSERT INTO Product VALUES (
  'Pacote pequeno',
  50.00,
  'Um produto composto por alguns cursos',
  2
);

INSERT INTO Product VALUES (
  'Pacote grande',
  100.00,
  'Um produto composto por vários cursos',
  3
);

----------------------------------------------------------------------------

INSERT INTO Course VALUES (
  'Primeiro curso',
  'Curso 1',
  1
);

INSERT INTO Course VALUES (
  'Segundo curso',
  'Curso 2',
  2
);

INSERT INTO Course VALUES (
  'Terceiro curso',
  'Curso 3',
  3
);

INSERT INTO Course VALUES (
  'Primeiro curso',
  'Quarto 4',
  4
);

INSERT INTO Course VALUES (
  'Quinto curso',
  'Curso 5',
  5
);

INSERT INTO Course VALUES (
  'Sexto curso',
  'Curso 6',
  6
);

----------------------------------------------------------------------------

INSERT INTO Plan VALUES (
  1,
  1
);

INSERT INTO Plan VALUES (
  2,
  2
);

INSERT INTO Plan VALUES (
  3,
  2
);

INSERT INTO Plan VALUES (
  4,
  3
);

INSERT INTO Plan VALUES (
  5,
  3
);

INSERT INTO Plan VALUES (
  6,
  3
);

----------------------------------------------------------------------------

INSERT INTO Module_ VALUES (
  'Módulo 1',
  'Primeiro módulo',
  1
);

INSERT INTO Module_ VALUES (
  'Conteúdo 2',
  'Segundo módulo',
  2
);

INSERT INTO Module_ VALUES (
  'Módulo 3',
  'Terceiro módulo',
  3
);

INSERT INTO Module_ VALUES (
  'Módulo 4',
  'Primeiro módulo',
  4
);

INSERT INTO Module_ VALUES (
  'Módulo 5',
  'Quinto módulo',
  5
);

INSERT INTO Module_ VALUES (
  'Módulo 6',
  'Sexto módulo',
  6
);

----------------------------------------------------------------------------

INSERT INTO CourseModule VALUES (
  1,
  1
);

INSERT INTO CourseModule VALUES (
  2,
  2
);

INSERT INTO CourseModule VALUES (
  3,
  3
);

INSERT INTO CourseModule VALUES (
  4,
  4
);

INSERT INTO CourseModule VALUES (
  5,
  5
);

INSERT INTO CourseModule VALUES (
  6,
  6
);

----------------------------------------------------------------------------

INSERT INTO Content_ VALUES (
  'Conteúdo 1',
  'Primeiro conteúdo - Gratuito',
  TRUE,
  1
);

INSERT INTO Content_ VALUES (
  'Conteúdo 2',
  'Segundo conteúdo - Pago',
  FALSE,
  2
);

INSERT INTO Content_ VALUES (
  'Conteúdo 3',
  'Terceiro conteúdo - Gratuito',
  TRUE,
  3
);

INSERT INTO Content_ VALUES (
  'Conteúdo 4',
  'Primeiro conteúdo - Pago',
  FALSE,
  4
);

INSERT INTO Content_ VALUES (
  'Conteúdo 5',
  'Quinto conteúdo - Gratuito',
  TRUE,
  5
);

INSERT INTO Content_ VALUES (
  'Conteúdo 6',
  'Sexto conteúdo - Pago',
  FALSE,
  6
);

----------------------------------------------------------------------------

INSERT INTO ModuleContent VALUES (
  1,
  1
);

INSERT INTO ModuleContent VALUES (
  2,
  2
);

INSERT INTO ModuleContent VALUES (
  3,
  3
);

INSERT INTO ModuleContent VALUES (
  4,
  4
);

INSERT INTO ModuleContent VALUES (
  5,
  5
);

INSERT INTO ModuleContent VALUES (
  6,
  6
);

----------------------------------------------------------------------------

INSERT INTO CreditCard VALUES (
  1234567891234567,
  '2030-01-01',
  'estudante 1',
  '123',
  0
);

INSERT INTO CreditCard VALUES (
  2345678912345671,
  '2031-01-01',
  'estudante 2',
  '231',
  1
);

INSERT INTO CreditCard VALUES (
  3456789123456712,
  '2032-01-01',
  'estudante 3',
  '312',
  2
);

----------------------------------------------------------------------------

INSERT INTO Order_ VALUES (
  current_timestamp,
  1,
  1,
  1,
  1,
  1
);

INSERT INTO Order_ VALUES (
  current_timestamp,
  6,
  2,
  2,
  2,
  2
);

INSERT INTO Order_ VALUES (
  current_timestamp,
  12,
  3,
  3,
  3,
  3
);

----------------------------------------------------------------------------

